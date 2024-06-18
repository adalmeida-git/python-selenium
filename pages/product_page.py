from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_locator = (By.ID, "add-to-cart-button-31")
        self.success_message_locator = (By.CLASS_NAME, "bar-notification")

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button_locator)
        )
        add_to_cart_button.click()

    def get_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message_locator)
        )
        return success_message.text

    def click_on_add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button_locator)
        )
        add_to_cart_button.click()

    def go_to_shopping_cart(self):
        shopping_cart_link_locator = (By.LINK_TEXT, "shopping cart")
        shopping_cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(shopping_cart_link_locator)
        )
        shopping_cart_link.click()
