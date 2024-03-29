import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.swag_labs_login_page import LoginPage
import json
from os import getenv

from pages.swag_labs_login_page import LoginPage
import pytest
from dotenv import load_dotenv
from definitions import ROOT_DIR


def load_config():
    path = ROOT_DIR / "config.json"
    with open(path, "r") as f:
        json_obj = json.load(f)
        return json_obj

load_dotenv()
BROWSER = getenv("BROWSER")


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


@pytest.fixture
def login_standard_user_fixture(init_driver):
    driver = init_driver
    login_page = LoginPage(driver, "https://www.saucedemo.com/")
    inventory_page = login_page.login_with_standard_user()
    return inventory_page
