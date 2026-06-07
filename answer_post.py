import asyncio
from telegram_sender import send_message

with open(
    "daily_answers.txt",
    "r",
    encoding="utf-8"
) as f:
    answers = f.read()

print(answers)

asyncio.run(
    send_message(answers)
)