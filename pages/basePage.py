from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.load_page()

    def load_page(self):
        self.driver.get(self.url)
