from motor.motor_asyncio import AsyncIOMotorClient
from src.config import MONGO_URI
# class Database:
#     def __init__(self, mongo_uri):
#         self.client = AsyncIOMotorClient(mongo_uri)
#         self.db = self.client.news_bot

#     async def add_news(self, news_item):
#         await self.db.news.insert_one(news_item)

#     async def get_news(self):
#         return await self.db.news.find().to_list(length=100)




class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client.news_bot

    async def add_news(self, news_item):
        await self.db.news.insert_one(news_item)

    async def get_news(self):
        return await self.db.news.find().to_list(length=100)

    async def add_user(self, user_id, username):
        user = await self.db.users.find_one({"user_id": user_id})
        if not user:
            await self.db.users.insert_one({
                "user_id": user_id,
                "username": username,
                "subscribed": True
            })

    async def check_subscription(self, user_id):
        user = await self.db.users.find_one({"user_id": user_id})
        if user:
            return user.get("subscribed", False)
        return False

    async def update_subscription(self, user_id, subscribed):
        await self.db.users.update_one({"user_id": user_id}, {"$set": {"subscribed": subscribed}})