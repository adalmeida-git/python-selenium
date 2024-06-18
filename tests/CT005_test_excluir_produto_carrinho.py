import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC



def test_delete_from_cart(driver):
    #adicionando produto ao carrinho ->14.1-inch Laptop
    driver.find_element(By.CSS_SELECTOR, 'html > body > div:nth-of-type(4) > div:first-of-type > div:nth-of-type(4) > div:nth-of-type(3) > div > div > div:nth-of-type(3) > div:nth-of-type(3) > div > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(2) > input').click()
    time.sleep(5)
    #abrindo página do carrinho
    driver.get('https://demowebshop.tricentis.com/cart')
    #selecionando produto para remover
    driver.find_element(By.NAME, 'removefromcart').click()
    time.sleep(5)
    #clicando no botão -> Update shopping cart
    driver.find_element(By.CSS_SELECTOR, 'html > body > div:nth-of-type(4) > div:first-of-type > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > form > div:first-of-type > div > input:first-of-type').click()
    time.sleep(5)
    #coletando mensagem de carrinho vazio
    success_message = driver.find_element(By.CLASS_NAME, 'order-summary-content')
    success_message.is_displayed()
    assert success_message.text == 'Your Shopping Cart is empty!', "Mensagem de erro incorreta! "
