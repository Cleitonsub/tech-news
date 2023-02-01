from tech_news.database import search_news
from datetime import date as dt


# Requisito 6
def search_by_title(title: str):
    title = search_news({'title': {"$regex": title.lower()}})

    result = [(titles['title'], titles['url']) for titles in title]
    return result if result else []


# Requisito 7
def search_by_date(date: str):
    try:
        formated_date = dt.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError('Data inválida')

    news = search_news({'timestamp': formated_date})
    result = [(new['title'], new['url']) for new in news]
    return result if result else []


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
