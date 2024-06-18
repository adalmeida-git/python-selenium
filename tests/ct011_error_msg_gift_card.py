import time
import pytest
from pages.giftCard_page import GiftCard
from pages.home_page import HomePage

def test_price_over(driver):
    giftCard = GiftCard(driver)
    home_page = HomePage(driver)
    home_page.open_gift_page()
    giftCard.click_add_to_cart()
    time.sleep(2)
    giftCard.valida_campos()

