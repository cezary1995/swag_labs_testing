from selenium import webdriver
from locators.page_locators import CartPageLocators


class CartPage:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.locators = CartPageLocators

    def click_checkout_btn(self):
        elem = self.driver.find_element(*self.locators.CHECKOUT_BUTTON)
        elem.click()
