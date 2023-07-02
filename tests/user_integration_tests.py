from selenium.webdriver.common.by import By

from pages.swag_labs_inventory_page import InventoryItem


# notice: returns that the description and price elements are clickable elements but actually are not.
def test_if_product_is_clickable(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    bike_light = InventoryItem(inventory_page.driver, "Sauce Labs Bolt T-Shirt")
    assert bike_light.check_if_product_name_is_clickable()


def test_if_add_product_to_cart_is_enable(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    bike_light = InventoryItem(inventory_page.driver, "Sauce Labs Bike Light")
    assert bike_light.check_if_adding_product_to_cart_is_enable()


def test_click_product_and_be_redirected(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    backpack = InventoryItem(inventory_page.driver, "Sauce Labs Bolt T-Shirt")
    backpack.click_product_name()


def test_check_if_product_has_require_elements(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    backpack = InventoryItem(inventory_page.driver, "Sauce Labs Bolt T-Shirt")
    assert backpack.check_if_product_have_require_elements()
