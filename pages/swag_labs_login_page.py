from selenium import webdriver
from locators.page_locators import LoginPageLocators, InventoryPageLocators
from pages.basePage import BasePage
from pages.swag_labs_inventory_page import InventoryPage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = LoginPageLocators()
        self.inventory_locators = InventoryPageLocators()
        self.valid_users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']

    def login_with_credentials(self, user, pwd):
        self._input_username_data(user)
        self._input_password_data(pwd)
        self._click_login_btn()

    def clear_username_input(self):
        elem = self.driver.find_element(*self.locators.USER_INPUT)
        elem.clear()

    def _input_username_data(self, login):
        elem = self.driver.find_element(*self.locators.USER_INPUT)
        elem.send_keys(login)

    def _input_password_data(self, password):
        elem = self.driver.find_element(*self.locators.PWD_INPUT)
        elem.send_keys(password)

    def _click_login_btn(self):
        self.click_btn(self.locators.CLICK_BTN)

    users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']

    def login_with_standard_user(self):
        self._input_username_data('standard_user')
        self._input_password_data('secret_sauce')
        self._click_login_btn()
        return InventoryPage(driver=self.driver, url="https://www.saucedemo.com/inventory.html")

    def login_with_locked_out_user(self):
        self._input_username_data('locked_out_user')
        self._input_password_data('secret_sauce')
        self._click_login_btn()
        error_msg = self.driver.find_element(*self.locators.ERROR_TEXT).text
        return error_msg

    def login_with_problem_user(self):
        self._input_username_data('problem_user')
        self._input_password_data('secret_sauce')
        self._click_login_btn()
        images = self.driver.find_elements(*self.inventory_locators.IMG_ELEMENTS)
        bike_light_img = images[1]
        src_img = bike_light_img.get_attribute("src")
        return src_img

    def login_with_performance_glitch_user(self):
        self._input_username_data('performance_glitch_user')
        self._input_password_data('secret_sauce')
        self._click_login_btn()

    def enter_invalid_data(self, username='', password=''):
        self._input_username_data(username)
        self._input_password_data(password)
        self._click_login_btn()
        error_msg = self.driver.find_element(*self.locators.ERROR_TEXT).text
        return error_msg
