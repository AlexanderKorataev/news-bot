from aiogram import Router, types
from src.database import Database
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7377998051:AAEYkjTJSrs373KrYO68Ni2I-Q9xbO1zuE0"

# All handlers should be attached to the Router (or Dispatcher)

router = Router()
db = Database(mongo_uri='mongodb://mongo:27017')

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет! Я новостной бот.")

@router.message(Command("addnews"))
async def add_news(message: types.Message):
    news = message.text[len("/addnews "):]
    await db.add_news({"news": news})
    await message.answer("Новость добавлена!")

@router.message(Command("getnews"))
async def get_news(message: types.Message):
    news_list = await db.get_news()
    response = "\n".join([item["news"] for item in news_list])
    await message.answer(f"Новости:\n{response}")