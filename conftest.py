import pytest
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Registration:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


@pytest.fixture
def get_correct_user_data():
    random_numbers = random.randint(100, 999)
    return Registration(f"Dmitry_simchuk_11_{random_numbers}@gmail.com", "4321qa", "Dmitry")


@pytest.fixture
def get_not_correct_user_data():
    return Registration("Santa@gmail", "12345", "   ")


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
