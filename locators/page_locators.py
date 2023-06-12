from selenium.webdriver.common.by import By


class NavbarPageLocators:
    TOGGLER = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")


class LoginPageLocators:
    USER_INPUT = (By.ID, "user-name")
    PWD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.NAME, "login-button")
    ERROR_TEXT = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    ERROR_DIV = (By.CLASS_NAME, "error-message-container error")


class InventoryPageLocators:
    CART = (By.CLASS_NAME, "shopping_cart_badge")
    TOGGLER = (By.ID, "react-burger-menu-btn")
    IMG_ELEMENTS = (By.CLASS_NAME, "inventory_item_img")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    LIST_OF_PRODUCTS = (By.CLASS_NAME, "inventory_list")
    PRODUCT = (By.CLASS_NAME, 'inventory_item')
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, 'inventory_item_description')
    PRICE_BAR = (By.CLASS_NAME, 'pricebar')
    BTN_ADD_TO_CART = (By.TAG_NAME, 'button')
    SORT_BTN = (By.CLASS_NAME, 'select_container')
    # SORT_ASC_NAME =
    OPTIONS = (By.TAG_NAME, 'option')

    BTN_ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BTN_ADD_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    BTN_ADD_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    BTN_ADD_BABY_CLOTHES = (By.ID, "add-to-cart-sauce-labs-onesie")
    BTN_ADD_TSHIRT_RED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")


class CartPageLocators:
    CHECKOUT_BUTTON = (By.NAME, "checkout")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")


class CheckStepOnePageLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")


class CheckStepTwoPageLocators:
    FINISH = (By.ID, "finish")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_subtotal_label")


class CompletePageLocators:
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")
