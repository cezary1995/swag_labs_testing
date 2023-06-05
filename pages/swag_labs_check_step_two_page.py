from selenium import webdriver
from locators.page_locators import CheckStepTwoPageLocators
from pages.basePage import BasePage


class CheckStepTwo(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = CheckStepTwoPageLocators

    def click_finish(self):
        self.click_btn(self.locators.FINISH)
