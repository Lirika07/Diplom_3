from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, '/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    USER_NAME_INPUT = (By.XPATH, "//input[@name='name']")