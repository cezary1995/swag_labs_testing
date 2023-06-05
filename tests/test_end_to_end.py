from pages.swag_labs_check_step_one_page import CheckStepOne
from pages.swag_labs_check_step_two_page import CheckStepTwo
from pages.swag_labs_complete_page import Complete
from pages.swag_labs_cart_page import CartPage


def test_end_to_end_success(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url

    inventory_page.add_everything_to_cart()
    amount = inventory_page.check_amount_products_in_cart()
    assert amount == "6"
    inventory_page.click_cart_icon()

    cart_page = CartPage(inventory_page.driver, base_url + "cart.html")
    cart_page.click_checkout_btn()

    step_one_page = CheckStepOne(cart_page.driver,  base_url + "checkout-step-one.html")
    step_one_page.fill_the_form_and_click_continue()

    step_two_page = CheckStepTwo(step_one_page.driver, base_url + "checkout-step-two.html")
    step_two_page.click_finish()

    complete_page = Complete(step_two_page.driver, base_url + "checkout-complete.html")
    complete_page.click_back_home()

    assert complete_page.driver.current_url == base_url + "inventory.html"
