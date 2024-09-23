from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    def __init__(self, mongo_uri):
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client.news_bot

    async def add_news(self, news_item):
        await self.db.news.insert_one(news_item)

    async def get_news(self):
        return await self.db.news.find().to_list(length=100)