from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not correct"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not correct"
