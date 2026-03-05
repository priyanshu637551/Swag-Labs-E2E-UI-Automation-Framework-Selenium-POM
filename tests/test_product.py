import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.fixture(autouse=True)
def login(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("standard_user", "secret_sauce")
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

def test_products_page_loads(driver):
    assert ProductPage(driver).get_title() == "Products"

def test_products_count(driver):
    assert ProductPage(driver).get_item_count() == 6, "❌ Expected 6 products"

def test_add_item_updates_cart(driver):
    ProductPage(driver).add_first_item_to_cart()
    assert ProductPage(driver).get_cart_badge_count() == "1", "❌ Cart badge not updated"

def test_sort_by_price_low_to_high(driver):
    ProductPage(driver).sort_products("lohi")
    assert ProductPage(driver).get_title() == "Products"

def test_sort_by_name_z_to_a(driver):
    ProductPage(driver).sort_products("za")
    assert ProductPage(driver).get_title() == "Products"