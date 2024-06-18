from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BooksPage:
    def __init__(self, driver):
        self.driver = driver
        self.display_dropdown_locator = (By.ID, "products-pagesize")
        self.product_item_locator = (By.CSS_SELECTOR, ".product-item")

    def open(self):
        self.driver.get('https://demowebshop.tricentis.com/books')

    def get_displayed_items_count(self):
        display_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.display_dropdown_locator)
        )
        select = Select(display_dropdown)
        selected_option = select.first_selected_option
        url_value = selected_option.get_attribute('value')
        # Extract the count from the URL
        count = url_value.split('pagesize=')[-1]
        return count

    def set_displayed_items_count(self, count):
        try:
            display_dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.display_dropdown_locator)
            )
            select = Select(display_dropdown)

            # Debug: Capture a screenshot of the current page
            self.driver.save_screenshot('results/before_selecting_option.png')

            # Debug: Print available options
            options = [option.get_attribute('value') for option in select.options]
            print("Available options:", options)

            # Adjust selection to match URL format
            value_to_select = f"https://demowebshop.tricentis.com/books?pagesize={count}"
            select.select_by_value(value_to_select)

            # Aguarde até que a URL mude para refletir a nova contagem de itens
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(f"pagesize={count}")
            )
        except TimeoutException:
            print("Timeout ao tentar definir a quantidade de itens por página.")
        except NoSuchElementException:
            print(f"Não foi possível localizar a opção com o valor: {value_to_select}")

    def get_product_items_count(self):
        product_items = self.driver.find_elements(*self.product_item_locator)
        return len(product_items)

    def select_book(self, nome):
        self.driver.find_element(By.LINK_TEXT, nome).click()

    def combobox_view(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "products-viewmode")))

    def select_over(self):
        self.driver.find_element(By.XPATH, "//a[contains(.,'Over 50.00')]").click()

    def return_over(self) -> object:
        over = self.driver.find_element(By.XPATH, "//span[contains(.,'51.00')]").text
        assert over == "51.00", "error teste não realizado"
