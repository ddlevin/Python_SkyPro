from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        element = wait.until(EC.presence_of_element_located(
            (By.NAME, field_name))
            )
        element.send_keys(value)

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_btn.click()

    zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    zip_color = zip_code.value_of_css_property("border-color")
    assert zip_color == "rgb(245, 194, 199)", f"Zip code цвет: {zip_color}"

    green_fields = ["first-name", "last-name", "address", "e-mail",
                    "phone", "city", "country", "job-position", "company"]

    for field_id in green_fields:
        element = driver.find_element(By.ID, field_id)
        color = element.value_of_css_property("border-color")
        assert color == "rgb(186, 219, 204)", f"{field_id} цвет: {color}"

    driver.quit()
