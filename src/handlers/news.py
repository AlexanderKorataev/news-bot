from aiogram import Router, types, F
# from src.database import Database
# from src.config import MONGO_URI
# from aiogram import Bot, Dispatcher, html
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
from src.database.database import Database
from aiogram.filters import CommandStart, Command

news_router = Router()
db = Database()
# @news_router.callback_query(F.data == "subscribe")
# async def subscribe(callback: types.CallbackQuery):
#         await callback.message.answer(
# """Вы успешно подписались на новостную рассылку! 📰
# Теперь вы будете получать самые свежие новости."""
# )

# @news_router.callback_query(F.data == "unsubscribe")
# async def unsubscribe(callback: types.CallbackQuery):
#         await callback.message.answer(
# """Вы отключили новостную рассылку. 
# Если захотите снова получать новости, просто введите /subscribe."""
# )

# @news_router.callback_query(F.data == "subscribe")
# async def subscribe(callback: types.CallbackQuery):
#     user_id = callback.from_user.id
#     username = callback.from_user.username

#     await db.add_user(user_id, username)
#     await db.update_subscription(user_id, True)
    
#     await callback.message.answer(
#         """Вы успешно подписались на новостную рассылку! 📰
# Теперь вы будете получать самые свежие новости."""
#     )


# @news_router.callback_query(F.data == "unsubscribe")
# async def unsubscribe(callback: types.CallbackQuery):
#     user_id = callback.from_user.id
#     await db.update_subscription(user_id, False)

#     await callback.message.answer(
#         """Вы отключили новостную рассылку. 
# Если захотите снова получать новости, просто введите /subscribe."""
#     )




# Обработчик нажатий на кнопки подписки/отписки
@news_router.callback_query(F.data.in_({"subscribe", "unsubscribe"}))
async def handle_subscription(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if callback.data == "subscribe":
        await db.update_subscription(user_id, True)
        await callback.message.answer("Вы успешно подписались на новостную рассылку! 📰")
    elif callback.data == "unsubscribe":
        await db.update_subscription(user_id, False)
        await callback.message.answer("Вы успешно отключили новостную рассылку.")

    # Обновляем клавиатуру после изменения статуса подписки
    is_subscribed = await db.check_subscription(user_id)
    await callback.message.edit_reply_markup(reply_markup=get_subscribe_keyboard(is_subscribed))









# @router.message(Command("addnews"))
# async def add_news(message: types.Message):
#     news = message.text[len("/addnews "):]
#     await db.add_news({"news": news})
#     await message.answer("Новость добавлена!")

# @router.message(Command("getnews"))
# async def get_news(message: types.Message):
#     news_list = await db.get_news()
#     response = "\n".join([item["news"] for item in news_list])
#     await message.answer(f"Новости:\n{response}")