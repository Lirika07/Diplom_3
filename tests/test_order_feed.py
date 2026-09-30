import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import Urls


@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increments(self, driver, create_user):
        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)
        initial_total = feed_page.get_total_orders_count()

        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        main_page.get_created_order_number()
        main_page.close_order_modal()

        feed_page.open(Urls.ORDER_FEED_URL)
        new_total = feed_page.wait_total_increased(initial_total)
        assert new_total > initial_total

    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increments(self, driver, create_user):
        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)
        initial_today = feed_page.get_today_orders_count()

        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        main_page.get_created_order_number()
        main_page.close_order_modal()

        feed_page.open(Urls.ORDER_FEED_URL)
        new_today = feed_page.wait_today_increased(initial_today)
        assert new_today > initial_today

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_appears_in_progress_list(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        order_num = main_page.get_created_order_number()
        main_page.close_order_modal()

        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)
        assert feed_page.is_order_in_progress(order_num)