from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")

    element = driver.find_element(By.LINK_TEXT, "HTML Form")
    element.click()

    assert driver.current_url == (
        "https://httpbin.qa-territory.online/forms/post"
    )
    sleep(2)

    driver.back
    sleep(2)

    assert driver.current_url == "https://httpbin.qa-territory.online"

    driver.quit()
