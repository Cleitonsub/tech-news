import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.analyzer.ratings import (
    top_5_categories,
    top_5_news
)

options = {
    "0": lambda: get_tech_news(
        input("Digite quantas notícias serão buscadas:\n")
    ),
    "1": lambda: search_by_title(input("Digite o título:\n")),
    "2": lambda: search_by_date(
        input("Digite a data no formato aaaa-mm-dd:\n")
    ),
    "3": lambda: search_by_tag(input("Digite a tag:\n")),
    "4": lambda: search_by_category(input("Digite a categoria:\n")),
    "5": lambda: top_5_news(),
    "6": lambda: top_5_categories(),
    "7": lambda: sys.stdout.write("Encerrando script\n"),
}


# Requisito 12
def analyzer_menu():
    menu = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    try:
        return options[menu]()
    except (KeyError, ValueError):
        return sys.stderr.write("Opção inválida\n")
