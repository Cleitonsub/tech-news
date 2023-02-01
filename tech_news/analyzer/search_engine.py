from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str):
    title = search_news({'title': {"$regex": title.lower()}})
    result = [(titles['title'], titles['url']) for titles in title]
    return result if result else []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
