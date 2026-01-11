from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# ========== ГЛАВНОЕ МЕНЮ (2 столбика + 2 большие) ==========
def main_menu():
    """
    Главное меню после нажатия "🚀 Старт"
    2 колонки + 2 большие кнопки внизу
    """
    buttons = [
        [KeyboardButton(text="📚 Учёба в ритме жизни"), KeyboardButton(text="🍎 Питание для занятых")],
        [KeyboardButton(text="⚖️ Баланс без надрыва"), KeyboardButton(text="❓ Частые вопросы")],
        [KeyboardButton(text="📝 Мой профиль"), KeyboardButton(text="💾 Дневник питания")],
        [KeyboardButton(text="👥 О нас")],  # Большая кнопка (во всю ширину)
        [KeyboardButton(text="🎁 Получить подарок")]  # Большая кнопка (во всю ширину)
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# ========== СТАРТОВАЯ КЛАВИАТУРА (только 🚀 Старт) ==========
def start_keyboard():
    """Клавиатура только с кнопкой Старт после /start"""
    buttons = [[KeyboardButton(text="🚀 Старт")]]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# ========== ПИТАНИЕ ДЛЯ ЗАНЯТЫХ (inline меню) ==========
def nutrition_menu():
    """
    Inline-меню для раздела "Питание для занятых"
    После вступительного текста
    """
    buttons = [
        [InlineKeyboardButton(text="🥪 Быстрые завтраки", callback_data="nutrition_breakfasts")],
        [InlineKeyboardButton(text="🍱 Обеды на бегу", callback_data="nutrition_lunches")],
        [InlineKeyboardButton(text="🍽️ Ужины за 15 минут", callback_data="nutrition_dinners")],
        [InlineKeyboardButton(text="🍎 Здоровые перекусы", callback_data="nutrition_snacks")],
        [InlineKeyboardButton(text="🏃 Питание на бегу", callback_data="nutrition_on_the_go")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== УЧЁБА В РИТМЕ ЖИЗНИ ==========
def study_menu():
    """
    Inline-меню для раздела "Учёба в ритме жизни"
    После вступительного текста
    """
    buttons = [
        [InlineKeyboardButton(text="🧠 Продукты для памяти", callback_data="study_memory")],
        [InlineKeyboardButton(text="📖 Как есть при учебе 12 часов", callback_data="study_12_hours")],
        [InlineKeyboardButton(text="📝 Питание перед экзаменом", callback_data="study_exam_day")],
        [InlineKeyboardButton(text="💧 Вода и мозг", callback_data="study_water_secret")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== БАЛАНС БЕЗ НАДРЫВА (без inline, только текст) ==========
# Для этого раздела inline-меню не нужно, только текст и кнопка назад

# ========== ЧАСТЫЕ ВОПРОСЫ ==========
def faq_menu():
    """
    Inline-меню для раздела "Частые вопросы"
    После вступительного текста
    """
    buttons = [
        [InlineKeyboardButton(text="1️⃣ С чего начать, если нет сил?", callback_data="faq_start_energy")],
        [InlineKeyboardButton(text="2️⃣ Как не срываться?", callback_data="faq_stress_eating")],
        [InlineKeyboardButton(text="3️⃣ Что делать, если нет времени готовить?", callback_data="faq_no_time_cook")],
        [InlineKeyboardButton(text="4️⃣ Как питаться бюджетно?", callback_data="faq_budget_food")],
        [InlineKeyboardButton(text="5️⃣ Про БАДы (мой опыт)", callback_data="faq_supplements")],
        [InlineKeyboardButton(text="💬 Задать свой вопрос", callback_data="faq_ask_question")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== ДНЕВНИК ПИТАНИЯ ==========
def diary_menu():
    """
    Inline-меню для раздела "Дневник питания"
    После вступительного текста
    """
    buttons = [
        [InlineKeyboardButton(text="📝 Записать приём пищи", callback_data="diary_add")],
        [InlineKeyboardButton(text="💧 Добавить воду", callback_data="diary_add_water")],
        [InlineKeyboardButton(text="📊 Посмотреть статистику", callback_data="diary_stats")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== ПРОФИЛЬ ==========
def profile_menu(has_questionnaire=False):
    """
    Inline-меню для раздела "Мой профиль"
    После вступительного текста
    """
    if has_questionnaire:
        buttons = [
            [InlineKeyboardButton(text="👀 Посмотреть мои данные", callback_data="profile_view")],
            [InlineKeyboardButton(text="✏️ Обновить анкету", callback_data="profile_edit")],
            [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton(text="📋 Заполнить анкету", callback_data="profile_start")],
            [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
        ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== О НАС ==========
def about_us_menu():
    """
    Inline-меню для раздела "О нас"
    После вступительного текста
    """
    buttons = [
        [InlineKeyboardButton(text="📢 Telegram-канал", url="https://t.me/neidealniy_nutriciolog")],
        [InlineKeyboardButton(text="💬 Чат поддержки", url="https://t.me/+guNv9c0RxTY5YjRi")],
        [InlineKeyboardButton(text="👤 Написать Кате", url="https://t.me/Ekaterina_andreeva13")],
        [InlineKeyboardButton(text="⬅️ Назад в главное меню", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== КНОПКА НАЗАД ДЛЯ ПОДРАЗДЕЛОВ ==========
def back_button(target_menu):
    """
    Создает клавиатуру только с кнопкой "Назад"
    target_menu: куда ведет кнопка (например, "nutrition", "study")
    """
    buttons = [
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=f"back_to_{target_menu}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
