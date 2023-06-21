from time import sleep

from pages.swag_labs_cart_page import CartPage

from pages.swag_labs_inventory_page import InventoryItem, SORT_OPTIONS
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
def test_check_if_bike_light_in_cart(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    bike_light = InventoryItem(inventory_page.driver, "Sauce Labs Bike Light")
    bike_light.add_item_to_cart_by_name()
    product_amount = inventory_page.check_amount_products_in_cart()
    product_name = bike_light.name
    assert product_amount == 1
    assert product_name == "Sauce Labs Bike Light"


@allure.severity(allure.severity_level.CRITICAL)
def test_check_if_all_6_products_in_cart(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    inventory_page.add_everything_to_cart()
    amount = inventory_page.check_amount_products_in_cart()
    assert amount == 6


@allure.severity(allure.severity_level.BLOCKER)
def test_check_if_len_cart_list_equal_cart_icon(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    tshirt = InventoryItem(inventory_page.driver, 'Sauce Labs Bolt T-Shirt')
    jacket = InventoryItem(inventory_page.driver, 'Sauce Labs Fleece Jacket')
    tshirt.add_item_to_cart_by_name()
    jacket.add_item_to_cart_by_name()
    amount = inventory_page.check_amount_products_in_cart()
    inventory_page.click_cart_icon()

    cart_page = CartPage(inventory_page.driver, base_url + "cart.html")
    len_cart_list = cart_page.get_length_of_cart_list()

    assert len_cart_list == amount


@allure.severity(allure.severity_level.TRIVIAL)
def test_add_and_remove_product(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    jacket = InventoryItem(inventory_page.driver, 'Sauce Labs Fleece Jacket')
    jacket.add_item_to_cart_by_name()
    inventory_page.click_cart_icon()
    amount = inventory_page.check_amount_products_in_cart()

    cart_page = CartPage(inventory_page.driver, base_url + "cart.html")
    cart_page.remove_product_from_cart('Sauce Labs Fleece Jacket')
    len_cart_list = cart_page.get_length_of_cart_list()
    assert len_cart_list == amount - 1


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('types_of_sort,exp_prods_in_cart', SORT_OPTIONS)
def test_sort_products_and_add_everything_to_cart(login_standard_user_fixture, types_of_sort, exp_prods_in_cart):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    sort = types_of_sort
    inventory_page.sort_products(sort_type=sort)
    inventory_page.add_everything_to_cart()
    amount = inventory_page.check_amount_products_in_cart()
    assert amount == exp_prods_in_cart

    cart_page = CartPage(inventory_page.driver, base_url + "cart.html")
    len_cart_list = cart_page.get_length_of_cart_list()
    assert len_cart_list == amount
