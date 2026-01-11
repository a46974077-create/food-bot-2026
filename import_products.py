"""
import_products.py - Импорт продуктов из Excel файла
"""

import sqlite3
import pandas as pd
from config import DB_PATH

def import_from_excel():
    """Импортирует продукты из Excel файла в базу данных"""
    
    try:
        # Читаем Excel файл
        df = pd.read_excel('Список продуктов.xlsx', sheet_name='ккал. разрешённые продукты')
        
        # Подключаемся к базе данных
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Счётчики
        imported = 0
        skipped = 0
        
        # Проходим по строкам
        for index, row in df.iterrows():
            # Пропускаем заголовки
            if pd.isna(row['продукты']) or row['продукты'] in ['продукты', 'Белок', 'Жиры', 'Углеводы']:
                continue
            
            product_name = str(row['продукты']).strip()
            
            if len(product_name) < 2:
                skipped += 1
                continue
            
            try:
                # Получаем значения из столбцов
                calories = float(str(row['ккал 100 гр.']).replace(',', '.')) if not pd.isna(row['ккал 100 гр.']) else 0
                
                # Ищем столбцы с БЖУ (они могут называться по-разному)
                protein = 0
                fat = 0
                carbs = 0
                
                # Пробуем разные варианты названий столбцов
                if 'Б\nна 100г' in df.columns:
                    protein = float(str(row['Б\nна 100г']).replace(',', '.')) if not pd.isna(row['Б\nна 100г']) else 0
                elif 'Б' in df.columns:
                    protein = float(str(row['Б']).replace(',', '.')) if not pd.isna(row['Б']) else 0
                
                if 'Ж\nна 100г' in df.columns:
                    fat = float(str(row['Ж\nна 100г']).replace(',', '.')) if not pd.isna(row['Ж\nна 100г']) else 0
                elif 'Ж' in df.columns:
                    fat = float(str(row['Ж']).replace(',', '.')) if not pd.isna(row['Ж']) else 0
                
                if 'У\nна 100г' in df.columns:
                    carbs = float(str(row['У\nна 100г']).replace(',', '.')) if not pd.isna(row['У\nна 100г']) else 0
                elif 'У' in df.columns:
                    carbs = float(str(row['У']).replace(',', '.')) if not pd.isna(row['У']) else 0
                    
            except (ValueError, TypeError):
                skipped += 1
                continue
            
            # Добавляем продукт
            cursor.execute('''
                INSERT OR REPLACE INTO products 
                (name, calories, protein, fat, carbs, added_by, is_custom)
                VALUES (?, ?, ?, ?, ?, NULL, 0)
            ''', (product_name, calories, protein, fat, carbs))
            
            imported += 1
        
        conn.commit()
        
        # Получаем общее количество
        cursor.execute("SELECT COUNT(*) FROM products WHERE is_custom = 0")
        total = cursor.fetchone()[0]
        
        conn.close()
        
        return f"✅ Импортировано {imported} продуктов. Пропущено {skipped}. Всего в базе: {total} продуктов."
        
    except FileNotFoundError:
        return f"❌ Файл не найден: 'Список продуктов.xlsx'"
    except Exception as e:
        return f"❌ Ошибка при импорте: {str(e)}"

if __name__ == "__main__":
    result = import_from_excel()
    print(result)