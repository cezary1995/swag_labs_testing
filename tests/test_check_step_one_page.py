from pages.swag_labs_check_step_one_page import CheckStepOne
from tests.test_cart_page import test_click_checkout_shopping


def test_fill_the_form(init_driver):
    driver = init_driver
    test_click_checkout_shopping(init_driver)
    page = CheckStepOne(driver, "https://www.saucedemo.com/checkout-step-one.html")
    page.fill_the_form_and_click_continue()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
