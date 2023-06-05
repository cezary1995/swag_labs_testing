from os import getenv

from pages.swag_labs_login_page import LoginPage
import pytest
from dotenv import load_dotenv

load_dotenv()
VALID_PWD = getenv("VALID_PASSWORD")
INVALID_PWD = getenv("INVALID_PASSWORD")


def test_login_page_success(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    base_url = page.base_url
    page.login_with_standard_user()

    assert driver.current_url == base_url + "inventory.html"


LOGIN_DATA = [
    (["standard_user", VALID_PWD], "https://www.saucedemo.com/inventory.html"),
    (["locked_out_user", VALID_PWD], "https://www.saucedemo.com/"),
    (["problem_user", VALID_PWD], "https://www.saucedemo.com/inventory.html"),
    (["performance_glitch_user", VALID_PWD], "https://www.saucedemo.com/inventory.html"),
    (["standard_user", INVALID_PWD], "https://www.saucedemo.com/"),
]


@pytest.mark.parametrize('login_credentials,expected_url', LOGIN_DATA)
def test_login_cases(init_driver, login_credentials, expected_url):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    user, password = login_credentials

    page.log_user_with_data(username=user, password=password)
    assert driver.current_url == expected_url
