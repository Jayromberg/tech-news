import requests
import time
from parsel import Selector


HEADER = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, header=HEADER, timeout=3)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(text=html_content)
    links = sel.css("a.cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(text=html_content)
    next_page_link = sel.css("a.next.page-numbers::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    sel = Selector(text=html_content)
    news_items = sel.css("header.entry-header")
    for news_item in news_items:
        # print(news_item.css("span.author > a::text").get())
        url = news_item.css("a::attr(href)").get()
        title = news_item.css("a::text").get()
        timestamp = news_item.css("li.meta-date::text").get()
        writer = news_item.css("span.author > a::text").get()
        print(f"{url}\n{title}\n{timestamp}\n{writer}")


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
