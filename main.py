import asyncio
from aiogram import Bot, Dispatcher
from src.handlers.start import start_router
from src.handlers.news import news_router
from src.config import BOT_TOKEN

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(news_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())