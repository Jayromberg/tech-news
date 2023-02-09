import requests
import time
from parsel import Selector
from tech_news.database import create_news


HEADER = {'User-agent': 'Fake user-agent'}
URL = "https://blog.betrybe.com"


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
    div_header = sel.css("div.entry-header-inner")

    url = sel.css("link[rel=canonical]::attr(href)").get()
    title = div_header.css("h1::text").get().strip()
    timestamp = div_header.css("li.meta-date::text").get()
    writer = div_header.css("span.author > a::text").get()
    reading_time = int(div_header.css(
                "li.meta-reading-time::text"
            ).get().split()[0])
    summary = ''.join(
            sel.css("div.entry-content > p:nth-of-type(1) ::text").getall()
        ).strip()
    category = div_header.css("span.label::text").get()

    return {
        "url": url, "title": title, "timestamp": timestamp,
        "writer": writer, "reading_time": reading_time,
        "summary": summary, "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    html_content = fetch(URL)
    updates = scrape_updates(html_content)
    next_page_link = scrape_next_page_link(html_content)

    news = []

    while next_page_link:
        for update in updates:
            if len(news) >= amount:
                break
            news_content = fetch(update)
            news.append(scrape_news(news_content))

        if len(news) < amount:
            html_content = fetch(next_page_link)
            updates = scrape_updates(html_content)
            next_page_link = scrape_next_page_link(html_content)
        else:
            break

    create_news(news)
    return news
