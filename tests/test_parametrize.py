import pytest

from pages.swag_labs_login_page import LoginPage

TEST_DATA = [([3, 4], 8), ([2, 4], 6), ([40, 2], 42)]


@pytest.mark.parametrize("test_input,expected", TEST_DATA)
def test_eval(test_input, expected):
    assert sum(test_input) == expected


def test_sum_loop():
    for data in TEST_DATA:
        assert sum(data[0]) == data[1]


LOGIN_DATA = [(["standard_user", "secret_sauce"], "https://www.saucedemo.com/inventory.html"),
              (["locked_out_user", "secret_sauce"], "https://www.saucedemo.com/")]


@pytest.mark.parametrize("login_credentials,expected_url", LOGIN_DATA)
def test_login_params(init_driver, login_credentials, expected_url):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    user, pwd = login_credentials

    page.login_with_credentials(user=user, pwd=pwd)
    assert driver.current_url == expected_url