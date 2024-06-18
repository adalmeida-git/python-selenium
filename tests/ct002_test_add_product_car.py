import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_add_to_cart(driver):
    home_page = HomePage(driver)
    home_page.click_on_laptop()

    product_page = ProductPage(driver)
    # Navegue para a página do produto
    product_page.add_to_cart()

    # Verifique se a mensagem de sucesso aparece
    success_message = product_page.get_success_message()
    assert "The product has been added to your shopping cart" in success_message, \
        "A mensagem de sucesso não foi exibida"

if __name__ == "__main__":
    pytest.main()