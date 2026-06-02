from keywords import KEYWORDS, EXCLUDE_KEYWORDS

def is_relevant(news):

    news = news.lower()

    # Reject junk first
    for word in EXCLUDE_KEYWORDS:

        if word.lower() in news:
            return False

    # Then allow useful news
    for keyword in KEYWORDS:

        if keyword.lower() in news:
            return True

    return False