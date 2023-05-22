from selenium import webdriver
from locators.page_locators import CartPageLocators
from pages.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = CartPageLocators

    def click_checkout_btn(self):
        elem = self.driver.find_element(*self.locators.CHECKOUT_BUTTON)
        elem.click()
