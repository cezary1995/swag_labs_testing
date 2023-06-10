from pages.swag_labs_cart_page import CartPage
from pages.swag_labs_inventory_page import InventoryItem


def test_add_to_cart(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    item = InventoryItem(inventory_page.driver, "Sauce Labs Bolt T-Shirt")
    item.add_item_to_cart_by_name()

    x = 10


def test_check_if_bike_light_in_cart(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    inventory_page.add_bike_light_to_cart()
    inventory_page.click_cart_icon()
    product_amount = inventory_page.check_amount_products_in_cart()
    product_name = inventory_page.get_name()
    assert product_amount == "1"
    assert product_name == "Sauce Labs Bike Light"


def test_check_if_all_6_products_in_cart(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    inventory_page.add_everything_to_cart()
    amount = inventory_page.check_amount_products_in_cart()
    assert amount == "6"


def test_check_if_len_cart_list_equal_cart_icon(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url

    inventory_page.add_red_tshirt_to_cart()
    inventory_page.add_jacket_to_cart()
    amount = inventory_page.check_amount_products_in_cart()
    inventory_page.click_cart_icon()

    cart_page = CartPage(inventory_page.driver, base_url + "cart.html")
    len_cart_list = cart_page.get_length_of_cart_list()

    assert str(len_cart_list) == amount
