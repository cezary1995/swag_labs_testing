from pages.swag_labs_cart_page import CartPage
from tests.test_inventory_page import test_go_to_cart


def test_click_checkout_shopping(init_driver):
    driver = init_driver
    test_go_to_cart(init_driver)
    page = CartPage(driver, "https://www.saucedemo.com/cart.html")
    page.click_checkout_btn()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    