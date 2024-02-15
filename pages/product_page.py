from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):

    def get_product_name(self):
        el_product_name = WebDriverWait(self.browser, 5)\
            .until(ec.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))
        return el_product_name.text

    def get_product_price(self):
        el_product_price = WebDriverWait(self.browser, 5)\
            .until(ec.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE))
        return el_product_price.text

    def should_be_add_to_cart_button(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_CART)

    def should_be_message_product_name(self):
        self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME)

    def should_be_message_product_price(self):
        self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE)

    def add_to_cart(self):
        el_add_to_card = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        el_add_to_card.click()

    def should_message_match_product_name(self, product_name):
        el_message = WebDriverWait(self.browser, 5)\
            .until(ec.visibility_of_element_located(ProductPageLocators.MESSAGE_PRODUCT_NAME))
        assert el_message.text == product_name, \
            f"Expected correct '{product_name}' product to be added to cart but" \
            f" the page returned '{el_message.text}' message"

    def should_message_match_price(self, product_price):
        el_message = WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(
            ProductPageLocators.MESSAGE_PRODUCT_PRICE))
        assert el_message.text == product_price, \
            f"Expected correct '{product_price}' price to be added to cart but" \
            f" the page returned '{el_message.text}' message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
