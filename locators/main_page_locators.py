from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    BASKET_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num')])[1]")
    MODAL_INGREDIENT_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close') or contains(@class, 'modal__close')]",
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'text_type_digits-large') or contains(@class, 'digits-large')]",
    )
    ORDER_MODAL_TITLE = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")