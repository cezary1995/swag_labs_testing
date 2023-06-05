from selenium import webdriver
from locators.page_locators import LoginPageLocators, InventoryPageLocators
from pages.basePage import BasePage
from pages.swag_labs_inventory_page import InventoryPage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = LoginPageLocators()
        self.inventory_locators = InventoryPageLocators()

    def _input_username_data(self, login):
        self.clear_and_enter_data(login, self.locators.USER_INPUT)

    def _input_password_data(self, password):
        self.clear_and_enter_data(password, self.locators.PWD_INPUT)

    def _click_login_btn(self):
        self.click_btn(self.locators.LOGIN_BTN)

    def login_with_standard_user(self):
        self._input_username_data('standard_user')
        self._input_password_data('secret_sauce')
        self._click_login_btn()
        return InventoryPage(self.driver, self.base_url + "inventory.html")

    def log_user_with_data(self, username, password):
        self._input_username_data(username)
        self._input_password_data(password)
        self._click_login_btn()
