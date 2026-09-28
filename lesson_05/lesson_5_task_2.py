from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    element = driver.find_element(By. NAME, "custname")
    element.send_keys("Дмитрий Левин")
    sleep(2)

    element = driver.find_element(By. XPATH, "//button[text()='Submit order']")
    element.click()
    sleep(1)

    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
