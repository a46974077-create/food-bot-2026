import sqlite3
import json
from datetime import datetime
from config import DB_PATH

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_db(self):
        """Создаём все таблицы"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # 1. Пользователи
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                consent BOOLEAN DEFAULT 0,
                name TEXT,
                gender TEXT,
                age INTEGER,
                height INTEGER,
                weight REAL,
                body_type TEXT,
                activity REAL,
                occupation TEXT,
                allergies TEXT,
                meals_per_day INTEGER,
                water_per_day REAL,
                sleep_schedule TEXT,
                sleep_quality TEXT,
                physical_activity TEXT,
                symptoms TEXT,
                goal TEXT,
                food_preferences TEXT,
                difficulties TEXT,
                diseases TEXT,
                medications TEXT,
                supplements TEXT,
                bmi REAL,
                ideal_weight REAL,
                bmr REAL,
                daily_calories REAL,
                protein REAL,
                fat REAL,
                carbs REAL,
                water_norm REAL,
                recommendations TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 2. Продукты
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                calories REAL NOT NULL,
                protein REAL,
                fat REAL,
                carbs REAL,
                added_by INTEGER,
                is_custom BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 3. Дневник
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS diary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date DATE DEFAULT CURRENT_DATE,
                meal_type TEXT,
                product_id INTEGER,
                quantity REAL,
                calories REAL,
                water_ml INTEGER DEFAULT 0,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        
        # 4. Статистика кликов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS button_clicks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                button_name TEXT,
                clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 5. Экспорты
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                admin_id INTEGER,
                filename TEXT,
                drive_url TEXT,
                exported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    # МЕТОДЫ ДЛЯ ПОЛЬЗОВАТЕЛЕЙ
    def user_exists(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists
    
    def get_user_profile(self, user_id):
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        profile = cursor.fetchone()
        conn.close()
        return dict(profile) if profile else None
    
    def save_user_answer(self, user_id, field, value):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET {field} = ? WHERE user_id = ?", (value, user_id))
        conn.commit()
        conn.close()
    
    def complete_questionnaire(self, user_id, data):
        conn = self.get_connection()
        cursor = conn.cursor()
        for field, value in data.items():
            if field != 'user_id':
                cursor.execute(f"UPDATE users SET {field} = ? WHERE user_id = ?", (value, user_id))
        cursor.execute("UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
    
    # МЕТОДЫ ДЛЯ ПРОДУКТОВ
    def get_product_by_name(self, name):
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name LIKE ? LIMIT 10", (f"%{name}%",))
        products = cursor.fetchall()
        conn.close()
        return [dict(p) for p in products]
    
    def add_product(self, name, calories, protein=0, fat=0, carbs=0, user_id=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, calories, protein, fat, carbs, added_by, is_custom)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, calories, protein, fat, carbs, user_id, 1))
        product_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return product_id
    
    # МЕТОДЫ ДЛЯ ДНЕВНИКА
    def add_diary_entry(self, user_id, meal_type, product_id, quantity, calories):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO diary (user_id, meal_type, product_id, quantity, calories)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, meal_type, product_id, quantity, calories))
        conn.commit()
        conn.close()
    
    def get_daily_summary(self, user_id, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT SUM(calories) as total_calories, 
                   SUM(water_ml) as total_water
            FROM diary 
            WHERE user_id = ? AND date = ?
        ''', (user_id, date))
        result = cursor.fetchone()
        conn.close()
        return {
            'total_calories': result[0] or 0,
            'total_water': result[1] or 0
        }
    
    # МЕТОДЫ ДЛЯ СТАТИСТИКИ
    def log_button_click(self, user_id, button_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO button_clicks (user_id, button_name)
            VALUES (?, ?)
        ''', (user_id, button_name))
        conn.commit()
        conn.close()
    
    def get_button_stats(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT button_name, COUNT(*) as clicks
            FROM button_clicks
            GROUP BY button_name
            ORDER BY clicks DESC
        ''')
        stats = cursor.fetchall()
        conn.close()
        return stats
    
    def get_all_users_data(self):
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.execute("SELECT * FROM diary ORDER BY date DESC")
        diary = cursor.fetchall()
        cursor.execute("SELECT * FROM button_clicks")
        clicks = cursor.fetchall()
        conn.close()
        return {
            'users': [dict(u) for u in users],
            'diary': [dict(d) for d in diary],
            'clicks': [dict(c) for c in clicks]
        }