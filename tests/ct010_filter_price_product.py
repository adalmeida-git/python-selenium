import pytest
from pages.home_page import HomePage
from pages.books_page import BooksPage


def test_price_over(driver):
    home_page = HomePage(driver)
    books_page = BooksPage(driver)
    home_page.open_books_page()
    books_page.select_over()
    books_page.return_over()




if __name__ == "__main__":
    pytest.main()