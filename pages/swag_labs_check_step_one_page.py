from selenium import webdriver
from locators.page_locators import CheckStepOnePageLocators
from pages.basePage import BasePage


INVALID_CLIENT_DATA = [
    (("", "", ""), "Error: First Name is required"),
    (("", "Dupa", ""), "Error: First Name is required"),
    (("", "", "14-300"), "Error: First Name is required"),
    (("", "Dupa", "14-300"), "Error: First Name is required"),
    (("Czarek", "", ""), "Error: Last Name is required"),
    (("Czarek", "", "14-300"), "Error: Last Name is required"),
    (("Czarek", "Dupa", ""), "Error: Postal Code is required")
]


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

    def send_form(self, first_name, last_name, postal_code):
        self._input_first_name(first_name)
        self._input_last_name(last_name)
        self._input_postal_code(postal_code)
        self._click_continue()

    def get_btn_error_value(self):
        btn_msg = self.driver.find_element(*self.locators.ERROR_BTN)
        text_value = btn_msg.text
        return text_value
