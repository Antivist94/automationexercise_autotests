## Описание проекта

Тестирование тренировочного сайта онлайн магазина https://automationexercise.com/.
В проекте используются UI и API тесты.

### Инструменты:

<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/python.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/github.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/selenoid.png" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/allure_pic.jpeg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/jenkins-original.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/pycharm-original.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/selene.png" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/telegram.png" height="30" width="30">
</p>

##### Команда для запуска тестов

UI тесты:

```
pytest tests/ui_automationexercise_test.py --browser=${BROWSER_NAME}
```

Где _${BROWSER_NAME}_ — это переменная, указывающая на браузер, в котором будут выполняться тесты в selenoid.

API тесты:

```
pytest tests/api_automationexercise_test.py
```

___

### Описание тестов

Тесты разработаны для проверки функциональности интернет-магазина.
Каждый из тест кейсов имеет аннотацию, которая позволяет использовать Allure для создания ручных тест-кейсов на основе
автотестов и также удобных отчетов о прохождении тестов.

Проверяемая функциональность:
- Тест на авторизацию
- Тест на открытие карточки товара из каталога
- Тест меню с категориями товаров
- Тест отображения товаров по бренду
- Тест добавления товара в корзину по кнопке на карточке товара в каталоге

___
Скриншоты тестов:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/Tests.png" height="480" width="750">
</p>

___

Скриншоты отчетности в Allure:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/Allure_2.png" height="480" width="750">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/Jenkins_example_1.png" height="480" width="750">
</p>

___

Скриншоты отчетности в Telegram:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/tg_report.png" height="300" width="250">
</p>

___

Скринкаст одного из тестов:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/test_example_video.gif" height="350" width="450">
</p>

___