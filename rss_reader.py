import feedparser

def get_latest_news():

    feeds = [

    # International
    "http://feeds.bbci.co.uk/news/world/rss.xml",

    #"https://feeds.reuters.com/Reuters/worldNews",

    "https://news.un.org/feed/subscribe/en/news/all/rss.xml",

    # India
    "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",

    "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",

]

    news_list = []

    for feed_url in feeds:

        try:

            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:5]:

                news_list.append(entry.title)

        except Exception as e:

            print("Feed Error:", feed_url)

    return list(set(news_list))


if __name__ == "__main__":

    news = get_latest_news()

    print("Total News:", len(news))

    for item in news:

        print(item)