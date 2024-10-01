from aiogram import Router, types
# from src.database import Database
# from src.config import MONGO_URI
# from aiogram import Bot, Dispatcher, html
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
from src.database.database import Database
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command

start_router = Router()
db = Database()
# def get_subscribe_keyboard():
#     builder = InlineKeyboardBuilder()
#     builder.button(
#         text="Подписаться ✅",
#         callback_data="subscribe"
#     )

#     builder.adjust(1)

#     return builder.as_markup()

# @start_router.message(CommandStart())
# async def start_command(message: types.Message):
    
#     await message.answer(
# """Привет! 👋

# Это бот для получения актуальных новостей. Вы можете подписаться на рассылку и получать последние новости прямо здесь.

# Команды:
# /subscribe - Подключить новостную рассылку.
# /unsubscribe - Отключить рассылку.
# /help - Получить список команд.""", reply_markup=get_subscribe_keyboard()
# )






# db = Database(mongo_uri=MONGO_URI)


# @router.message(Command("addnews"))
# async def add_news(message: types.Message):
#     news = message.text[len("/addnews "):]
#     await db.add_news({"news": news})
#     await message.answer("Новость добавлена!")

# @router.message(Command("getnews"))
# async def get_news(message: types.Message):
#     news_list = await db.get_news()
#     response = "\n".join([item["news"] for item in news_list])
#     await message.answer(f"Новости:\n{response}")# Функция для создания клавиатуры


#     builder = InlineKeyboardBuilder()
#     builder.button(
#         text="Подписаться ✅",
#         callback_data="subscribe"
#     )

#     builder.adjust(1)

#     return builder.as_markup()



def get_subscribe_keyboard(is_subscribed):
    if is_subscribed:
        return InlineKeyboardBuilder().button(
        text="Отписаться 🚫",
        callback_data="unsubscribe"
    ).adjust(1).as_markup()
    else:
        return InlineKeyboardBuilder().button(
        text="Подписаться ✅",
        callback_data="subscribe"
    ).adjust(1).as_markup()

# Обработчик команды /start
@start_router.message(CommandStart())
async def start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Добавляем пользователя в базу данных
    await db.add_user(user_id, username)

    # Проверяем статус подписки пользователя
    is_subscribed = await db.check_subscription(user_id)

    # Отправляем приветственное сообщение с динамической клавиатурой
    await message.answer(
        """Привет! 👋

Это бот для получения актуальных новостей. Вы можете подписаться на рассылку и получать последние новости прямо здесь.

Команды:
/subscribe - Подключить новостную рассылку.
/unsubscribe - Отключить рассылку.
/help - Получить список команд.""",
        reply_markup=get_subscribe_keyboard(is_subscribed)
    )

