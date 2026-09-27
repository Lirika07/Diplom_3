import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидание отображения элемента: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание присутствия элемента в DOM: {locator}")
    def find_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def fill(self, locator, text):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверка видимости элемента: {locator}")
    def is_visible(self, locator):
        try:
            return bool(
                self.wait.until(EC.visibility_of_element_located(locator))
            )
        except Exception:
            return False

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскивание элемента {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except Exception:
            pass

        # Нативный эмулятор событий HTML5 Drag and Drop для Firefox
        js_dnd = """
        const source = arguments[0];
        const target = arguments[1];
        const dt = new DataTransfer();
        ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(type => {
            const event = new DragEvent(type, {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            (type === 'dragstart' || type === 'dragend' ? source : target).dispatchEvent(event);
        });
        """
        self.driver.execute_script(js_dnd, source, target)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url