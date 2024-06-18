from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ViewBookPage:

    def __init__(self, driver):
        self.driver = driver

    def open_add_review_link(self):
        self._get_add_review_link().click()

    def add_to_wishlist(self):
        self._get_add_wishlist_button().click()

    def assert_wishlist_message_displayed(self):
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'bar-notification')))
        assert 'The product has been added to your wishlist' in success_message.text, "Produto não foi adicionado à lista de desejos"

    def _get_add_review_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'Add your review')

    def _get_add_wishlist_button(self):
        return self.driver.find_element(By.ID, 'add-to-wishlist-button-22')
