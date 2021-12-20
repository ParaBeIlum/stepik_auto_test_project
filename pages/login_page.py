from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login form is not correct"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form is not correct"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration form is not correct"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration form is not correct"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration form is not correct"