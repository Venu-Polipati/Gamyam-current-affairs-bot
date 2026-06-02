import feedparser

def get_latest_news():

    feeds = [

    # India
    "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",

    "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",

    # Economy
    "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",

    # Science & Tech
   # "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",

    # PIB
    "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3",

    # International
    "http://feeds.bbci.co.uk/news/world/rss.xml"

    # Andhra Pradesh
    #"https://www.thehansindia.com/rss/andhra-pradesh",
    # AP News
    "https://www.newsonair.gov.in/category/state-news/andhra-pradesh/feed/",
]

    news_list = []

    for feed_url in feeds:

        try:

            feed = feedparser.parse(feed_url)
            print(feed_url, len(feed.entries))


            for entry in feed.entries[:8]:

                news_list.append(entry.title)

        except Exception as e:

            print("Feed Error:", feed_url)

    return list(set(news_list))


if __name__ == "__main__":

    news = get_latest_news()

    print("Total News:", len(news))

    for item in news:

        print(item)

