## Описание проекта
Тестирование сайта онлайн магазина https://automationexercise.com/

### Инструменты:

<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/python.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/github.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/selenoid.png" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/allure_pic.jpeg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/jenkins-original.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/pycharm-original.svg" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/selene.png" height="30" width="30">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/giticons/telegram.png" height="30" width="30">
</p>

##### Команда для запуска тестов
___
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
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/Tests.png" height="480" width="750">
</p>

___

Скриншоты отчетности в Allure:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/Allure_2.png" height="480" width="750">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/Jenkins_example_1.png" height="480" width="750">
</p>

___

Скриншоты отчетности в Telegram:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/tg_example.png" height="300" width="250">
</p>

___

Скринкаст одного из тестов:
<p align="left">
<img align="center" src="https://github.com/Antivist94/automationexercise_autotests/blob/main/gitpics/test_example_video.gif" height="350" width="450">
</p>

___