from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_checkout():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    login_page.open().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Петров", "123456")
    checkout_page.click_continue()

    total = checkout_page.get_total()
    driver.quit()

    assert total == "Total: $58.29", (
        f"Итоговая сумма не совпадает. Получено: {total}"
    )
