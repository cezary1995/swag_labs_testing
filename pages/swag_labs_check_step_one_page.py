from selenium import webdriver
from locators.page_locators import CheckStepOnePageLocators


class CheckStepOne:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.locators = CheckStepOnePageLocators

    def clear_and_input_first_name(self, first_name):
        elem = self.driver.find_element(*self.locators.FIRST_NAME)
        elem.clear()
        elem.send_keys(first_name)

    def clear_and_input_last_name(self, last_name):
        elem = self.driver.find_element(*self.locators.LAST_NAME)
        elem.clear()
        elem.send_keys(last_name)

    def clear_and_input_postal_code(self, postal_code):
        elem = self.driver.find_element(*self.locators.POSTAL_CODE)
        elem.clear()
        elem.send_keys(postal_code)

    def click_continue(self):
        elem = self.driver.find_element(*self.locators.CONTINUE)
        elem.click()

    def fill_the_form_and_click_continue(self):
        self.clear_and_input_first_name("Czaro")
        self.clear_and_input_last_name("rolexy")
        self.clear_and_input_postal_code("14-300")
        self.click_continue()
