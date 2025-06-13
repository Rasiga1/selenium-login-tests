from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def test_successful_login(driver):
    driver.get("https://berpress.github.io/selenium-login-demo/")
    
    # Поиск элементов с явными ожиданиями
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text'], input[type='password']"))
    )
    # Заполнение полей
    inputs[0].send_keys("admin")
    inputs[1].send_keys("password")
    
    # Ожидание кнопки submit и клик по ней
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button, input[type='submit']"))
    ).click()
    
    # Проверка успешного входа
    assert "Успешно" in driver.page_source or "Success" in driver.page_source

def test_invalid_login(driver):
    driver.get("https://berpress.github.io/selenium-login-demo/")
    
    # Заполнение полей с неправильными данными
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text'], input[type='password']"))
    )
    inputs[0].send_keys("wrong")
    inputs[1].send_keys("wrong")
    
    # Ожидание кнопки submit и тык по ней
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button, input[type='submit']"))
    ).click()
    
    # Проверка ошибки
    assert "Ошибка" in driver.page_source or "Error" in driver.page_source
