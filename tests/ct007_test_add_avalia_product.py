
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.home_page import HomePage
from pages.books_page import BooksPage
from pages.ViewBookPage import ViewBookPage
from pages.ReviewPage import ReviewPage

class TestAvaliacaoEWishlistDoProduto:
    URL = 'https://demowebshop.tricentis.com/'
    email = 'mos@cesar.school'
    password = '123456'
    product_name = 'Health Book'
    review_title = 'Teste'
    review_text = 'Bom'

    @pytest.fixture(scope="class")
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        request.cls.driver = self.driver
        yield
        self.driver.quit()

    @pytest.mark.usefixtures("setup")
    def test_adicionar_avaliacao(self):
        driver = self.driver
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        books_page = BooksPage(driver)
        view_book_page = ViewBookPage(driver)
        review_page = ReviewPage(driver)

        home_page.open_login_page()

        login_page.logon(self.email, self.password)

        # Navegar para a página de livros
        home_page.open_books_page()

        # Selecionar o produto "Health Book"
        books_page.select_book(self.product_name)

        # Clicar no link "Add your review"
        view_book_page.open_add_review_link()

        # Preencher o formulário de review
        review_page.add_review(self.review_title, self.review_text, 5)

        # Verificar se a mensagem de sucesso é exibida
        review_page.assert_message_review_added()

        # Verificar se a avaliação submetida aparece na lista de avaliações
        review_page.assert_review_added_on_list(self.review_title, self.review_text)

if __name__ == "__main__":
    pytest.main()
