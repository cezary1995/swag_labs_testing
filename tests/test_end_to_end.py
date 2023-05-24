from pages.swag_labs_login_page import LoginPage
from pages.swag_labs_inventory_page import InventoryPage
from pages.swag_labs_cart_page import CartPage
from pages.swag_labs_check_step_one_page import CheckStepOne
from pages.swag_labs_check_step_two_page import CheckStepTwo
from pages.swag_labs_complete_page import Complete


def test_check_if_bike_light_in_cart(login_standard_user):
    inventory_page = login_standard_user
    inventory_page.add_bike_light_to_cart()
    inventory_page.click_cart_icon()
    product_amount = inventory_page.check_amount_products_in_cart()
    product_name = inventory_page.get_product_name_in_cart()
    assert product_amount == "1"
    assert product_name == "Sauce Labs Bike Light"


def test_end_to_end_success(login_standard_user):

    inventory_page = login_standard_user
    cart_page = inventory_page.add_product_to_basket_and_checkout()
    cart_page.click_checkout_btn()

    step_one_page = CheckStepOne(cart_page.driver, "https://www.saucedemo.com/checkout-step-one.html")
    step_one_page.fill_the_form_and_click_continue()

    step_two_page = CheckStepTwo(step_one_page.driver, "https://www.saucedemo.com/checkout-step-two.html")
    step_two_page.click_finish()

    complete_page = Complete(driver, "https://www.saucedemo.com/checkout-complete.html")
    complete_page.click_back_home()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
