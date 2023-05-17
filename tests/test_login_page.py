from pages.swag_labs_login_page import LoginPage


def test_login_page_success(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    page.login_with_standard_user()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_fails_locked_out_user(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.login_with_locked_out_user() == "Epic sadface: Sorry, this user has been locked out."


def test_fails_problem_user(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.login_with_problem_user() == "https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg"


def test_enter_invalid_user(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.enter_invalid_data('invalid_user', 'secret_sauce') == "Epic sadface: Username and password" \
                                                                      " do not match any user in this service"


def test_enter_invalid_password(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.enter_invalid_data('standard_user', 'invalid_password') == "Epic sadface: Username and password" \
                                                                           " do not match any user in this service"


def test_no_enter_username_and_correct_password(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.enter_invalid_data(password='invalid_password') == "Epic sadface: Username is required"


def test_no_enter_password_with_standard_user(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.enter_invalid_data(username='standard_user') == "Epic sadface: Password is required"


def test_empty_username_password(init_driver):
    driver = init_driver
    page = LoginPage(driver, "https://www.saucedemo.com/")
    assert page.enter_invalid_data(password='invalid_password') == "Epic sadface: Username is required"
