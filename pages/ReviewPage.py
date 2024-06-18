from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReviewPage:

    def __init__(self, driver):
        self.driver = driver

    def add_review(self, title, text, rating):
        self._get_title_field().send_keys(title)
        self._get_text_field().send_keys(text)
        self._get_rating_radio(rating).click()
        self._get_submit_button().click()

    def assert_message_review_added(self):
        wait = WebDriverWait(self.driver, 10)
        success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result'))).text
        assert success_message == 'Product review is successfully added.', "Avaliação não enviada!"

    def assert_review_added_on_list(self, review_title, review_text):
        reviews = self._get_review_titles()
        titles = [review.text for review in reviews]

        reviews_texts = self._get_review_texts()
        texts = [review.text for review in reviews_texts]

        assert review_title in titles and review_text in texts, "Avaliação não encontrada"

    def _get_title_field(self):
        return self.driver.find_element(By.ID, 'AddProductReview_Title')

    def _get_text_field(self):
        return self.driver.find_element(By.ID, 'AddProductReview_ReviewText')

    def _get_rating_radio(self, rating):
        return self.driver.find_element(By.ID, 'addproductrating_' + str(rating))

    def _get_submit_button(self):
        return self.driver.find_element(By.NAME, 'add-review')

    def _get_review_titles(self):
        return self.driver.find_elements(By.CLASS_NAME, 'review-title')

    def _get_review_texts(self):
        return self.driver.find_elements(By.CLASS_NAME, 'review-text')