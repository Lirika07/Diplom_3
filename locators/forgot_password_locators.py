from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PASSWORD_EYE_ICON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")