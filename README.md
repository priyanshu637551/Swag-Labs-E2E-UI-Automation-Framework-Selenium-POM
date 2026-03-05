# 🧪 Swag Labs E2E UI Automation Framework

An end-to-end UI test automation framework built with Python, Selenium WebDriver, and the Page Object Model (POM) design pattern. Tests cover the full user journey of the SauceDemo e-commerce application — from login to checkout.

## 📌 Project Overview

This framework automates browser-based testing of [SauceDemo](https://www.saucedemo.com) — a demo e-commerce platform used by QA professionals worldwide. It validates critical user flows including authentication, product browsing, cart management, and order checkout using industry-standard POM architecture.

## 🗂️ Project Structure
```
qa_selenium_testing/
├── tests/
│   ├── test_login.py        # Login flow & authentication tests
│   ├── test_product.py      # Product page & sorting tests
│   ├── test_cart.py         # Cart management tests
│   └── test_checkout.py     # End-to-end checkout flow tests
├── pages/
│   ├── login_page.py        # Login page object
│   ├── product_page.py      # Product listing page object
│   ├── cart_page.py         # Cart page object
│   └── checkout_page.py     # Checkout page object
├── reports/
│   └── test_report.html     # Auto-generated HTML test report
├── conftest.py              # Shared fixtures & WebDriver setup
└── pytest.ini               # Pytest configuration
```

## 🛠️ Tech Stack

- **Python** — Core test logic
- **Selenium WebDriver** — Browser automation
- **Pytest** — Test framework & HTML reporting
- **WebDriver Manager** — Automatic ChromeDriver management
- **Page Object Model (POM)** — Design pattern for maintainable tests

## ✅ Test Coverage (17 Test Cases)

| Module | Test Cases | What's Covered |
|---|---|---|
| `test_login.py` | 5 | Valid login, invalid password, invalid username, empty credentials, locked user |
| `test_product.py` | 4 | Page load, product count, add to cart, sort by price & name |
| `test_cart.py` | 4 | Cart opens, item count, remove item, checkout navigation |
| `test_checkout.py` | 4 | Empty field validations, full order completion |

## 🚀 How to Run
```bash
# Install dependencies
pip install pytest selenium webdriver-manager pytest-html

# Run all tests with HTML report
pytest -v

# HTML report auto-generated at
reports/test_report.html
```

## 📊 Test Results
```
17 passed in 174s
```

## 🏗️ Architecture — Page Object Model

Each page of the application has a dedicated class encapsulating its locators and actions. Tests import page objects and call their methods — keeping test logic clean and locators maintainable in one place.
```python
# Example — clean test using POM
def test_valid_checkout_completes(driver):
    CheckoutPage(driver).fill_details("John", "Doe", "12345")
    CheckoutPage(driver).click_continue()
    CheckoutPage(driver).click_finish()
    assert CheckoutPage(driver).get_confirmation() == "Thank you for your order!"
```
<img width="1919" height="908" alt="Screenshot 2026-03-05 161542" src="https://github.com/user-attachments/assets/f4eca7f3-727b-45ce-a40a-2607ed6acb8f" />

