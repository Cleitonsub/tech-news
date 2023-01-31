import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str, timeout: int = 3):
    fake = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout, headers=fake)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str):
    selector = Selector(html_content)
    links = selector.css('a.cs-overlay-link::attr(href)').getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content: str):
    selector = Selector(html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page if next_page else None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
