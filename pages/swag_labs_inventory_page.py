from selenium import webdriver
from locators.page_locators import InventoryPageLocators, NavbarPageLocators
from pages.basePage import BasePage
from pages.swag_labs_cart_page import CartPage


class InventoryPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.inventory_locators = InventoryPageLocators
        self.navbar_locators = NavbarPageLocators

    def add_bike_light_to_cart(self):
        elem = self.driver.find_element(*self.inventory_locators.BIKE_LIGHT_BUTTON)
        elem.click()

    def add_element_to_the_cart(self, name: str):
        elem = self.driver.find_element(*self.inventory_locators.BIKE_LIGHT_BUTTON)

    def check_amount_products_in_cart(self):
        elem = self.driver.find_element(*self.inventory_locators.CART)
        value = elem.text
        return value

    def get_product_name_in_cart(self):
        elem = self.driver.find_element(*self.inventory_locators.CART_ITEM)
        value = elem.text
        return value

    def click_cart_icon(self):
        elem = self.driver.find_element(*self.inventory_locators.CART)
        elem.click()

    def click_toggler(self):
        elem = self.driver.find_element(*self.navbar_locators.TOGGLER)
        elem.click()

    def click_logout(self):
        elem = self.driver.find_element(*self.navbar_locators.LOGOUT_BTN)
        elem.click()

    def logout(self):
        self.click_toggler()
        self.click_logout()

    def add_product_to_basket_and_checkout(self):
        self.add_bike_light_to_cart()
        self.click_cart_icon()
        return CartPage(self.driver, "https://www.saucedemo.com/cart.html")


"""jak zdefinowac element koszyka jako artybut klasy? W tym momencie mam 2 x zdefiniowane to samo"""
