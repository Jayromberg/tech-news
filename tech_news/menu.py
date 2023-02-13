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

    options = {
        "0": (get_tech_news, int, "Digite quantas notícias serão buscadas:"),
        "1": (search_by_title, str, "Digite o título:"),
        "2": (search_by_date, str, "Digite a data no formato aaaa-mm-dd:"),
        "3": (search_by_category, str, "Digite a categoria:"),
        "4": (top_5_categories, None, None),
        "5": (None, None, "Encerrando script\n"),
    }

    func, arg_type, input_prompt = options.get(option, (None, None, None))

    if func is None and input_prompt is not None:
        print(input_prompt)
    elif func is None:
        print("Opção inválida", file=sys.stderr)
    elif arg_type:
        print(input_prompt)
        arg = arg_type(input())
        print(func(arg))
    else:
        print(func())
