import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # временно выключаем
    options.add_argument("--window-size=1920,1080")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # <-- добавили ожидание элементов
    yield driver
    driver.quit()
