import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture(autouse=True)
def login_and_add(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )
    ProductPage(driver).add_first_item_to_cart()

def test_cart_opens(driver):
    CartPage(driver).open_cart()
    assert CartPage(driver).get_title() == "Your Cart"

def test_cart_has_one_item(driver):
    CartPage(driver).open_cart()
    assert CartPage(driver).get_cart_item_count() == 1, "❌ Cart should have 1 item"

def test_remove_item_from_cart(driver):
    CartPage(driver).open_cart()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Remove')]"))
    )
    CartPage(driver).remove_first_item()
    assert CartPage(driver).get_cart_item_count() == 0, "❌ Item not removed"

def test_checkout_button_navigates(driver):
    CartPage(driver).open_cart()
    CartPage(driver).click_checkout()
    assert "checkout-step-one" in driver.current_url, "❌ Checkout did not navigate"