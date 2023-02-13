import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def menu():
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )


# Requisitos 11 e 12
def analyzer_menu():
    menu()
    option = input()

    if option == "0":
        print("Digite quantas notícias serão buscadas:")
        quantity = input()
        a = get_tech_news(int(quantity))
        print(a)
    elif option == "1":
        print("Digite o título:")
        title = input()
        b = search_by_title(title)
        print(b)
    elif option == "2":
        print("Digite a data no formato aaaa-mm-dd:")
        date = input()
        c = search_by_date(date)
        print(c)
    elif option == "3":
        print("Digite a categoria:")
        category = input()
        d = search_by_category(category)
        print(d)
    elif option == "4":
        e = top_5_categories()
        print(e)
    elif option == "5":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)
