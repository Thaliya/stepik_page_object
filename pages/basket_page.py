from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.CART_MESSAGE), \
                          "Expected empty cart text to be present"

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS), "Expected cart items not to be preset"
