import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urls import Urls
import random
import string


def generate_random_string(length=8):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    user_data = {
        "email": f"{generate_random_string(8)}@yandex.ru",
        "password": generate_random_string(10),
        "name": f"User_{generate_random_string(5)}",
    }
    response = requests.post(Urls.REGISTER_API, json=user_data)
    token = response.json().get("accessToken")

    yield user_data

    if token:
        requests.delete(Urls.USER_API, headers={"Authorization": token})