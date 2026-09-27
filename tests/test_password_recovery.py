import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from urls import Urls


@allure.epic("Stellar Burgers UI")
@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_go_to_forgot_password_page_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open(Urls.LOGIN_URL)
        login_page.click_forgot_password()

        assert Urls.FORGOT_PASSWORD_URL in driver.current_url

    @allure.title("Ввод почты и клик по кнопке 'Восстановить' переводит на сброс пароля")
    def test_enter_email_and_click_recover_success(self, driver, create_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open(Urls.FORGOT_PASSWORD_URL)
        forgot_page.recover_password(create_user["email"])

        assert forgot_page.wait.until(
            lambda d: Urls.RESET_PASSWORD_URL in d.current_url
        )

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_icon_makes_field_active(self, driver, create_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open(Urls.FORGOT_PASSWORD_URL)
        forgot_page.recover_password(create_user["email"])

        forgot_page.wait.until(
            lambda d: Urls.RESET_PASSWORD_URL in d.current_url
        )
        forgot_page.click_show_password_icon()

        assert forgot_page.is_password_field_active()