import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.books_page import BooksPage
from pages.ViewBookPage import ViewBookPage
from pages.WishlistPage import WishlistPage

class TestWishlistDoProduto:
    URL = 'https://demowebshop.tricentis.com/'
    product_name = 'Health Book'

    @pytest.fixture(scope="class")
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        request.cls.driver = self.driver
        yield
        self.driver.quit()

    @pytest.mark.usefixtures("setup")
    def test_lista_desejos(self):
        driver = self.driver
        home_page = HomePage(driver)
        books_page = BooksPage(driver)
        view_book_page = ViewBookPage(driver)
        wishlist_page = WishlistPage(driver)

        # Navegar para a página de livros
        home_page.books_page()

        # Selecionar o produto "Health Book"
        books_page.select_book(self.product_name)

        # Adicionar o produto à lista de desejos
        view_book_page.add_to_wishlist()

        # Esperar e verificar se a mensagem de sucesso é exibida
        view_book_page.assert_wishlist_message_displayed()

        # Navegar para a lista de desejos
        home_page.open_wishlist_page()

        # Verificar se o produto foi adicionado à lista de desejos
        wishlist_page.assert_product_added(self.product_name)

if __name__ == "__main__":
    pytest.main()
