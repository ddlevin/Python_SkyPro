from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для страницы каталога товаров."""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        """Инициализация страницы каталога.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_id):
        """Добавляет товар в корзину по его идентификатору кнопки.

        :param product_id: id кнопки добавления товара
            (например, "add-to-cart-sauce-labs-backpack").
        :type product_id: str
        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: InventoryPage
        """
        locator = (By.ID, product_id)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def go_to_cart(self):
        """Переходит на страницу корзины.

        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: InventoryPage
        """
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        return self
