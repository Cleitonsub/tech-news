from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=itemgetter('comments_count'), reverse=True)

    result = [(new["title"], new["url"]) for new in news][:5]
    return result if result else []


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
