from selenium import webdriver
from locators.page_locators import CheckStepTwoPageLocators


class CheckStepTwo:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.locators = CheckStepTwoPageLocators

    def click_finish(self):
        elem = self.driver.find_element(*self.locators.FINISH)
        elem.click()
