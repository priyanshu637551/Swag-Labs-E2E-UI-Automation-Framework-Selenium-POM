from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BTNS = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    SORT_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITLE)
        ).text

    def get_item_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ITEMS)
        )
        return len(self.driver.find_elements(*self.ITEMS))

    def add_first_item_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTNS)
        )
        self.driver.find_elements(*self.ADD_TO_CART_BTNS)[0].click()

    def get_cart_badge_count(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_BADGE)
        ).text

    def sort_products(self, value):
        from selenium.webdriver.support.ui import Select
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_value(value)