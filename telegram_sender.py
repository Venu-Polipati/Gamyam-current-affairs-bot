from telegram import Bot
from telegram.constants import ParseMode
from config import BOT_TOKEN, CHANNEL_ID


async def send_message(message):

    bot = Bot(token=BOT_TOKEN)

    max_length = 4000

    for i in range(0, len(message), max_length):

        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message[i:i + max_length],
            parse_mode=ParseMode.HTML
        )


async def send_photo(photo_path, caption=""):

    bot = Bot(token=BOT_TOKEN)

    with open(photo_path, "rb") as photo:

        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo,
            caption=caption
        )