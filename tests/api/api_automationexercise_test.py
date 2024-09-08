import json

import allure
import pytest
import requests
from allure_commons.types import Severity

from paths import json_schema_file
from jsonschema import validate


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров_API")
@allure.story("Получение списка товаров - метод productsList")
def test_get_all_product_list(api_base_url):
    with allure.step("Направить GET запрос на productsList"):
        url = api_base_url + '/api/productsList'
        response = requests.get(url)
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить, Json schema ответа"):
        with open(json_schema_file('productList_schema.json')) as file:
            schema = json.loads(file.read())
            validate(body_json, schema)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров_API")
@allure.story("Получение категорий товаров - метод brandsList")
def test_get_brands_list(api_base_url):
    with allure.step("Направить GET запрос на brandsList"):
        url = api_base_url + '/api/brandsList'
        response = requests.get(url)
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить, Json schema ответа"):
        with open(json_schema_file('brandsList_schema.json')) as file:
            schema = json.loads(file.read())
            validate(body_json, schema)


category = ["dress", "saree", "tshirts", "jeans"]


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Поиск товаров_API")
@allure.story("Поиск товара по категорий товаров - метод searchProduct")
@pytest.mark.parametrize("category", category)
def test_search_products(api_base_url, category):
    with allure.step("Направить POST запрос на searchProduct"):
        url = api_base_url + '/api/searchProduct'
        response = requests.post(url, data = {'search_product': f'{category}'})
        body_json = response.json()
        print(body_json)
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить, Json schema ответа"):
        with open(json_schema_file('searchProduct_schema.json')) as file:
            schema = json.loads(file.read())
            validate(body_json, schema)
    with allure.step("Проверить, что категория товара соответствует запросу"):
        for product in body_json['products']:
            assert product['category'][
                       'category'] == f'{category.capitalize()}', f"Категория товара {product['name']} не равна f'{category}'"


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("пользовательские данные_API")
@allure.story("Регистрация нового пользователя - метод createAccount")
def test_create_user_by_api(api_base_url):
    with (allure.step("Направить POST запрос на createAccount")):
        url = api_base_url + '/api/createAccount'
        form_data = {"name": "Test", "email": "test@moil.qu", "password": "12345", "title": "Mr", "birth_date": "12",
                     "birth_month": "11", "birth_year": "2000", "firstname": "John", "lastname": "Doe", "company": "QA",
                     "address1": "Address", "address2": "Second address", "country": "Qanada", "zipcode": "001192",
                     "state": "Test", "city": "New-Testland", "mobile_number": "777999332112"}
        response = requests.post(url, data = form_data)
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить сообщение"):
        assert body_json['message'] == 'User created!'


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("пользовательские данные_API")
@allure.story("Редактирование пользователя - метод updateAccount")
def test_update_user_by_api(api_base_url):
    with (allure.step("Направить PUT запрос на updateAccount")):
        url = api_base_url + '/api/updateAccount'
        form_data = {"name": "Test_new_name", "email": "test@moil.qu", "password": "12345", "title": "Mr",
                     "birth_date": "12",
                     "birth_month": "11", "birth_year": "2000", "firstname": "John", "lastname": "Doe", "company": "QA",
                     "address1": "Address", "address2": "Second address", "country": "Qanada", "zipcode": "001192",
                     "state": "Test", "city": "New-Testland", "mobile_number": "777999332112"}
        response = requests.put(url, data = form_data)
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить сообщение"):
        assert body_json['message'] == 'User updated!'
        print(body_json)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("пользовательские данные_API")
@allure.story("Авторизация новым пользователем - метод verifyLogin")
def test_login_user_by_api(api_base_url):
    with (allure.step("Направить PUT запрос на verifyLogin")):
        url = api_base_url + '/api/verifyLogin'
        form_data = {"email": "test@moil.qu", "password": "12345"}
        response = requests.post(url, data = form_data)
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить сообщение"):
        assert body_json['message'] == 'User exists!'


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("пользовательские данные_API")
@allure.story("Удаление пользователя - метод deleteAccount")
def test_delete_user_by_api(api_base_url):
    with (allure.step("Направить DELETE запрос на deleteAccount")):
        url = api_base_url + '/api/deleteAccount'
        response = requests.delete(url, data = {"email": "test@moil.qu", "password": "12345"})
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить сообщение"):
        assert body_json['message'] == 'Account deleted!'


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("пользовательские данные_API")
@allure.story("(-)Авторизация несущестующим пользователем - метод verifyLogin")
def test_negative_login_deleted_user_by_api(api_base_url):
    with (allure.step("Направить PUT запрос на verifyLogin")):
        url = api_base_url + '/api/verifyLogin'
        form_data = {"email": "test@moil.qu", "password": "12345"}
        response = requests.post(url, data = form_data)
        body_json = response.json()
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить сообщение"):
        assert body_json['message'] == 'User not found!'


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров_API")
@allure.story("(-)Получение списка товаров - запрос productsList с неправильным Методом")
def test_negative_get_all_product_list_with_bad_method(api_base_url):
    with allure.step("Направить POST запрос на productsList"):
        url = api_base_url + '/api/productsList'
        response = requests.post(url)
    with allure.step("Проверить, что статус код == 200"):
        assert response.status_code == 200
    with allure.step("Проверить, сообщение об ошибке"):
        assert response.json()['message'] == 'This request method is not supported.'


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Поиск товаров_API")
@allure.story("(-)Поиск товаров с неправильным запросом - запрос searchProduct без категории")
def test_negative_search_product_without_category(api_base_url):
    with allure.step("Направить POST запрос на searchProduct без указания категории поиска"):
        url = api_base_url + '/api/searchProduct'
        response = requests.post(url, data = {'search_product': None})
    with allure.step("Проверить, сообщение об ошибке"):
        assert response.json()['message'] == 'Bad request, search_product parameter is missing in POST request.'

