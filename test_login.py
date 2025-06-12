import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver в PATH
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_credentials("admin", "password")
    assert login_page.get_success_message() == "Успешно! Вход выполнен."

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_credentials("wrong_user", "password")
    assert login_page.get_error_message() == "Ошибка! Неверные данные."

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_credentials("admin", "wrong_pass")
    assert login_page.get_error_message() == "Ошибка! Неверные данные."