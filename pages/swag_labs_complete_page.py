from selenium import webdriver
from locators.page_locators import CompletePageLocators
from pages.basePage import BasePage


class Complete(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = CompletePageLocators

    def click_back_home(self):
        elem = self.driver.find_element(*self.locators.BACK_TO_PRODUCTS)
        elem.click()
