from tech_news.database import find_news
from operator import itemgetter
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=itemgetter('comments_count'), reverse=True)

    result = [(new["title"], new["url"]) for new in news][:5]
    return result if result else []


# Requisito 11
def top_5_categories():
    news = find_news()
    categories = [new["category"] for new in news]
    top_categories = Counter(sorted(categories)).most_common(5)
    # pega o primeiro item tupla
    result = [category[0] for category in top_categories]
    return result if result else []
