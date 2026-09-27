import random
import string
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from urls import Urls


def generate_random_string(length=8):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
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