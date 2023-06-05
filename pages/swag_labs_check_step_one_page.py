from selenium import webdriver
from locators.page_locators import CheckStepOnePageLocators
from pages.basePage import BasePage


class CheckStepOne(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = CheckStepOnePageLocators

    def _input_first_name(self, first_name):
        self.clear_and_enter_data(first_name, self.locators.FIRST_NAME)

    def _input_last_name(self, last_name):
        self.clear_and_enter_data(last_name, self.locators.LAST_NAME)

    def _input_postal_code(self, postal_code):
        self.clear_and_enter_data(postal_code, self.locators.POSTAL_CODE)

    def _click_continue(self):
        self.click_btn(self.locators.CONTINUE)

    def fill_the_form_and_click_continue(self):
        self._input_first_name("Czaro")
        self._input_last_name("rolexy")
        self._input_postal_code("14-300")
        self._click_continue()
