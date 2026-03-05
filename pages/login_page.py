import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(1)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.LOGIN_BTN)
    )
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
        time.sleep(4)  # Give popup time to appear AND be dismissed
        self._kill_popup()
    time.sleep(1)  # Wait after dismissal

    def _kill_popup(self):
        """Try every possible way to dismiss the Chrome password popup"""
        # Method 1: JavaScript click on any visible dialog button
        try:
            self.driver.execute_script("""
                var buttons = document.querySelectorAll('button');
                for(var b of buttons) {
                    if(b.textContent.trim() === 'OK' || b.textContent.trim() === 'Ok') {
                        b.click();
                        break;
                    }
                }
            """)
        except:
            pass

        # Method 2: Send Enter key to dismiss
        try:
            from selenium.webdriver.common.keys import Keys
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.RETURN)
        except:
            pass

        # Method 3: JavaScript to remove any overlay/dialog
        try:
            self.driver.execute_script("""
                var dialogs = document.querySelectorAll('dialog, [role="dialog"], [role="alertdialog"]');
                dialogs.forEach(d => d.remove());
            """)
        except:
            pass

        time.sleep(1)

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ERROR_MSG)
        ).text