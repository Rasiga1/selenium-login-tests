from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(driver):
    driver.get("https://berpress.github.io/selenium-login-demo/")
    
    # Более надежный поиск элементов с явными ожиданиями
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text'], input[type='password']"))
    )
    inputs[0].send_keys("admin")
    inputs[1].send_keys("password")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button, input[type='submit']"))
    ).click()
    
    assert "Успешно" in driver.page_source or "Success" in driver.page_source

def test_invalid_login(driver):
    driver.get("https://berpress.github.io/selenium-login-demo/")
    
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text'], input[type='password']"))
    )
    inputs[0].send_keys("wrong")
    inputs[1].send_keys("wrong")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button, input[type='submit']"))
    ).click()
    
    assert "Ошибка" in driver.page_source or "Error" in driver.page_source