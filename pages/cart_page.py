from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.XPATH, "//button[@id='checkout']")
    REMOVE_BTN = (By.XPATH, "//button[contains(text(),'Remove')]")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITLE)
        )

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        ).click()

    def remove_first_item(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REMOVE_BTN)
        ).click()

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text