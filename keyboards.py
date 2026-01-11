from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# ========== ГЛАВНОЕ МЕНЮ (2 столбика) ==========
def main_menu():
    buttons = [
        [KeyboardButton(text="🍎 Моя кухня"), KeyboardButton(text="📚 Учёба в ритме")],
        [KeyboardButton(text="⚖️ Без идеала"), KeyboardButton(text="💾 Дневник питания")],
        [KeyboardButton(text="📝 Мой профиль"), KeyboardButton(text="❓ Спроси у Кати")],
        [KeyboardButton(text="👥 О нас")],
        [KeyboardButton(text="🎁 Получить подарок")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# ========== СТАРТОВАЯ КЛАВИАТУРА ==========
def start_keyboard():
    buttons = [[KeyboardButton(text="🚀 Старт")]]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# ========== КУХНЯ ==========
def kitchen_menu():
    buttons = [
        [InlineKeyboardButton(text="🍳 Завтраки за 5 минут", callback_data="kitchen_breakfast")],
        [InlineKeyboardButton(text="🥗 Обеды без готовки", callback_data="kitchen_lunch")],
        [InlineKeyboardButton(text="🍝 Ужины на скорую руку", callback_data="kitchen_dinner")],
        [InlineKeyboardButton(text="🍰 Перекусы без чувства вины", callback_data="kitchen_snack")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== УЧЁБА ==========
def study_life_menu():
    buttons = [
        [InlineKeyboardButton(text="🧠 Еда для концентрации", callback_data="study_focus")],
        [InlineKeyboardButton(text="⚡ Энергия вместо кофе", callback_data="study_energy")],
        [InlineKeyboardButton(text="😴 Что есть при усталости", callback_data="study_tired")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== БАЛАНС ==========
def balance_menu():
    buttons = [
        [InlineKeyboardButton(text="🍫 Как справляться со срывами", callback_data="balance_cravings")],
        [InlineKeyboardButton(text="⚖️ Отказ от дихотомии 'хорошо/плохо'", callback_data="balance_dichotomy")],
        [InlineKeyboardButton(text="❤️ Забота вместо контроля", callback_data="balance_care")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== ДНЕВНИК ==========
def diary_menu():
    buttons = [
        [InlineKeyboardButton(text="📝 Записать приём пищи", callback_data="diary_add")],
        [InlineKeyboardButton(text="📊 Посмотреть статистику", callback_data="diary_stats")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== ПРОФИЛЬ ==========
def profile_menu(has_questionnaire=False):
    if has_questionnaire:
        buttons = [
            [InlineKeyboardButton(text="✏️ Изменить данные", callback_data="profile_edit")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
        ]
    else:
        buttons = [
            [InlineKeyboardButton(text="📝 Заполнить анкету", callback_data="profile_start")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
        ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== СПРОСИ У КАТИ ==========
def ask_kate_menu():
    buttons = [
        [InlineKeyboardButton(text="🍩 Что делать при срыве?", callback_data="ask_cravings")],
        [InlineKeyboardButton(text="⏰ Как начать, если нет времени?", callback_data="ask_time")],
        [InlineKeyboardButton(text="😔 Как не бросить на середине?", callback_data="ask_motivation")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ========== О НАС ==========
def about_us_menu():
    buttons = [
        [InlineKeyboardButton(text="📱 Instagram", url="https://instagram.com")],
        [InlineKeyboardButton(text="📘 Telegram-канал", url="https://t.me")],
        [InlineKeyboardButton(text="💬 Чат поддержки", url="https://t.me")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
