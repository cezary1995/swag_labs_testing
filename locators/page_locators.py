from selenium.webdriver.common.by import By


class NavbarPageLocators:
    TOGGLER = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")


class LoginPageLocators:
    USER_INPUT = (By.ID, "user-name")
    PWD_INPUT = (By.ID, "password")
    CLICK_BTN = (By.NAME, "login-button")
    ERROR_TEXT = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    ERROR_DIV = (By.CLASS_NAME, "error-message-container error")


class InventoryPageLocators:
    BIKE_LIGHT_BUTTON = (By.NAME, "add-to-cart-sauce-labs-bike-light")
    CART = (By.CLASS_NAME, "shopping_cart_badge")
    TOGGLER = (By.ID, "react-burger-menu-btn")
    IMG_ELEMENTS = (By.CLASS_NAME, "inventory_item_img")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")


class CartPageLocators:
    CHECKOUT_BUTTON = (By.NAME, "checkout")


class CheckStepOnePageLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")


class CheckStepTwoPageLocators:
    FINISH = (By.ID, "finish")


class CompletePageLocators:
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")
