import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step("Переход в раздел 'История заказов'")
    def open_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик по кнопке 'Выход'")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)