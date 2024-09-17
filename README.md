# Saucedemo E2E Test

Этот проект содержит автоматический e2e тест для проверки процесса покупки на сайте saucedemo.com с использованием Playwright и Python.

Требования

    Операционная система: Windows, macOS или Linux
    Python: версия 3.10 или выше

Если у вас не установлен Python, следуйте шагам ниже, чтобы установить его.
Установка Python
Шаги для установки Python на Windows/macOS/Linux:

   1. Перейдите на официальный сайт Python и скачайте последнюю стабильную версию.
   2. Во время установки убедитесь, что выбрали опцию "Add Python to PATH" (Добавить Python в переменные среды).
   3. Проверьте установку, запустив в терминале/командной строке:
```bash
python --version
Должно появиться сообщение с номером версии Python
```
Настройка проекта
Шаг 1: Клонируйте репозиторий

Клонируйте этот репозиторий на свой компьютер:
```bash
git clone https://github.com/KoposOFF/saucedemo.git
cd saucedemo-test
```
Шаг 2: Создайте и активируйте виртуальную среду

Рекомендуется использовать виртуальную среду для управления зависимостями проекта.
Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Для macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
После активации виртуальной среды вы увидите префикс (venv) перед командной строкой.

Шаг 3: Установите зависимости

Установите необходимые библиотеки, перечисленные в requirements.txt:
```bash
pip install -r requirements.txt

Установите браузеры, которые Playwright будет использовать для тестов:
playwright install
```
Шаг 4: Запуск теста

Теперь вы можете запустить e2e тест с помощью следующей команды:
```bash
python test_saucedemo.py
```
Тест выполнит следующие действия:

    Авторизация на сайте с использованием учётных данных:
    Логин: standard_user, Пароль: secret_sauce.
    Добавление товара в корзину.
    Оформление покупки.
    Проверка успешного завершения заказа.
