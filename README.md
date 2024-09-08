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
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/Appium_pic.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/icons/Android_Studio_pic.svg" height="30" width="30">
</p>

##### Команда для запуска тестов

UI тесты. Параметр _${BROWSER_NAME}_ — браузер, в котором будут выполняться тесты в selenoid.

```
pytest tests/ui/ui_automationexercise_test.py --browser=${BROWSER_NAME}
```

API тесты:

```
pytest tests/api/api_automationexercise_test.py
```

Тесты мобильного приложения BrowserStuck. Для запуска локально, следует указать параметр --context=local_emulator

```
pytest tests/mobile/mobile_git_tutor_test.py --context=bstack 
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
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/mobile_report.png" height="480" width="750">
</p>

___

Скриншоты отчетности в Telegram:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/tg_report.png" height="300" width="250">
</p>

___

Скринкасты тестов:
UI:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/test_example_video.gif" height="350" width="450">
</p>

Mobile:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/resources/mobile_tests.gif" height="350" width="450">
</p>

___