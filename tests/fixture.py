import pytest
import time
from selenium import webdriver
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


    def test_quanti_prod(self, setup):
        URL_SIZE = 'https://demowebshop.tricentis.com/books?pagesize=4'
        driver = setup
        self.driver.find_element(By.LINK_TEXT,'Books').click()
        self.driver.find_element(By.ID, 'products-pagesize').click()
        self.driver.find_element(By.XPATH, "//option[contains(.,'4')]").is_selected()
        self.driver.find_element(By.XPATH, "//option[contains(.,'4')]").click()

        assert self.driver.current_url == URL_SIZE, 'URL não encontrada!'




