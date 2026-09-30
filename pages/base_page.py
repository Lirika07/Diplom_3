import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидание отображения элемента")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание присутствия элемента в DOM")
    def find_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов")
    def find_elements(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Клик через JavaScript")
    def click_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Прокрутка к элементу")
    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Ввод текста в поле")
    def fill(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверка видимости элемента")
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    @allure.step("Ожидание исчезновения элемента")
    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения оверлея модалки")
    def wait_overlay_gone(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
                )
            )
        except Exception:
            pass

    @allure.step("Drag and drop")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        try:
            ActionChains(self.driver).click_and_hold(source).move_to_element(
                target
            ).pause(0.5).release().perform()
        except Exception:
            pass
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            ['dragstart', 'drag', 'dragenter', 'dragover', 'drop', 'dragend'].forEach((type) => {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                if (type === 'dragstart' || type === 'drag' || type === 'dragend') {
                    source.dispatchEvent(event);
                } else {
                    target.dispatchEvent(event);
                }
            });
            """,
            source,
            target,
        )

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверка, что URL содержит: {path}")
    def url_contains(self, path):
        return path in self.driver.current_url

    @allure.step("Проверка, что текущий URL равен: {url}")
    def url_is(self, url):
        return self.driver.current_url.rstrip("/") == url.rstrip("/")

    @allure.step("Ожидание URL, содержащего: {path}")
    def wait_for_url_contains(self, path, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: path in driver.current_url
        )

    @allure.step("Ожидание текста элемента")
    def wait_for_text_not_in(self, locator, texts, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text.strip()
            not in texts
        )

    @allure.step("Ожидание условия")
    def wait_for(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)