from time import sleep


# bez sleep'a test nie passuje
def test_logout(login_standard_user_fixture):
    inventory_page = login_standard_user_fixture
    base_url = inventory_page.base_url
    inventory_page._click_toggler()
    sleep(0.5)
    inventory_page._click_logout()
    assert inventory_page.driver.current_url == base_url
