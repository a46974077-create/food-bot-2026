import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📚 Учёба в ритме жизни")],
            [types.KeyboardButton(text="🍎 Питание для занятых")],
            [types.KeyboardButton(text="⚖️ Баланс без надрыва")],
            [types.KeyboardButton(text="❓ Частые вопросы")],
            [types.KeyboardButton(text="📝 Мой профиль")],
            [types.KeyboardButton(text="💾 Дневник питания")],
            [types.KeyboardButton(text="🎁 Получить подарок")],
            [types.KeyboardButton(text="👥 О нас")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "Привет! Я твой помощник по питанию и учебе. 🍎📚\n"
        "Я помогу тебе сбалансировать питание, учебу и отдых.\n"
        "Выбери раздел ниже:",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
