from keywords import KEYWORDS

def is_relevant(news):

    for keyword in KEYWORDS:

        if keyword.lower() in news.lower():
            return True

    return False