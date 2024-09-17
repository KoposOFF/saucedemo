import asyncio
from playwright.async_api import async_playwright

async def test_purchase_saucedemo():
    # Запускаем браузер
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) 
        page = await browser.new_page()

        # Открываем сайт
        await page.goto('https://www.saucedemo.com/')
        await asyncio.sleep(2)

        # Авторизация
        await page.fill('input[id="user-name"]', 'standard_user')
        await page.fill('input[id="password"]', 'secret_sauce')
        await page.click('input[id="login-button"]')
        await asyncio.sleep(2)

        # Добавляем товар в корзину
        await page.click('button[id="add-to-cart-sauce-labs-backpack"]')
        await asyncio.sleep(2)

        # Переходим в корзину
        await page.click('a[class="shopping_cart_link"]')
        await asyncio.sleep(2)

        # Проверяем, что товар добавлен в корзину
        cart_item = await page.text_content('.inventory_item_name')
        assert cart_item == 'Sauce Labs Backpack'
        await asyncio.sleep(2)

        # Переходим к оформлению заказа
        await page.click('button[id="checkout"]')

        # Заполняем информацию о покупателе
        await page.fill('input[id="first-name"]', 'Test')
        await page.fill('input[id="last-name"]', 'User')
        await page.fill('input[id="postal-code"]', '12345')
        await asyncio.sleep(2)

        # Завершаем заказ
        await page.click('input[id="continue"]')
        await page.click('button[id="finish"]')
        await asyncio.sleep(2)

        # Проверяем успешное завершение заказа
        success_message = await page.text_content('h2[class="complete-header"]')
        assert "Спасибо за заказ" in success_message
        await asyncio.sleep(2)

        # Закрываем браузер
        await browser.close()

# Запуск теста
if __name__ == "__main__":
    asyncio.run(test_purchase_saucedemo())
