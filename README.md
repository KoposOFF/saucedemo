# Saucedemo E2E Test

Этот проект содержит автоматический e2e тест для проверки процесса покупки на сайте saucedemo.com с использованием Playwright и Python.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/KoposOFF/saucedemo
cd saucedemo-test

2. Установка зависимостей:
pip install -r requirements.txt

3. Установите браузеры Playwright:
playwright install

4. Для запуска теста используйте команду:
python main.py

Тест автоматически откроет браузер, выполнит авторизацию, добавит товар в корзину, оформит покупку и проверит успешное завершение.
