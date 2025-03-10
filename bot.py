import asyncio
import logging
import nest_asyncio
from pyrogram import Client
from pyrogram import idle

# ✅ PyCharm ва Jupyter Notebook учун event loop муаммосини ҳал қилиш
nest_asyncio.apply()

# 📌 Логларни кўриш учун logging ёқиб қўйиш
logging.basicConfig(level=logging.INFO)

# 📌 Telegram'да бот яратиш учун маълумотлар (аниқланг!)
API_ID = 26013710  # 🔹 my.telegram.org сайтидан олинади
API_HASH = "e463b5122908e7aa5b05d6000145b113"  # 🔹 my.telegram.org сайтидан олинади
BOT_TOKEN = "8071302436:AAHrdj7kbZfzi4voazCRRJKMUFIRiOwachI"  # 🔹 @BotFather орқали олинади

# 📌 Pyrogram бот объектимиз
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 📌 Асосий ишловчи функция
async def main():
    logging.info("Бот ишга тушди!")  # Бот старт бўлганини билдиради
    await app.start()  # Ботни ишга туширамиз
    await idle()  # Ботни ишлаб туриши учун кутамиз
    await app.stop()  # Агар ботни тўхтатиш керак бўлса

# 📌 Ботни ишга тушириш
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())  # 🔹 `asyncio.run(main())` ўрнига ишлайди
