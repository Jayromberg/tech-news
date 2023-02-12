from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)
    return [(new["title"], new["url"]) for new in response]


# Requisito 8
def search_by_date(date):
    try:
        ISO_date = datetime.strptime(date, "%Y-%m-%d")
        date_str = ISO_date.strftime("%d-%m-%Y")
    except Exception:
        raise ValueError('Data inválida')

    query = {"timestamp": {"$eq": date_str}}
    response = search_news(query)
    return [(new["title"], new["url"]) for new in response]


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    response = search_news(query)
    return [(new["title"], new["url"]) for new in response]
