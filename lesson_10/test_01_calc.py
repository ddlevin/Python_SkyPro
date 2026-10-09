import allure
from selenium import webdriver
from pages.calc_page import CalculatorPage


@allure.title("Проверка медленного калькулятора")
@allure.description(
    "Тест проверяет работу калькулятора с задержкой 45 секунд: "
    "выполняется операция 7 + 8, ожидается результат 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    """Тест медленного калькулятора с задержкой вычислений."""
    driver = webdriver.Chrome()

    with allure.step("Открыть страницу калькулятора"):
        page = CalculatorPage(driver)
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получить результат с экрана"):
        result = page.get_result("15", timeout=50)

    driver.quit()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15", (
            f"Ожидался результат 15, получен: {result}"
        )
