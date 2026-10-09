from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины интернет-магазина."""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        """Инициализация страницы корзины.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """Нажимает кнопку оформления заказа (Checkout).

        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: CartPage
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        return self
