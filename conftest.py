import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers.data_generator import generate_user_data
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    else:
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )

    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    user_data = generate_user_data()
    response = requests.post(Urls.REGISTER_API, json=user_data)
    token = response.json().get("accessToken")

    yield user_data

    if token:
        requests.delete(Urls.USER_API, headers={"Authorization": token})