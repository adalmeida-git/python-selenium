from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ListPage:
    def __init__(self, driver):
        self.driver = driver

    def assert_viewmode_list_in_url(self):
        assert "viewmode=list" in self.driver.current_url, "View não estpá em Lista"
