from pages.swag_labs_inventory_page import InventoryPage
from time import sleep


# bez sleep'a test nie passuje
def test_logout(init_driver, login_standard_user):
    driver = init_driver
    page = InventoryPage(driver, "https://www.saucedemo.com/inventory.html")
    page.click_toggler()
    sleep(0.5)
    page.click_logout()
    assert driver.current_url == "https://www.saucedemo.com/"
