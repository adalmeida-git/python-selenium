from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.apply_coupon_button_locator = (By.ID, "apply-coupon-button")

    def apply_coupon(self):
        apply_coupon_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_coupon_button_locator)
        )
        apply_coupon_button.click()