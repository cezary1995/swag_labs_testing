from selenium import webdriver
from locators.page_locators import CompletePageLocators


class Complete:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.locators = CompletePageLocators

    def click_back_home(self):
        elem = self.driver.find_element(*self.locators.BACK_TO_PRODUCTS)
        elem.click()
