from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FIRST_ORDER_CARD = (
        By.XPATH,
        "(//li[contains(@class, 'OrderHistory_listItem')])[1]",
    )
    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay')] | //button[contains(@class, 'Modal_modal__close')] | //*[contains(text(), 'остав')]",
    )
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p",
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p",
    )
    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//p[contains(text(), 'В работе:')]/following-sibling::ul//li",
    )