import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_product_to_cart_and_apply_coupon(driver):
    # Pré-condição: Acessar https://demowebshop.tricentis.com/
    home_page = HomePage(driver)
    home_page.access_page()
    # Passo 1: Selecionar o produto "14.1-inch Laptop" na página inicial
    home_page.select_product("14.1-inch Laptop")

    # Passo 2: Clicar no botão "Add to cart" na página do produto selecionado
    product_page = ProductPage(driver)
    product_page.add_to_cart()

    # Verificar que a mensagem "The product has been added to your shopping cart" é exibida
    assert "The product has been added to your shopping cart" in product_page.get_success_message()

    # Passo 3: Selecionar "shopping cart" na mensagem
    product_page.go_to_shopping_cart()

    # Verificar que a página de Shopping Cart é carregada
    shopping_cart_page = ShoppingCartPage(driver)
    assert shopping_cart_page.is_loaded()

    # Passo 4: Selecionar "Apply coupon"
    shopping_cart_page.apply_coupon("INVALID_COUPON_CODE")

    # Verificar a mensagem de erro
    assert "The coupon code you entered couldn't be applied to your order" in shopping_cart_page.get_error_message()
