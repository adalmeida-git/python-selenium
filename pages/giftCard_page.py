import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class GiftCard:

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, "(//input[contains(@type,'button')])[3]").click()

    def valida_campos(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//label[contains(@for,'RecipientName')]")))
        mensage_name = self.driver.find_element(By.XPATH, "//label[contains(@for,'RecipientName')]").is_displayed()
        has_mensage_name = mensage_name == "Recipient's Name:"


        return mensage_name and has_mensage_name
