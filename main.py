import asyncio
import logging
from content_handlers import router as content_router
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, ADMIN_ID
from handlers import router
from database import Database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    db = Database()
    db.init_db()
    logger.info("База данных инициализирована")
    
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    dp.include_router(content_router)  # Добавляем обработчики контента
    try:
        await bot.send_message(
            ADMIN_ID,
            "🤖 Бот успешно запущен!\nВсе системы работают нормально."
        )
    except Exception as e:
        logger.warning(f"Не удалось отправить сообщение админу: {e}")
    
    logger.info("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())