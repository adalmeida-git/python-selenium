from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class SelectViewPage:

    def __init__(self, driver):
        self.driver = driver

    def select_List(self):
        wait = WebDriverWait(self.driver, 10)
        combobox = wait.until(EC.presence_of_element_located((By.ID, "products-viewmode")))
        select = Select(combobox)
        select.select_by_visible_text("List")

    