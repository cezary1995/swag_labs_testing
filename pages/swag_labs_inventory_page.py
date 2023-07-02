from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from locators.page_locators import InventoryPageLocators, NavbarPageLocators, CartPageLocators
from pages.basePage import BasePage
from time import sleep

SORT_OPTIONS = [
    ('Name (A to Z)', 6),
    ('Name (Z to A)', 6),
    ('Price (low to high)', 6),
    ('Price (high to low)', 6)
]


class InventoryItem:
    def __init__(self, driver, name: str):
        self.driver = driver
        self.name = name
        self.containers = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def add_item_to_cart_by_name(self):
        for item in self.containers:
            if item.find_element(By.CLASS_NAME, "inventory_item_name").text == self.name:
                item.find_element(By.CSS_SELECTOR, '[data-test^="add-to-cart-"]').click()

    def check_if_adding_product_to_cart_is_enable(self):
        for item in self.containers:
            btn_add_to_cart = item.find_element(By.TAG_NAME, 'button')
            return self.is_clickable(btn_add_to_cart)

    def check_if_product_name_is_clickable(self):
        for item in self.containers:
            product_name = item.find_element(By.CLASS_NAME, "inventory_item_name")
            return self.is_clickable(product_name)

    def check_if_product_have_require_elements(self):
        for item in self.containers:
            if item.find_element(By.CLASS_NAME, "inventory_item_name").text == self.name:
                img = item.find_element(By.CLASS_NAME, "inventory_item_img")
                name = item.find_element(By.CLASS_NAME, "inventory_item_name")
                desc = item.find_element(By.CLASS_NAME, "inventory_item_desc")
                pricebar = item.find_element(By.CLASS_NAME, "pricebar")
                price = item.find_element(By.CLASS_NAME, "inventory_item_price")
                btn = item.find_element(By.TAG_NAME, 'button')
                elems = [img, name, desc, pricebar, price, btn]
                bools = [self.is_clickable(elem) for elem in elems]
                return False if False is bools else True

    def click_product_name(self):
        """function click_product_name() doesn't work for img and name element
        I don't know why (StaleElementReferenceException)"""
        for item in self.containers:
            if item.find_element(By.CLASS_NAME, "inventory_item_name").text == self.name:
                item.find_element(By.CLASS_NAME, "inventory_item_img").click()





    @staticmethod
    def is_clickable(element):
        try:
            return element.is_displayed() and element.is_enabled()
        except NoSuchElementException:
            return False


class InventoryPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.inventory_locators = InventoryPageLocators
        self.navbar_locators = NavbarPageLocators

    def check_amount_products_in_cart(self) -> int:
        elem = self.driver.find_element(*self.inventory_locators.CART)
        value = elem.text
        return int(value)

    def get_product_name_in_cart(self) -> str:
        elem = self.driver.find_element(*self.inventory_locators.CART_ITEM)
        value = elem.text
        return value

    def get_name(self) -> str:
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
