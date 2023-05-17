from pages.swag_labs_check_step_two_page import CheckStepTwo
from tests.test_check_step_one_page import test_fill_the_form


def test_finish_order(init_driver):
    driver = init_driver
    test_fill_the_form(init_driver)
    page = CheckStepTwo(driver, "https://www.saucedemo.com/checkout-step-two.html")
    page.click_finish()
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
