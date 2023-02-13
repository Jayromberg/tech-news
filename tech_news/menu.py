import sys


# Requisitos 11 e 12
def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )
    option = input()

    if option == 0:
        print("Digite quantas notícias serão buscadas:")
        quantity = input()
    elif option == 1:
        print("Digite o título:")
        title = input()
    elif option == 2:
        print("Digite a data no formato aaaa-mm-dd:")
        date = input()
    elif option == 3:
        print("Digite a categoria:")
        category = input()
    elif option == 4:
        print("")
    elif option == 5:
        print("Encerrando script\n")
        sys.exit()
    else:
        print("Opção inválida", file=sys.stderr)
