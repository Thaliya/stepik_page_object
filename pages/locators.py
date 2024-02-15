from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn")


class BasketPageLocators:
    CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    CART_ITEMS = (By.CLASS_NAME, "basket-items")


# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#     CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

