import asyncio
import os
from aiohttp import web
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
    # Создаём маленький веб-сервер для Render
    async def health(request):
        return web.Response(text="OK")
    
    app = web.Application()
    app.router.add_get("/", health)
    
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info(f"Веб-сервер запущен на порту {port}")
    logger.info("База данных инициализирована")
    
    bot = Bot(token=BOT_TOKEN)  # Убрал HTML-разметку временно
    
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    dp.include_router(content_router)
    
    try:
        await bot.send_message(
            ADMIN_ID,
            "Бот запущен."  # Упростил сообщение
        )
    except Exception as e:
        logger.warning(f"Не удалось отправить сообщение админу: {e}")
    
    logger.info("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
