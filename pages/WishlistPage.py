from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WishlistPage:
    def __init__(self, driver):
        self.driver = driver

    def assert_product_added(self, product_name):
        wait = WebDriverWait(self.driver, 10)
        product_in_wishlist = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
        assert product_in_wishlist is not None, "Produto não encontrado na lista de desejos"