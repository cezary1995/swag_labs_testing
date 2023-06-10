from selenium import webdriver
from selenium.webdriver.common.by import By

from locators.page_locators import InventoryPageLocators, NavbarPageLocators
from pages.basePage import BasePage


class InventoryItem:
    def __init__(self, driver, name: str):
        self.driver = driver
        self.name = name

    def add_item_to_cart_by_name(self):
        containers = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for item in containers:
            print(item.text)

            if item.text == self.name:
                item.find_element(By.LINK_TEXT, "Add to cart").click()


class InventoryPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.inventory_locators = InventoryPageLocators
        self.navbar_locators = NavbarPageLocators

    def add_backpack_to_cart(self):
        self.click_btn(self.inventory_locators.BTN_ADD_BACKPACK)

    def add_bike_light_to_cart(self):
        self.click_btn(self.inventory_locators.BTN_ADD_BIKE_LIGHT)

    def add_tshirt_to_cart(self):
        self.click_btn(self.inventory_locators.BTN_ADD_TSHIRT)

    def add_jacket_to_cart(self):
        self.click_btn(self.inventory_locators.BTN_ADD_JACKET)

    def add_baby_to_cart(self):
        self.click_btn(self.inventory_locators.BTN_ADD_BABY_CLOTHES)

    def add_red_tshirt_to_cart(self):
        self.click_btn(self.inventory_locators.BTN_ADD_TSHIRT_RED)

    def check_amount_products_in_cart(self):
        elem = self.driver.find_element(*self.inventory_locators.CART)
        value = elem.text
        return value

    def get_product_name_in_cart(self):
        elem = self.driver.find_element(*self.inventory_locators.CART_ITEM)
        value = elem.text
        return value

    def get_name(self):
        name = self.get_product_name(self.inventory_locators.CART_ITEM)
        return name

    def click_cart_icon(self):
        self.click_btn(self.inventory_locators.CART)

    def _click_toggler(self):
        self.click_btn(self.inventory_locators.TOGGLER)

    def _click_logout(self):
        self.click_btn(self.navbar_locators.LOGOUT_BTN)

    def logout(self):
        self._click_toggler()
        self._click_logout()

    def add_all_products_to_cart(self):
        price_bars = self.driver.find_elements(*self.inventory_locators.PRICE_BAR)
        for price_bar in price_bars:
            button = price_bar.find_element(*self.inventory_locators.BTN_ADD_TO_CART)
            button.click()

    def add_everything_to_cart(self) -> None:
        self.add_backpack_to_cart()
        self.add_bike_light_to_cart()
        self.add_tshirt_to_cart()
        self.add_jacket_to_cart()
        self.add_baby_to_cart()
        self.add_red_tshirt_to_cart()

    # def add(self):
    #     list_of_pricebars = []
    #     list_of_items = []
    #     list_of_btns = []
    #     list_products = self.driver.find_element(*self.inventory_locators.LIST_OF_PRODUCTS)
    #     products = list_products.find_elements(*self.inventory_locators.PRODUCT)
    #     for product in products:
    #         item_desc = product.find_element(*self.inventory_locators.PRODUCT_DESCRIPTION)
    #         list_of_items.append(item_desc)
    #
    #     for item in list_of_items:
    #         price_bar = item.find_elements(*self.inventory_locators.PRICE_BAR)
    #         list_of_pricebars.append(price_bar)
    #     return list_of_pricebars
