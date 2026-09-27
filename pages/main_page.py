import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.header_locators import HeaderLocators


class MainPage(BasePage):
    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Закрытие модального окна кликом по крестику")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Добавление первого ингредиента в корзину через drag-and-drop")
    def add_ingredient_to_basket(self):
        source = self.find_element(MainPageLocators.FIRST_INGREDIENT)
        target = self.find_element(MainPageLocators.BASKET_AREA)
        ActionChains(self.driver).click_and_hold(source).move_to_element(target).pause(0.3).release().perform()

    @allure.step("Получение значения счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        return self.get_text(MainPageLocators.FIRST_INGREDIENT_COUNTER)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Ожидание подтверждения заказа и получение его номера")
    def get_created_order_number(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL_TITLE))
        wait.until(
            lambda d: d.find_element(*MainPageLocators.ORDER_MODAL_NUMBER).text.strip()
            not in ["", "9999"]
        )
        return self.get_text(MainPageLocators.ORDER_MODAL_NUMBER).strip()

    @allure.step("Закрытие модального окна с номером заказа")
    def close_order_modal(self):
        self.close_modal()
        self.wait_until_invisible(MainPageLocators.ORDER_MODAL_TITLE)

    @allure.step("Переход в Ленту Заказов через шапку сайта")
    def go_to_feed(self):
        self.click(HeaderLocators.FEED_BUTTON)

    @allure.step("Переход в Личный Кабинет через шапку сайта")
    def go_to_profile(self):
        self.click(HeaderLocators.PROFILE_BUTTON)