import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test1:
    URL = 'https://demowebshop.tricentis.com/'

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        yield self.driver

    def test_open_home(self, setup):
        driver = setup
        assert driver.current_url == self.URL, "Pagina Não encontrada"


    def test_size_books(self, setup):
        URL_SIZE = 'https://demowebshop.tricentis.com/books?pagesize=4'
        driver = setup
        self.driver.find_element(By.LINK_TEXT,'Books').click()
        self.driver.find_element(By.ID, 'products-pagesize').click()
        self.driver.find_element(By.XPATH, "//option[contains(.,'4')]").is_selected()
        self.driver.find_element(By.XPATH, "//option[contains(.,'4')]").click()
        assert self.driver.current_url == URL_SIZE, 'URL não encontrada!'

    def test_add_carrinho(self, setup):
        URL_CART = 'https://demowebshop.tricentis.com/cart'
        self.driver.find_element(By.LINK_TEXT,'Computers').click()
        self.driver.find_element(By.XPATH,  "//h2[contains(.,'Desktops')]").click()
        self.driver.find_element(By.LINK_TEXT, 'Simple Computer').click()
        self.driver.find_element(By.ID, 'product_attribute_75_5_31_96').click()
        self.driver.find_element(By.ID, 'add-to-cart-button-75').click()
        self.driver.find_element(By.LINK_TEXT, 'Shopping cart').click()
        self.driver.find_element(By.CLASS_NAME, 'cart').is_displayed()
        assert self.driver.current_url == URL_CART, 'Não acessou a pagina de cart'
        self.driver.save_screenshot('../results/PaginaShop.png')

        self.driver.find_element(By.NAME, 'continueshopping').is_displayed()

    def test_pesquisa_produto_pagina_inicial(self, setup):
        self.driver.find_element(By.ID, 'small-searchterms').is_selected()
        self.driver.find_element(By.ID, 'small-searchterms').click()
        time.sleep(5)

        self.driver.find_element(By.ID, 'small-searchterms').send_keys("Black & White Diamond Heart")
        time.sleep(5)

        self.driver.find_element(By.LINK_TEXT,'Search').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//img[@alt='Picture of Black & White Diamond Heart']").is_enabled()



