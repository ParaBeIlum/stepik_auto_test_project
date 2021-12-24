from selenium.webdriver.common.by import By


#class MainPageLocators:

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id='content_inner']/p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")
    EMAIL_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTRATION_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REGISTRATION = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
    STRONG_TEXT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
