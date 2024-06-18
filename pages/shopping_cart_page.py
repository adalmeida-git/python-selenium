from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.apply_coupon_button_locator = (By.CSS_SELECTOR, "input[name='applydiscountcouponcode']")
        self.coupon_error_message_locator = (By.XPATH, "//div[@class='message']")

    def is_loaded(self):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(self.apply_coupon_button_locator)
        )
        return True

    def apply_coupon(self, coupon_code):
        coupon_input_locator = (By.NAME, "discountcouponcode")
        coupon_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(coupon_input_locator)
        )
        coupon_input.clear()
        coupon_input.send_keys(coupon_code)

        apply_coupon_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_coupon_button_locator)
        )
        apply_coupon_button.click()

    def get_error_message(self):
        coupon_error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.coupon_error_message_locator)
        )
        return coupon_error_message.text


