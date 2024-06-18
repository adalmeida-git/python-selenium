import pytest
from pages.home_page import HomePage
from pages.books_page import BooksPage

def test_books_page(driver):
    home_page = HomePage(driver)
    books_page = BooksPage(driver)

    # Abra a página Books
    home_page.open_books_page()

    # Valide que a página Books foi carregada verificando a presença do dropdown
    assert books_page.get_displayed_items_count() is not None, "A página Books não foi carregada corretamente."

    # Defina a quantidade de itens por página
    books_page.set_displayed_items_count("12")

    # Verifique se a quantidade de itens por página está correta
    displayed_count = books_page.get_displayed_items_count()
    assert displayed_count == "12", f"Esperava 12 itens por página, mas encontrou {displayed_count}."

    # Valide que a quantidade de itens exibida na página corresponde à seleção
    product_count = books_page.get_product_items_count()
    assert product_count <= 12, f"A quantidade de produtos exibida ({product_count}) é maior que o esperado (12)."

if __name__ == "__main__":
    pytest.main()
