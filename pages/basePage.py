from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.load_page()

    def load_page(self):
        self.driver.get(self.url)

    def click_btn(self, locator: tuple):
        elem = self.driver.find_element(*locator)
        elem.click()

    def input_and_clear(self, data: str, locator):
        elem = self.driver.find_element(*locator)
        elem.clear()
        elem.send_keys(data)