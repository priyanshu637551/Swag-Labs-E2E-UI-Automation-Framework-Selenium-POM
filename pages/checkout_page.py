from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRM_MSG = (By.CLASS_NAME, "complete-header")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )

    def fill_details(self, first, last, postal):
        self.wait_for_form()
        if first:
            self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        if last:
            self.driver.find_element(*self.LAST_NAME).send_keys(last)
        if postal:
            self.driver.find_element(*self.POSTAL).send_keys(postal)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BTN)
        ).click()

    def get_confirmation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CONFIRM_MSG)
        ).text

    def get_error(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ERROR_MSG)
        ).text