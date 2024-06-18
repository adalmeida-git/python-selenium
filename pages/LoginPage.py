from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def logon(self, user, password):
        self._get_email_field().send_keys(user)
        self._get_password_field().send_keys(password)
        self._get_button_login().click()

    def _get_email_field(self):
        return self.driver.find_element(By.ID, 'Email')

    def _get_password_field(self):
        return self.driver.find_element(By.ID, 'Password')

    def _get_button_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input.button-1.login-button')