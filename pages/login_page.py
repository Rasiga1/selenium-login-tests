from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://berpress.github.io/selenium-login-demo/"
        
    def open(self):
        self.driver.get(self.url)
        
    def enter_credentials(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        
    def get_success_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "success-message"))
        ).text
        
    def get_error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "error-message"))
        ).text