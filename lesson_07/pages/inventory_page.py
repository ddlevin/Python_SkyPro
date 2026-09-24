from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_id):
        locator = (By.ID, product_id)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        return self
