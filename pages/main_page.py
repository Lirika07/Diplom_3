import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.header_locators import HeaderLocators


class MainPage(BasePage):

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_LINK)

    @allure.step("Закрытие модального окна крестиком")
    def close_modal(self):
        self.wait_overlay_gone()
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверка, что открыто окно деталей ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_visible(MainPageLocators.MODAL_INGREDIENT_TITLE)

    @allure.step("Проверка, что окно деталей ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        return self.wait_until_invisible(MainPageLocators.MODAL_INGREDIENT_TITLE)

    @allure.step("Добавление ингредиента в корзину")
    def add_ingredient_to_basket(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_LINK,
            MainPageLocators.BASKET_AREA,
        )
        try:
            self.wait_for(
                lambda d: (self.get_ingredient_counter() or "0") not in ["", "0"],
                timeout=5,
            )
        except Exception:
            pass

    @allure.step("Получение счётчика ингредиента")
    def get_ingredient_counter(self):
        try:
            return self.get_text(MainPageLocators.INGREDIENT_COUNTER)
        except Exception:
            return "0"

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.wait_overlay_gone()
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получение номера созданного заказа")
    def get_created_order_number(self):
        self.wait_for(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL_TITLE),
            timeout=30,
        )
        self.wait_for(
            lambda d: d.find_element(*MainPageLocators.ORDER_MODAL_NUMBER)
            .text.strip()
            not in ["", "9999"],
            timeout=30,
        )
        return self.get_text(MainPageLocators.ORDER_MODAL_NUMBER).strip()

    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        self.close_modal()
        self.wait_until_invisible(MainPageLocators.ORDER_MODAL_TITLE)

    @allure.step("Переход в Ленту заказов")
    def go_to_feed(self):
        self.wait_overlay_gone()
        self.click(HeaderLocators.FEED_BUTTON)

    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.wait_overlay_gone()
        self.click(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в Личный кабинет")
    def go_to_profile(self):
        self.wait_overlay_gone()
        self.click(HeaderLocators.PROFILE_BUTTON)