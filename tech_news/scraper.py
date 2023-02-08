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
    news_item = sel.css("div.entry-header-inner")

    url = sel.css("link[rel=canonical]::attr(href)").get()
    title = news_item.css("h1::text").get().strip()
    timestamp = news_item.css("li.meta-date::text").get()
    writer = news_item.css("span.author > a::text").get()
    reading_time = int(news_item.css(
                "li.meta-reading-time::text"
            ).get().split()[0])
    summary = ''.join(
            sel.css("div.entry-content > p:nth-of-type(1) ::text").getall()
        ).strip()
    category = news_item.css("span.label::text").get()

    return {
        "url": url, "title": title, "timestamp": timestamp,
        "writer": writer, "reading_time": reading_time,
        "summary": summary, "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
