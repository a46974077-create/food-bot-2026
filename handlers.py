from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from config import ADMIN_ID
from keyboards import *
from database import Database

router = Router()
db = Database()

# ========== КОМАНДА /START ==========
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    
    welcome_text = f"""
🌟 Привет, {username}!

Я NutriDiary Bot - помощник от Кати (того самого неидеального нутрициолога 😉).

Я помогу тебе:
🍎 Улучшить питание без фанатизма
🧠 Найти энергию для учёбы/работы
⚡ Справляться со срывами без чувства вины
🍳 Готовить быстро (даже если не любишь готовить)

Нажми кнопку 🚀 Старт чтобы начать!

*P.S. Все советы - это «опоры», а не правила. Бери то, что отзывается, и адаптируй под свою жизнь.*
    """
    
    await message.answer(
        welcome_text,
        reply_markup=start_keyboard(),
        parse_mode="Markdown"
    )
    
    # Отправляем PDF-подарок
    try:
        with open("13_opor.pdf", "rb") as file:
            await message.answer_document(
                file,
                caption="🎁 *Ваш подарок — гайд по питанию!*\n\nЭто основа моего подхода, сжатый опыт моего пути к балансу.",
                parse_mode="Markdown"
            )
    except FileNotFoundError:
        await message.answer(
            "📘 *Гайд будет доступен совсем скоро!*\nСейчас мы работаем над его обновлением 💫",
            parse_mode="Markdown"
        )
    
    db.log_button_click(user_id, "start_command")

# ========== КНОПКА "🚀 СТАРТ" ==========
@router.message(F.text == "🚀 Старт")
async def start_main_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "start_main")
    
    main_text = """
📚 *Главное меню: «Мой лайфхак: как есть, чтобы учиться и всё успевать»*

Привет! Здесь собрано всё, что реально работает в моей жизни: от рецептов за 5 минут до принципов, которые спасают от срывов. Выбирай, что нужно прямо сейчас.

---

🍎 *1. Моя кухня*: рецепты для дня, когда время есть, но его нет

📚 *2. Учёба в ритме жизни*: как кормить мозг, а не усталость

⚖️ *3. Без идеала*: как я перестала бороться с едой и собой

💾 *4. Мой дневник питания*: твой личный уголок для наблюдений

📝 *5. Мой профиль*: здесь мы знакомимся ближе

❓ *6. Спроси у Кати*: вот что меня реально спасает

👥 *7. О нас*: давай знакомиться

🎁 *8. Получить подарок*: моя шпаргалка «Старт без стресса»
    """
    
    await message.answer(
        main_text,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# ========== РАЗДЕЛ 1: МОЯ КУХНЯ ==========
@router.message(F.text == "🍎 1. Моя кухня: рецепты")
async def kitchen_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "kitchen_menu")
    
    text = """
🍎 *1. Моя кухня: рецепты для дня, когда время есть, но его нет*

Когда ты мама, медсестра и студентка, «нормально поесть» — это акт заботы о себе. Здесь — моя система «кухонного конвейера» и рецепты, которые собираются быстрее, чем дети в сад.

Выбери категорию:
    """
    
    await message.answer(
        text,
        reply_markup=kitchen_menu(),
        parse_mode="Markdown"
    )

# ========== РАЗДЕЛ 2: УЧЁБА ==========
@router.message(F.text == "📚 2. Учёба в ритме жизни")
async def study_life_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "study_life_menu")
    
    text = """
📚 *2. Учёба в ритме жизни: как кормить мозг, а не усталость*

Мой опыт учёбы в трёх местах одновременно: что есть, чтобы голова ясно соображала даже на 12-й час марафона.

Выбери тему:
    """
    
    await message.answer(
        text,
        reply_markup=study_life_menu(),
        parse_mode="Markdown"
    )

# ========== РАЗДЕЛ 3: БАЛАНС ==========
@router.message(F.text == "⚖️ 3. Без идеала: баланс")
async def balance_new_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "balance_menu")
    
    text = """
⚖️ *3. Без идеала: как я перестала бороться с едой и собой*

Не философия, а выжимка моего опыта. История о том, как я перестала делить еду на «хорошую» и «плохую», а себя — на «молодец» и «сорвалась».

Выбери вопрос:
    """
    
    await message.answer(
        text,
        reply_markup=balance_menu(),
        parse_mode="Markdown"
    )

# ========== РАЗДЕЛ 4: ДНЕВНИК ПИТАНИЯ ==========
@router.message(F.text == "💾 4. Мой дневник питания")
async def diary_handler(message: Message):
    user_id = message.from_user.id
    profile = db.get_user_profile(user_id)
    if not profile or not profile.get('consent'):
        await message.answer("📝 *Сначала заполните анкету!*", reply_markup=main_menu(), parse_mode="Markdown")
        return
    
    text = """
💾 *4. Мой дневник питания: твой личный уголок для наблюдений*

Сюда я записываю не калории, а ощущения. Что дало энергию? После чего потянуло в сон? Это твой инструмент, чтобы узнать язык своего тела, а не наказание.
    """
    
    await message.answer(
        text,
        reply_markup=diary_menu(),
        parse_mode="Markdown"
    )
    db.log_button_click(user_id, "diary_menu")

# ========== РАЗДЕЛ 5: МОЙ ПРОФИЛЬ ==========
@router.message(F.text == "📝 5. Мой профиль")
async def profile_handler(message: Message):
    user_id = message.from_user.id
    profile = db.get_user_profile(user_id)
    has_questionnaire = bool(profile and profile.get('name'))
    
    if has_questionnaire:
        text = f"""
👤 *Ваш профиль*

*Имя:* {profile['name']}
*Возраст:* {profile['age']} лет
*Рост:* {profile['height']} см
*Вес:* {profile['weight']} кг
*ИМТ:* {profile['bmi']}

*Ваши нормы:*
• Калории: {profile['daily_calories']} ккал
• Белки: {profile['protein']} г
• Жиры: {profile['fat']} г
• Углеводы: {profile['carbs']} г
• Вода: {profile['water_norm']} мл

*Цель:* {profile['goal']}
        """
        await message.answer(
            text.strip(),
            reply_markup=profile_menu(has_questionnaire=True),
            parse_mode="Markdown"
        )
    else:
        text = """
📝 *5. Мой профиль: здесь мы знакомимся ближе*

Расскажи немного о себе, своих целях и сложностях. Так мне будет проще делиться тем, что может пригодиться именно тебе.
        """
        await message.answer(
            text,
            reply_markup=profile_menu(has_questionnaire=False),
            parse_mode="Markdown"
        )
    db.log_button_click(user_id, "profile_menu")

# ========== РАЗДЕЛ 6: СПРОСИ У КАТИ ==========
@router.message(F.text == "❓ 6. Спроси у Кати")
async def ask_kate_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "ask_kate_menu")
    
    text = """
❓ *6. Спроси у Кати: вот что меня реально спасает*

Ответы на вопросы, которые мне задают чаще всего. Не теория из учебников, а мой личный опыт пробы, ошибки и находки.

Выбери вопрос:
    """
    
    await message.answer(
        text,
        reply_markup=ask_kate_menu(),
        parse_mode="Markdown"
    )

# ========== РАЗДЕЛ 7: О НАС ==========
@router.message(F.text == "👥 7. О нас")
async def about_us_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "about_us_menu")
    
    text = """
👥 *7. О нас: давай знакомиться*

Привет! Рада, что тебе интересно наше сообщество 💖

Это пространство родилось не из желания поучить. Оно родилось из страха, бессонных ночей и понимания, что «идеально» — это скучно и… неправдиво.

*Кто я?* Меня зовут Катя. Я — человек в постоянном движении:
▪️ Вечная студентка: учусь на врача и психолога.
▪️ Практик: работаю старшей медсестрой.
▪️ Мама: растию двоих детей.
▪️ Наблюдатель: пытаюсь не забыть про себя в этом потоке и замечать, что на самом деле работает.

Где продолжить разговор?
    """
    
    await message.answer(
        text,
        reply_markup=about_us_menu(),
        parse_mode="Markdown"
    )

# ========== РАЗДЕЛ 8: ПОЛУЧИТЬ ПОДАРОК ==========
@router.message(F.text == "🎁 8. Получить подарок")
async def gift_handler(message: Message):
    user_id = message.from_user.id
    db.log_button_click(user_id, "gift_menu")
    
    text = """
🎁 *8. Получить подарок: моя шпаргалка «Старт без стресса»*

PDF-файл с моими самыми простыми и работающими схемами: план питания на неделю, чек-лист «База на кухне», список продуктов для занятых. Чтобы у тебя было четкое руководство к действию.

(Файл отправляется сразу)
    """
    
    await message.answer(text, parse_mode="Markdown")
    
    # Отправляем PDF
    try:
        with open("13_opor.pdf", "rb") as file:
            await message.answer_document(
                file,
                caption="🎁 *Ваш подарок — шпаргалка «Старт без стресса»!*",
                parse_mode="Markdown"
            )
    except FileNotFoundError:
        await message.answer(
            "📘 *Файл будет доступен совсем скоро!*",
            parse_mode="Markdown"
        )

# ========== ОБРАБОТКА КНОПКИ "НАЗАД" ==========
@router.callback_query(F.data.startswith("back_to_"))
async def back_handler(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    target = callback.data.replace("back_to_", "")
    db.log_button_click(user_id, f"back_to_{target}")
    await state.clear()
    await callback.message.edit_text("Вы вернулись в главное меню:", reply_markup=main_menu())
    await callback.answer()

# ========== ОБРАБОТКА "ДА"/"НЕТ" ДЛЯ АНКЕТЫ ==========
@router.callback_query(F.data.in_(["yes", "no"]))
async def yes_no_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data == "yes":
        await callback.message.edit_text("✅ *Спасибо за согласие!*\n\nПереходим к анкете...", parse_mode="Markdown")
        # Здесь будет переход к анкете
        await callback.answer()
    else:
        await callback.message.edit_text("❌ *Вы отказались от обработки данных*", parse_mode="Markdown")
        await state.clear()
        await callback.answer()