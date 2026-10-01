import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description(
    "Тест проверяет полный сценарий покупки: авторизация, "
    "добавление трёх товаров в корзину, оформление заказа "
    "и проверка итоговой суммы ($58.29)."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_checkout():
    """Тест полного цикла оформления заказа в SauceDemo."""
    driver = webdriver.Firefox()

    with allure.step("Авторизоваться как standard_user"):
        login_page = LoginPage(driver)
        login_page.open().login("standard_user", "secret_sauce")

    with allure.step("Добавить три товара в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(
            "add-to-cart-sauce-labs-backpack"
        )
        inventory_page.add_product_to_cart(
            "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        inventory_page.add_product_to_cart(
            "add-to-cart-sauce-labs-onesie"
        )

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Начать оформление заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнить форму покупателя"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Иван", "Петров", "123456")

    with allure.step("Перейти к итоговой сумме"):
        checkout_page.click_continue()

    with allure.step("Получить итоговую сумму"):
        total = checkout_page.get_total()

    driver.quit()

    with allure.step("Проверить итоговую сумму заказа"):
        assert total == "Total: $58.29", (
            f"Итоговая сумма не совпадает. Получено: {total}"
        )
