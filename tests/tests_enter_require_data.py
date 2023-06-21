import pytest

from pages.swag_labs_check_step_one_page import CheckStepOne, INVALID_CLIENT_DATA
from pages.swag_labs_inventory_page import InventoryItem
from pages.swag_labs_cart_page import CartPage


@pytest.mark.parametrize('client_data,exp_btn_msg', INVALID_CLIENT_DATA)
def test_enter_invalid_client_data(login_standard_user_fixture, client_data, exp_btn_msg):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    item = InventoryItem(inventory_page.driver, "Sauce Labs Bike Light")
    item.add_item_to_cart_by_name()

    cart_page = CartPage(inventory_page.driver, base_url + "cart.html")
    cart_page.click_checkout_btn()

    step_one_page = CheckStepOne(cart_page.driver, base_url + "checkout-step-one.html")
    step_one_page.send_form(*client_data)
    error_msg = step_one_page.get_btn_error_value()
    assert error_msg == exp_btn_msg
