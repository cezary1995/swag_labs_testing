from selenium import webdriver



class BasePage:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.base_url = "https://www.saucedemo.com/"
        if driver.current_url != self.url:
            self.load_page()

    def load_page(self) -> None:
        self.driver.get(self.url)

    def click_btn(self, locator: tuple) -> None:
        elem = self.driver.find_element(*locator)
        elem.click()

    def clear_and_enter_data(self, data: str, locator) -> None:
        elem = self.driver.find_element(*locator)
        elem.clear()
        elem.send_keys(data)

    def get_product_name(self, locator: tuple) -> str:
        elem = self.driver.find_element(*locator)
        name = elem.text
        return name


