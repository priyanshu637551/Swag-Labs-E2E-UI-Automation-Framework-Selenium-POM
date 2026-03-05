import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(autouse=True)
def setup(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    ProductPage(driver).add_first_item_to_cart()
    CartPage(driver).open_cart()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
    )
    CartPage(driver).click_checkout()
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))

def test_empty_first_name_shows_error(driver):
    CheckoutPage(driver).click_continue()
    assert "First Name is required" in CheckoutPage(driver).get_error()

def test_empty_last_name_shows_error(driver):
    CheckoutPage(driver).fill_details("John", "", "")
    CheckoutPage(driver).click_continue()
    assert "Last Name is required" in CheckoutPage(driver).get_error()

def test_empty_postal_shows_error(driver):
    CheckoutPage(driver).fill_details("John", "Doe", "")
    CheckoutPage(driver).click_continue()
    assert "Postal Code is required" in CheckoutPage(driver).get_error()

def test_valid_checkout_completes(driver):
    CheckoutPage(driver).fill_details("John", "Doe", "12345")
    CheckoutPage(driver).click_continue()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    CheckoutPage(driver).click_finish()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert CheckoutPage(driver).get_confirmation() == "Thank you for your order!"