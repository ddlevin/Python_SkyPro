from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")

    user1_cookie = {
        "name": "sessionid",
        "value": "NGRkZDA3M2YtNGY2Yy00OTUyLTk4MTQtMzVkNjczMjhiN2Y5",
        "domain": "gitflic.ru",
    }
    driver.add_cookie(user1_cookie)

    driver.refresh()

    driver.get("https://gitflic.ru/user/levindm")

    wait.until(EC.url_contains("/user/levindm"))

    url_user1 = driver.current_url

    driver.delete_all_cookies()

    user2_cookie = {
        "name": "sessionid",
        "value": "MjQyMTNlNmYtOGViMi00ZTQ3LTg5ODAtNGQyODZmODQ2ZjJl",
        "domain": "gitflic.ru",
    }
    driver.add_cookie(user2_cookie)

    driver.refresh()

    driver.get("https://gitflic.ru/user/ddlevin")

    wait.until(EC.url_contains("/user/ddlevin"))

    url_user2 = driver.current_url

    print(f"URL пользователя 1: {url_user1}")
    print(f"URL пользователя 2: {url_user2}")

    assert url_user1 != url_user2, (
        f"URL должны различаться, но оба равны: {url_user1}"
    )

    driver.quit()
