import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Клик по карточке заказа")
    def click_order_card(self):
        card = self.find_element(OrderFeedLocators.ORDER_CARD)
        self.scroll_to(card)
        links = card.find_elements(By.TAG_NAME, "a")
        target = links[0] if links else card
        try:
            target.click()
        except Exception:
            self.click_js(target)

    @allure.step("Проверка отображения модального окна заказа")
    def is_order_modal_displayed(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Получение счётчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(text.replace(" ", "").replace(",", ""))

    @allure.step("Получение счётчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(text.replace(" ", "").replace(",", ""))

    @allure.step("Получение номеров заказов 'В работе'")
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [elem.text.strip() for elem in elements]

    @allure.step("Проверка, что номер заказа есть в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        variants = {order_number, order_number.lstrip("0") or "0"}
        if not order_number.startswith("0"):
            variants.add(f"0{order_number}")

        def _check(driver):
            current = set(self.get_orders_in_progress())
            return bool(variants & current)

        self.wait_for(_check, timeout=15)
        current = set(self.get_orders_in_progress())
        return bool(variants & current)

    @allure.step("Ожидание роста счётчика 'за всё время'")
    def wait_total_increased(self, initial):
        self.wait_for(lambda d: self.get_total_orders_count() > initial, timeout=15)
        return self.get_total_orders_count()

    @allure.step("Ожидание роста счётчика 'за сегодня'")
    def wait_today_increased(self, initial):
        self.wait_for(lambda d: self.get_today_orders_count() > initial, timeout=15)
        return self.get_today_orders_count()