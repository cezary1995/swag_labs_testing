from pages.swag_labs_login_page import LoginPage
from pages.swag_labs_inventory_page import InventoryPage
from pages.swag_labs_cart_page import CartPage
from pages.swag_labs_check_step_one_page import CheckStepOne
from pages.swag_labs_check_step_two_page import CheckStepTwo
from pages.swag_labs_complete_page import Complete


def test_check_if_bike_light_in_cart(init_driver, login_standard_user):
    driver = init_driver

    inventory_page = InventoryPage(driver, "https://www.saucedemo.com/inventory.html")
    inventory_page.add_bike_light_to_cart()
    inventory_page.click_cart_icon()
    product_amount = inventory_page.check_amount_products_in_cart()
    product_name = inventory_page.get_product_name_in_cart()
    assert product_amount == "1"
    assert product_name == "Sauce Labs Bike Light"


def test_end_to_end_success(init_driver, login_standard_user):
    driver = init_driver
    cart_page = CartPage(driver, "https://www.saucedemo.com/cart.html")
    inventory_page = InventoryPage(driver, "https://www.saucedemo.com/inventory.html")
    step_one_page = CheckStepOne(driver, "https://www.saucedemo.com/checkout-step-one.html")
    step_two_page = CheckStepTwo(driver, "https://www.saucedemo.com/checkout-step-two.html")
    complete_page = Complete(driver, "https://www.saucedemo.com/checkout-complete.html")

    inventory_page.add_bike_light_to_cart()
    inventory_page.click_cart_icon()
    cart_page.click_checkout_btn()
    step_one_page.fill_the_form_and_click_continue()
    step_two_page.click_finish()
    complete_page.click_back_home()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
