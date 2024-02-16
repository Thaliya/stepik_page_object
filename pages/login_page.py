import random
import string
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    _email = None
    _password = None

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        print(current_url)
        assert "login" in current_url, "Expected the login page url to include the 'login' text"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Expected login form to be displayed"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Expected register form to be displayed"

    def register_new_user(self):
        el_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        el_email.send_keys(self._generate_email())
        el_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        new_password = self._generate_password()
        el_password.send_keys(new_password)
        el_repeat = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT)
        el_repeat.send_keys(new_password)
        el_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        el_submit.click()

    def _generate_email(self):
        self._email = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "@" + \
                      ''.join(random.choices(string.ascii_letters + string.digits, k=3)) + ".com"
        return self._email

    def _generate_password(self):
        self._password = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "!"
        return self._password
