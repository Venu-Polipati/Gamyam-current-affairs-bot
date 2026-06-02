import asyncio
from image_generator import create_image
from telegram_sender import send_photo
from rss_reader import get_latest_news
from filter import is_relevant
from formater import format_news
from telegram_sender import send_message
from datetime import datetime

today = datetime.now().strftime("%d %B %Y")
print("Starting GAMYAM...")
news_list = get_latest_news()

relevant_news = []

for news in news_list:

    if is_relevant(news):
        relevant_news.append(news)
#Removes duplicates
unique_news = []
seen = set()

for news in relevant_news:

    key = news.lower().strip()

    if key not in seen:
        seen.add(key)
        unique_news.append(news)

relevant_news = unique_news

if len(relevant_news) == 0:
    print("No relevant news found")
    exit()

combined_news = "\n".join(
    [f"{i+1}. {news}" for i, news in enumerate(relevant_news[:8])]
)

print("Sending to Gemini...")
print(combined_news)
formatted_news = format_news(combined_news)
formatted_news = (
    f"📅 GAMYAM Daily Current Affairs | {today}\n\n"
    + formatted_news
)

# image_path = create_image(
#     relevant_news[:8]
# )

# asyncio.run(
#     send_photo(
#         image_path,
#         "📅 GAMYAM Daily Current Affairs"
#     )
# )

asyncio.run(
    send_message(formatted_news)
)

print("Posted Successfully")
print(f"Unique Relevant News Found: {len(relevant_news)}")