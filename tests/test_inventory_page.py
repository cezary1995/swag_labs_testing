from pages.swag_labs_inventory_page import InventoryPage
from tests.test_login_page import test_login_page_success
from time import sleep

def test_is_bike_light_added_to_cart(init_driver):
    driver = init_driver
    test_login_page_success(init_driver)
    inventory_page_url = driver.current_url
    page = InventoryPage(driver, inventory_page_url)
    page.add_bike_light_to_cart()
    product = page.check_amount_products_in_cart()
    assert product == "1"


def test_go_to_cart(init_driver):
    driver = init_driver
    test_is_bike_light_added_to_cart(init_driver)
    page = InventoryPage(driver, "https://www.saucedemo.com/inventory.html")
    page.click_cart_icon()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"


# bez sleep'a test nie passuje
def test_logout(init_driver):
    driver = init_driver
    test_login_page_success(init_driver)
    page = InventoryPage(driver, "https://www.saucedemo.com/inventory.html")
    page.click_toggler()
    sleep(0.5)
    page.click_logout()
    assert driver.current_url == "https://www.saucedemo.com/"
