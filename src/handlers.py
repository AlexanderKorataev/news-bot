from aiogram import Router, types
from bot.database import Database

router = Router()
db = Database(mongo_uri='mongodb://mongo:27017')

@router.message(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет! Я новостной бот.")

@router.message(commands=["addnews"])
async def add_news(message: types.Message):
    news = message.text[len("/addnews "):]
    await db.add_news({"news": news})
    await message.answer("Новость добавлена!")

@router.message(commands=["getnews"])
async def get_news(message: types.Message):
    news_list = await db.get_news()
    response = "\n".join([item["news"] for item in news_list])
    await message.answer(f"Новости:\n{response}")