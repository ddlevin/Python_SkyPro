from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы медленного калькулятора.

    Предоставляет методы для настройки задержки вычислений,
    нажатия кнопок и получения результата с экрана.
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        """Инициализация страницы.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def open(self):
        """Открывает страницу калькулятора в браузере.

        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: CalculatorPage
        """
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        """Устанавливает задержку вычислений в секундах.

        :param seconds: количество секунд задержки.
        :type seconds: int
        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: CalculatorPage
        """
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, label):
        """Нажимает кнопку калькулятора по её текстовой метке.

        :param label: текст на кнопке (например, "7", "+", "=").
        :type label: str
        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: CalculatorPage
        """
        locator = (By.XPATH, f"//span[text()='{label}']")
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()
        return self

    def get_result(self, expected_text, timeout=50):
        """Ожидает появления текста на экране и возвращает его.

        :param expected_text: ожидаемый текст на экране калькулятора.
        :type expected_text: str
        :param timeout: максимальное время ожидания в секундах (
        по умолчанию 50
        ).
        :type timeout: int
        :return: текст, отображаемый на экране калькулятора.
        :rtype: str
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
        return self.driver.find_element(*self.SCREEN).text
