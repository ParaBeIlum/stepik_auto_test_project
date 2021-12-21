from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Not basket page"

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Products in basket"

    def should_be_present_empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text, "Message is not correct"