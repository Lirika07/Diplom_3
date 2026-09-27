import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Заполнение email и отправка формы восстановления")
    def recover_password(self, email):
        self.fill(ForgotPasswordLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordLocators.RECOVER_BUTTON)

    @allure.step("Клик по иконке глаза в поле пароля")
    def click_show_password_icon(self):
        self.click(ForgotPasswordLocators.PASSWORD_EYE_ICON)

    @allure.step("Проверка активности поля ввода пароля")
    def is_password_field_active(self):
        return self.is_visible(ForgotPasswordLocators.PASSWORD_FIELD_ACTIVE)