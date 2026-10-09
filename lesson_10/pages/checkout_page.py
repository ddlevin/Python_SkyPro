from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """Инициализация страницы оформления заказа.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        """Заполняет форму данными покупателя.

        :param first_name: имя покупателя.
        :type first_name: str
        :param last_name: фамилия покупателя.
        :type last_name: str
        :param postal_code: почтовый индекс.
        :type postal_code: str
        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: CheckoutPage
        """
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        ).send_keys(last_name)
        self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE_INPUT)
        ).send_keys(postal_code)
        return self

    def click_continue(self):
        """Нажимает кнопку Continue для перехода к итоговой сумме.

        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: CheckoutPage
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()
        return self

    def get_total(self):
        """Возвращает текст итоговой суммы заказа.

        :return: текст итоговой суммы (например, "Total: $58.29").
        :rtype: str
        """
        element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return element.text
