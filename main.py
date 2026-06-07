import asyncio
from telegram import Bot

TOKEN = "8661877739:AAGjTswGxMLN-r16GTSORHnaNQBSiWftXwE"
CHANNEL_ID = "1119960739"

async def send_message():
    bot = Bot(token=TOKEN)

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="🔥 Hello from GAMYAM Bot"
    )

asyncio.run(send_message())