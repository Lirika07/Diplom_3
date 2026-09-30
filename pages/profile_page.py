import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step("Открыть историю заказов")
    def open_order_history(self):
        self.wait_overlay_gone()
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.wait_overlay_gone()
        self.click(ProfilePageLocators.LOGOUT_BUTTON)