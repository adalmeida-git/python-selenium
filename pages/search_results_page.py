from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_titles_locator = (By.CSS_SELECTOR, ".product-title a")

    def get_first_result_title(self):
        first_result = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_titles_locator)
        )
        return first_result.text

    def is_product_listed(self, product_name):
        try:
            product_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{product_name}')]"))
            )
            return True
        except TimeoutException:
            return False