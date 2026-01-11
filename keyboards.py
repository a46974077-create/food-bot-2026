from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# ========== КНОПКА СТАРТ ==========
def start_keyboard():
    """Клавиатура после приветствия"""
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="🚀 Старт"))
    return builder.as_markup(resize_keyboard=True)

# ========== ГЛАВНОЕ МЕНЮ ==========
def main_menu():
    """Обновленное главное меню"""
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="🍎 1. Моя кухня: рецепты"))
    builder.row(KeyboardButton(text="📚 2. Учёба в ритме жизни"))
    builder.row(KeyboardButton(text="⚖️ 3. Без идеала: баланс"))
    builder.row(KeyboardButton(text="💾 4. Мой дневник питания"))
    builder.row(KeyboardButton(text="📝 5. Мой профиль"))
    builder.row(KeyboardButton(text="❓ 6. Спроси у Кати"))
    builder.row(KeyboardButton(text="👥 7. О нас"))
    builder.row(KeyboardButton(text="🎁 8. Получить подарок"))
    return builder.as_markup(resize_keyboard=True)

# ========== РАЗДЕЛ 1: МОЯ КУХНЯ ==========
def kitchen_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🥪 Мои 5 завтраков", callback_data="kitchen_breakfasts"))
    builder.row(InlineKeyboardButton(text="🍱 Обеды с собой", callback_data="kitchen_lunches"))
    builder.row(InlineKeyboardButton(text="🍽️ Ужины за 15 минут", callback_data="kitchen_dinners"))
    builder.row(InlineKeyboardButton(text="🍎 Здоровые перекусы", callback_data="kitchen_snacks"))
    builder.row(InlineKeyboardButton(text="🏃 Питание на бегу", callback_data="kitchen_on_the_go"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== РАЗДЕЛ 2: УЧЁБА ==========
def study_life_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🧠 Топ-10 продуктов для памяти", callback_data="study_memory_foods"))
    builder.row(InlineKeyboardButton(text="📖 Как есть при учебе 12 часов", callback_data="study_12_hours"))
    builder.row(InlineKeyboardButton(text="📝 Питание перед экзаменом", callback_data="study_exam_day"))
    builder.row(InlineKeyboardButton(text="💧 Мой главный секрет ясной головы", callback_data="study_water_secret"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== РАЗДЕЛ 3: БАЛАНС ==========
def balance_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🍎 7 принципов баланса", callback_data="balance_principles"))
    builder.row(InlineKeyboardButton(text="💪 С чего начать, если нет сил", callback_data="balance_start"))
    builder.row(InlineKeyboardButton(text="⚖️ Как не срываться", callback_data="balance_no_breakdown"))
    builder.row(InlineKeyboardButton(text="⏰ Нет времени готовить", callback_data="balance_no_time"))
    builder.row(InlineKeyboardButton(text="💰 Бюджетное питание", callback_data="balance_budget"))
    builder.row(InlineKeyboardButton(text="💊 Правда о БАДах", callback_data="balance_supplements"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== РАЗДЕЛ 4: ДНЕВНИК ПИТАНИЯ ==========
def diary_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📝 Записать приём пищи", callback_data="diary_add_meal"))
    builder.row(InlineKeyboardButton(text="💧 Отметить стакан воды", callback_data="diary_add_water"))
    builder.row(InlineKeyboardButton(text="📊 Посмотреть, как прошёл день", callback_data="diary_summary"))
    builder.row(InlineKeyboardButton(text="🔍 Найти продукт в базе", callback_data="diary_search_product"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== РАЗДЕЛ 5: МОЙ ПРОФИЛЬ ==========
def profile_menu(has_questionnaire=False):
    builder = InlineKeyboardBuilder()
    if has_questionnaire:
        builder.row(InlineKeyboardButton(text="📊 Посмотреть мои данные", callback_data="profile_stats"))
        builder.row(InlineKeyboardButton(text="✏️ Обновить анкету", callback_data="profile_update"))
    else:
        builder.row(InlineKeyboardButton(text="📋 Заполнить анкету", callback_data="profile_questionnaire"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== РАЗДЕЛ 6: СПРОСИ У КАТИ ==========
def ask_kate_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="1️⃣ С чего начать, если нет сил", callback_data="faq_start_energy"))
    builder.row(InlineKeyboardButton(text="2️⃣ Как перестать заедать стресс", callback_data="faq_stress_eating"))
    builder.row(InlineKeyboardButton(text="3️⃣ Нет времени готовить", callback_data="faq_no_time_cook"))
    builder.row(InlineKeyboardButton(text="4️⃣ Бюджетное питание", callback_data="faq_budget_food"))
    builder.row(InlineKeyboardButton(text="5️⃣ Правда о БАДах", callback_data="faq_supplements"))
    builder.row(InlineKeyboardButton(text="💬 Задать свой вопрос", url="https://t.me/Ekaterina_andreeva13"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== РАЗДЕЛ 7: О НАС ==========
def about_us_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📢 Наш канал", url="https://t.me/neidealniy_nutriciolog"))
    builder.row(InlineKeyboardButton(text="💬 Группа поддержки", url="https://t.me/+guNv9c0RxTY5YjRi"))
    builder.row(InlineKeyboardButton(text="💌 Написать мне лично", url="https://t.me/Ekaterina_andreeva13"))
    builder.row(InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main"))
    return builder.as_markup()

# ========== КНОПКИ ДА/НЕТ ДЛЯ АНКЕТЫ ==========
def yes_no_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅ Да", callback_data="yes"),
        InlineKeyboardButton(text="❌ Нет", callback_data="no")
    )
    return builder.as_markup()

# ========== ДЛЯ АНКЕТЫ ==========
def gender_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="👨 Мужчина", callback_data="gender_male"))
    builder.row(InlineKeyboardButton(text="👩 Женщина", callback_data="gender_female"))
    return builder.as_markup()

def body_type_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🦴 Худощавый (астеник)", callback_data="body_type_asthenic"))
    builder.row(InlineKeyboardButton(text="💪 Средний (нормостеник)", callback_data="body_type_normosthenic"))
    builder.row(InlineKeyboardButton(text="🏋️ Крепкий (гиперстеник)", callback_data="body_type_hypersthenic"))
    builder.row(InlineKeyboardButton(text="❓ Не знаю", callback_data="body_type_unknown"))
    return builder.as_markup()

def activity_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🛌 Минимальная (1.4)", callback_data="activity_1.4"))
    builder.row(InlineKeyboardButton(text="🚶‍♂️ Легкая (1.6)", callback_data="activity_1.6"))
    builder.row(InlineKeyboardButton(text="🏃‍♀️ Средняя (1.9)", callback_data="activity_1.9"))
    builder.row(InlineKeyboardButton(text="🏋️‍♂️ Высокая (2.2)", callback_data="activity_2.2"))
    builder.row(InlineKeyboardButton(text="🔥 Очень высокая (2.5)", callback_data="activity_2.5"))
    return builder.as_markup()