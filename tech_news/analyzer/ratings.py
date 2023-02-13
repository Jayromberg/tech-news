from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news = find_news()
    rank_categories = Counter(map(
        lambda x: x['category'],
        news)
    ).most_common(5)
    sort_category = sorted(rank_categories, key=lambda x: (-x[1], x[0]))
    return [new[0] for new in sort_category]
