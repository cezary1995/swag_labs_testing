from selenium import webdriver
from selenium.webdriver.common.by import By

from locators.page_locators import InventoryPageLocators, NavbarPageLocators
from pages.basePage import BasePage
from time import sleep

class InventoryItem:
    def __init__(self, driver, name: str):
        self.driver = driver
        self.name = name

    def add_item_to_cart_by_name(self):
        containers = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in containers:
            if item.find_element(By.CLASS_NAME, "inventory_item_name").text == self.name:
                item.find_element(By.CSS_SELECTOR, '[data-test^="add-to-cart-"]').click()


class InventoryPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.inventory_locators = InventoryPageLocators
        self.navbar_locators = NavbarPageLocators

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
        backpack = InventoryItem(self.driver, 'Sauce Labs Backpack')
        bike_light = InventoryItem(self.driver, 'Sauce Labs Bike Light')
        tshirt = InventoryItem(self.driver, 'Sauce Labs Bolt T-Shirt')
        jacket = InventoryItem(self.driver, 'Sauce Labs Fleece Jacket')
        baby = InventoryItem(self.driver, 'Sauce Labs Onesie')
        red_tshirt = InventoryItem(self.driver, 'Test.allTheThings() T-Shirt (Red)')
        backpack.add_item_to_cart_by_name()
        bike_light.add_item_to_cart_by_name()
        tshirt.add_item_to_cart_by_name()
        jacket.add_item_to_cart_by_name()
        baby.add_item_to_cart_by_name()
        red_tshirt.add_item_to_cart_by_name()

    def sort_products(self, sort_type):
        unfold_sort_btn = self.driver.find_element(*self.inventory_locators.SORT_BTN)
        unfold_sort_btn.click()
        options = unfold_sort_btn.find_elements(*self.inventory_locators.OPTIONS)
        for option in options:
            if option.text == sort_type:
                option.click()

    def get_list_of_sort_types(self):
        unfold_sort_btn = self.driver.find_element(*self.inventory_locators.SORT_BTN)
        unfold_sort_btn.click()
        options = unfold_sort_btn.find_elements(*self.inventory_locators.OPTIONS)
        sort_types = [option.text for option in options]
        return sort_types



    def sort_products2(self):
        unfold_sort_btn = self.driver.find_element(*self.inventory_locators.SORT_BTN)
        unfold_sort_btn.click()


