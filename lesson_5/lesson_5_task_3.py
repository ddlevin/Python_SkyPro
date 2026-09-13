from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    all_links = driver.find_elements(By.TAG_NAME, "a")

    assert len(all_links) > 0, "На странице нет ссылок"

    print(f"Найдено ссылок: {len(all_links)}")

    for i, link in enumerate(all_links):
        print(f"Ссылка {i}: {link.text} -> {link.get_attribute('href')}")

    first_link = all_links[0]
    first_link.click()

    assert driver.current_url == (
        "https://httpbin.qa-territory.online/links/10/1")

    sleep(2)
    driver.quit()
