from pages.swag_labs_login_page import LoginPage
import pytest
from time import sleep
from tests.conftest import load_config

VALID_PWD = load_config()["valid_pwd"]
INVALID_PWD = load_config()["invalid_pwd"]


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


# bez sleep'a test nie passuje
def test_logout(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    inventory_page._click_toggler()
    sleep(0.5)
    inventory_page._click_logout()
    assert inventory_page.driver.current_url == base_url
