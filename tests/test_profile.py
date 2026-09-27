import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Urls


@allure.epic("Stellar Burgers UI")
@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_go_to_profile_page_success(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.go_to_profile()

        assert main_page.wait.until(
            lambda d: Urls.PROFILE_URL in d.current_url
        )

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history_success(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.open_order_history()

        assert profile_page.wait.until(
            lambda d: Urls.ORDER_HISTORY_URL in d.current_url
        )

    @allure.title("Выход из аккаунта")
    def test_logout_success(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.logout()

        assert profile_page.wait.until(
            lambda d: Urls.LOGIN_URL in d.current_url
        )