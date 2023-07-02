from selenium import webdriver
from locators.page_locators import CartPageLocators
from pages.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)
        self.locators = CartPageLocators

    def click_checkout_btn(self) -> None:
        self.click_btn(self.locators.CHECKOUT_BUTTON)

    def get_length_of_cart_list(self) -> int:
        cart_list = self.driver.find_element(*self.locators.CART_LIST)
        cart_items = cart_list.find_elements(*self.locators.CART_ITEM)
        return len(cart_items)

    def remove_product_from_cart(self, name):
        cart_list = self.driver.find_elements(*self.locators.CART_ITEM)
        for item in cart_list:
            if item.find_element(*self.locators.CART_ITEM_NAME).text == name:
                item.find_element(*self.locators.REMOVE_BTN).click()



