from keywords import KEYWORDS, EXCLUDE_KEYWORDS

def is_relevant(news):

    news = news.lower()

    # Reject unwanted news first
    for word in EXCLUDE_KEYWORDS:
        if word.lower() in news:
            return False

    score = 0

    # Count matching keywords
    for keyword in KEYWORDS:
        if keyword.lower() in news:
            score += 1

    # Accept if at least one useful keyword found
    if score >= 1:
        return True

    return False