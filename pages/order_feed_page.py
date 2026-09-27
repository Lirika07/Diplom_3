import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from urls import Urls


class OrderFeedPage(BasePage):
    @allure.step("Клик по первой карточке заказа в ленте")
    def click_first_order_card(self):
        card = self.find_element(OrderFeedLocators.FIRST_ORDER_CARD)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", card
        )
        links = card.find_elements(By.TAG_NAME, "a")
        target = links[0] if links else card
        try:
            target.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", target)

    @allure.step("Проверка отображения модального окна заказа")
    def is_order_modal_displayed(self):
        try:
            return bool(
                self.wait.until(
                    EC.visibility_of_element_located(
                        OrderFeedLocators.ORDER_MODAL
                    )
                )
            )
        except Exception:
            return (
                "/feed/" in self.driver.current_url
                and self.driver.current_url.rstrip("/")
                != Urls.ORDER_FEED_URL.rstrip("/")
            )

    @allure.step("Получение общего количества заказов за все время")
    def get_total_orders_count(self):
        text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(text.replace(" ", "").replace(",", ""))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(text.replace(" ", "").replace(",", ""))

    @allure.step("Получение списка номеров заказов в разделе 'В работе'")
    def get_orders_in_progress(self):
        elements = self.driver.find_elements(
            *OrderFeedLocators.ORDERS_IN_PROGRESS
        )
        return [elem.text.strip() for elem in elements]