from pages.swag_labs_complete_page import Complete
from tests.test_check_step_two_page import test_finish_order


def test_back_home_after_order_complete(init_driver):
    driver = init_driver
    test_finish_order(init_driver)
    page = Complete(driver, "https://www.saucedemo.com/checkout-complete.html")
    page.click_back_home()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
