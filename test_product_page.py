import time

from .pages.product_page import ProductPage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_cart()
    WebDriverWait(browser, 5).until(ec.alert_is_present())
    page.solve_quiz_and_get_code()
    page.should_message_match_product_name(product_name)
    page.should_message_match_price(product_price)
