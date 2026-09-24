from selenium import webdriver
from pages.calc_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()

    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result("15", timeout=50)
    driver.quit()

    assert result == "15", f"Ожидался результат 15, получен: {result}"
