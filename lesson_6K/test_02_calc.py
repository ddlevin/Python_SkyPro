from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='=']"))).click()

    result = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    assert result, "Результат 15 не отобразился"

    driver.quit()
