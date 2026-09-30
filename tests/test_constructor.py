import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import Urls


@allure.epic("Stellar Burgers UI")
@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на 'Конструктор' и 'Лента заказов'")
    def test_navigation_between_constructor_and_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)

        main_page.go_to_feed()
        assert main_page.url_contains("/feed")

        main_page.go_to_constructor()
        assert main_page.url_is(Urls.BASE_URL)

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_open_ingredient_modal_success(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_open()

    @allure.title("Закрытие всплывающего окна ингредиента кликом по крестику")
    def test_close_ingredient_modal_success(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increments(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        initial = int(main_page.get_ingredient_counter() or "0")
        main_page.add_ingredient_to_basket()
        updated = int(main_page.get_ingredient_counter() or "0")
        assert updated > initial

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_create_order_authorized_user_success(self, driver, create_user):
        login_page = LoginPage(driver)
        login_page.login(create_user["email"], create_user["password"])

        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.add_ingredient_to_basket()
        main_page.click_order_button()
        order_number = main_page.get_created_order_number()
        assert order_number.isdigit()