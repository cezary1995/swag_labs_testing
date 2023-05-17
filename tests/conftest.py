import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import json


def load_config():
    with open(r"C:\Users\czare\PycharmProjects\selenium\config.json", "r") as f:
        json_obj = json.load(f)
        return json_obj


@pytest.fixture
def init_driver():
    config = load_config()
    if config['browser'] == 'chrome':
        chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield chrome_driver
        chrome_driver.quit()
    elif config['browser'] == 'firefox':
        firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        yield firefox_driver
        firefox_driver.quit()
    elif config['browser'] == 'edge':
        edge_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        yield edge_driver
        edge_driver.quit()
    else:
        raise ValueError("Browser isn't supported. Use chrome, firefox or edge instead.")
