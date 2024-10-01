from aiogram import Router, types
# from src.database import Database
# from src.config import MONGO_URI
# from aiogram import Bot, Dispatcher, html
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
from src.database.database import Database
from aiogram.filters import CommandStart, Command


admin_router = Router()
db = Database()

# Проверка, является ли пользователь администратором
def is_admin(user_id):
    # Добавьте здесь свой список администраторов
    return user_id in [901705591]

@admin_router.message(Command("add_news"))
async def add_news(message: types.Message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        await message.answer("У вас нет прав для добавления новостей.")
        return
    
    news_item = message.text[len("/add_news "):]
    await db.add_news({"news": news_item})

    await message.answer("Новость успешно добавлена!")
