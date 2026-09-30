from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]/parent::a")
    FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]/parent::a")
    PROFILE_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")