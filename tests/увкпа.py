from selenium.webdriver.common.by import By

def test_successful_login(driver):
    driver.get("https://berpress.github.io/selenium-login-demo/")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    message = driver.find_element(By.ID, "flash").text
    assert "Успешно! Вход выполнен." in message

def test_invalid_login(driver):
    driver.get("https://berpress.github.io/selenium-login-demo/")
    driver.find_element(By.NAME, "username").send_keys("wrong")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    message = driver.find_element(By.ID, "flash").text
    assert "Неверный логин или пароль" in message
