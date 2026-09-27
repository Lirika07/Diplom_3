import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from urls import Urls


@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_open_order_details_modal_success(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)
        feed_page.click_first_order_card()

        assert feed_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя из 'Истории заказов' отображаются в 'Ленте заказов'")
    def test_user_orders_displayed_in_feed(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        order_num = main_page.get_created_order_number()
        main_page.close_order_modal()

        main_page.go_to_profile()
        profile_page = ProfilePage(driver)
        profile_page.open_order_history()
        assert profile_page.wait.until(lambda d: order_num in d.page_source)

        main_page.go_to_feed()
        assert main_page.wait.until(lambda d: order_num in d.page_source)

    @allure.title("При создании заказа счётчик 'Выполнено за все время' увеличивается")
    def test_total_orders_counter_increments(self, driver, create_user):
        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)
        initial_total = feed_page.get_total_orders_count()

        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        main_page.get_created_order_number()
        main_page.close_order_modal()

        feed_page.open(Urls.ORDER_FEED_URL)
        feed_page.wait.until(
            lambda d: feed_page.get_total_orders_count() > initial_total
        )
        assert feed_page.get_total_orders_count() > initial_total

    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increments(self, driver, create_user):
        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)
        initial_today = feed_page.get_today_orders_count()

        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        main_page.get_created_order_number()
        main_page.close_order_modal()

        feed_page.open(Urls.ORDER_FEED_URL)
        feed_page.wait.until(
            lambda d: feed_page.get_today_orders_count() > initial_today
        )
        assert feed_page.get_today_orders_count() > initial_today

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_appears_in_progress_list(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        order_num = main_page.get_created_order_number()
        main_page.close_order_modal()

        feed_page = OrderFeedPage(driver)
        feed_page.open(Urls.ORDER_FEED_URL)

        formatted_num = f"0{order_num}" if not order_num.startswith("0") else order_num
        feed_page.wait.until(
            lambda d: order_num in feed_page.get_orders_in_progress()
            or formatted_num in feed_page.get_orders_in_progress()
        )
        in_progress = feed_page.get_orders_in_progress()
        assert (order_num in in_progress) or (formatted_num in in_progress)