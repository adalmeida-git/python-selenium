import pytest
from selenium import webdriver


from pages.home_page import HomePage
from pages.SelectViewPage import SelectViewPage
from pages.ListPage import ListPage
from pages.books_page import BooksPage

class TestFiltro:
    URL = 'https://demowebshop.tricentis.com/'

    @pytest.fixture(scope="class")
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        request.cls.driver = self.driver
        yield
        self.driver.quit()

    @pytest.mark.usefixtures("setup")
    def test_View_List(self):
        driver = self.driver
        home_page = HomePage(driver)
        select_view_page = SelectViewPage(driver)
        list_page = ListPage(driver)
        books_page = BooksPage(driver)

        # Navegar para a página de livros
        home_page.open_books_page()

        # Esperar o dropdown "View mode" estar presente
        books_page.combobox_view()

        # Selecionar a opção "List"
        select_view_page.select_List()

        # Verificar se a visualização mudou para "List"
        list_page.assert_viewmode_list_in_url()


if __name__ == "__main__":
    pytest.main()
