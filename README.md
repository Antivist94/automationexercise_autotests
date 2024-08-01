## Описание проекта
Тестирование сайта он-лайн магазина https://automationexercise.com/

### Инструменты:

<p align="left">
<img align="center" src="" height="30" width="30">
</p>
___

##### Команда для запуска тестов
___
Чтобы запустить тесты, используйте команду:
```
pytest tests/automationexercise_tests.py --browser=${BROWSER_NAME}
```
Где _${BROWSER_NAME}_ — это переменная, указывающая на браузер, в котором будут выполняться тесты в selenoid.
___

### Описание тестов

Тесты разработаны для проверки функциональности интернет-магазина. 
Каждый из тест кейсов имеет аннотацию, которая позволяет использовать Allure для создания наглядных отчетов.
- Тест на авторизацию
- Тест на открытие карточки товара из каталога
- Тест меню с категориями товаров
- Тест отображения товаров по бренду
- Тест добавления товара в корзину по кнопке на карточке товара в каталоге
___
Скриншоты тестов:

___
Скриншоты отчетности в Allure:

___
Скриншоты отчетности в Telegram:

___
Скринкаст одного из тестов:

___