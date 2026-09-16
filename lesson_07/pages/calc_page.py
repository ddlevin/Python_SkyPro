from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, label):
        locator = (By.XPATH, f"//span[text()='{label}']")
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        button.click()
        return self

    def get_result(self, expected_text, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
        return self.driver.find_element(*self.SCREEN).text
