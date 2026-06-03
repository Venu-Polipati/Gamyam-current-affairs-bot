import feedparser

def get_latest_news():

    feeds = [

# TOI India
"https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",

# TOI Business
"https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",

# PIB
"https://pib.gov.in/PressReleasePage.aspx?PRID=RSS",

# AIR National
"https://www.newsonair.gov.in/feed/",

# AP News
"https://www.newsonair.gov.in/category/state-news/andhra-pradesh/feed/",

 "https://www.thehindu.com/news/national/feeder/default.rss",
"https://www.pib.gov.in/ViewRss.aspx?reg=1&lang=1",
"https://timesofindia.indiatimes.com/rssfeeds/2950554.cms",


]

    news_list = []

    for feed_url in feeds:

        try:

            feed = feedparser.parse(feed_url)

            print(feed_url, len(feed.entries))
            print(feed.feed.get("title", "NO TITLE"))
            print("Entries:", len(feed.entries))


            for entry in feed.entries[:15]:

                title = entry.title.strip()
                if len(title) > 20:
                    news_list.append(title)


        except Exception as e:

            print("Feed Error:", feed_url)

    return list(set(news_list))


if __name__ == "__main__":

    news = get_latest_news()

    print("Total News:", len(news))
    print("\nTOTAL RAW NEWS:", len(news))

    for item in news:

        print(item)

