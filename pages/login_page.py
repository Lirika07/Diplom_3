import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import Urls


class LoginPage(BasePage):
    @allure.step("Авторизация пользователем: email={email}")
    def login(self, email, password):
        self.open(Urls.LOGIN_URL)
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_until_invisible(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)