import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def scrape_news(html_content: str):
    selector = Selector(html_content)
    news = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": selector.css(".post-comments-simple h5::text")
        .get() or 0,
        "summary": selector.css(".entry-content p").xpath("string()").get()
        .strip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css(".meta-category .label::text").get(),
    }
    return news
# .strip() remove os espacos no inicio e no final da string
# link: https://www.w3schools.com/python/ref_string_strip.asp
# XPath é uma linguagem para selecionar nos em documentos XML e HTML
# link: https://parsel.readthedocs.io/en/latest/usage.html


# Requisito 5
def get_tech_news(amount: int):
    base_url = "https://blog.betrybe.com/"
    news = []

    while len(news) < amount:
        trybe_page = fetch(base_url)
        links = scrape_updates(trybe_page)
        for link in links:
            if len(news) < amount:
                news.append(scrape_news(fetch(link)))
        base_url = scrape_next_page_link(trybe_page)
        if not base_url:
            break

    create_news(news)
    return news
