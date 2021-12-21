from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to basket button not presented"

    def should_be_name_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT), "Name of product don't found"

    def should_be_price_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "Product Price not found"

    def should_be_correct_buy_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        message = self.browser.find_element(*ProductPageLocators.STRONG_TEXT_IN_SUCCESS_MESSAGE).text
        assert product_name == message, "Product name not found on message"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Product price and basket price is not equal"
    
    def add_to_cart(self):
        self.should_be_name_of_product()
        self.should_be_price_of_product()
        self.should_be_add_to_cart_button()
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_correct_buy_message()
        self.should_be_correct_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear"