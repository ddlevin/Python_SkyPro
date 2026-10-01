# Проект автоматизации тестирования (Selenium + Pytest + Allure)

Проект содержит тесты для проверки:
- работы медленного калькулятора (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html);
- полного цикла оформления заказа в интернет-магазине SauceDemo (https://www.saucedemo.com/).

## Требования

- Python 3.9+
- Google Chrome (для теста калькулятора)
- Mozilla Firefox (для теста магазина)
- Установленный Selenium

## Установка

1. Клонируйте репозиторий:

   git clone <https://github.com/ddlevin/Python_SkyPro>
   cd <lesson_10>

2. Установите зависимости:

   pip install -r requirements.txt

Содержимое `requirements.txt`:

selenium
pytest
allure-pytest
flake8

## Запуск тестов

Запуск тестов:

pytest --alluredir=allure-results


## Формирование отчёта Allure

После запуска тестов в папке `allure-results` появятся результаты.

С помощью команды откройте отчет:

allure serve allure-results

Команда автоматически сгенерирует отчёт и откроет его в браузере.

## .gitignore

gitignore
__pycache__/
*.py[cod]
venv/
.venv/
allure-results/
allure-report/
.pytest_cache/


## Примечания

- Папки с результатами (`allure-results`) и отчётом (`allure-report`) создаются автоматически и не коммитятся в репозиторий.
- Для корректного запуска теста калькулятора требуется установленный Chrome, для теста магазина — Firefox.