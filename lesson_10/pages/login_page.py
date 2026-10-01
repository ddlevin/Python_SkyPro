from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """Инициализация страницы авторизации.

        :param driver: экземпляр WebDriver для управления браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает страницу авторизации в браузере.

        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: LoginPage
        """
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        """Выполняет вход в систему с указанными учётными данными.

        :param username: имя пользователя.
        :type username: str
        :param password: пароль пользователя.
        :type password: str
        :return: текущий экземпляр страницы для чейнинга вызовов.
        :rtype: LoginPage
        """
        self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
        return self
