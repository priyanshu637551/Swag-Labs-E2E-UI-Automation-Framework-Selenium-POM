import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url, "❌ Valid login failed"

def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    assert "Epic sadface" in page.get_error_message(), "❌ No error for wrong password"

def test_invalid_username(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wrong_user", "secret_sauce")
    assert "Epic sadface" in page.get_error_message(), "❌ No error for wrong username"

def test_empty_credentials(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", "")
    assert "Username is required" in page.get_error_message(), "❌ No error for empty credentials"

def test_locked_out_user(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.get_error_message(), "❌ No error for locked user"