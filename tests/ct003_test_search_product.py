import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search_product(driver):
    home_page = HomePage(driver)

    # Pesquisa pelo produto "Black & White Diamond Heart"
    home_page.search_product("Black & White Diamond Heart")

    # Captura de tela após a pesquisa
    driver.save_screenshot('after_search.png')

    search_results_page = SearchResultsPage(driver)
    assert search_results_page.is_product_listed("Black & White Diamond Heart"), \
        "O produto não foi encontrado nos resultados de busca."


if __name__ == "__main__":
    pytest.main()
