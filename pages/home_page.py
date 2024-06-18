from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.laptop_link_locator = (By.LINK_TEXT, "14.1-inch Laptop")
        self.search_box_locator = (By.ID, "small-searchterms")
        self.search_button_locator = (By.CSS_SELECTOR, "input[value='Search']")
        self.books_menu_locator = (By.XPATH, "//ul[@class='top-menu']//a[contains(text(), 'Books')]")
        self.gift_card = (By.XPATH, "(//a[@href='/gift-cards'][contains(.,'Gift Cards')])[1]")
        self.search_suggestion_locator = (
        By.CSS_SELECTOR, ".ui-autocomplete li a")  # Define o localizador para a sugestão de pesquisa
        self.URL = 'https://demowebshop.tricentis.com/'
    def access_page(self):
        self.driver.get(self.URL)
    def click_on_laptop(self):
        laptop_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.laptop_link_locator)
        )
        laptop_link.click()

    def search_product(self, product_name):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(product_name)

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()

    def select_product(self, product_name):
        product_link_locator = (By.LINK_TEXT, product_name)
        product_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(product_link_locator)
        )
        product_link.click()

    def open_books_page(self):
        books_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.books_menu_locator)
        )
        books_menu.click()

    def open_login_page(self):
        self._get_login_link().click()

    def open_wishlist_page(self):
        self._get_wishlist_link().click()

    def books_page(self):
        self.driver.get(self.URL + 'books')

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.item-box')))

    def _get_login_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'ico-login')

    def _get_wishlist_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'ico-wishlist')

    def open_gift_page(self):
        gift_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.gift_card)
        )
        gift_menu.click()