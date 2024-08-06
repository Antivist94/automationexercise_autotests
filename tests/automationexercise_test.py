import allure
import pytest
from allure_commons.types import Severity

from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from test_data.data import Brands

login_page = LoginPage()
catalog_page = CatalogPage()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров")
@allure.story("Авторизация на сайте")
def test_login():
    login_page.open_login_page()
    login_page.input_email_address()
    login_page.input_password()
    login_page.submit_log_in_values()
    login_page.check_sing_up_login_button()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров")
@allure.story("Проверка открытия карточки товара из каталога")
def test_catalog_page():
    catalog_page.open_catalog_page()
    catalog_page.open_product_detail()
    catalog_page.check_review_tab_is_show()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров")
@allure.story("Проверка аккордеон меню с категориями товаров")
def test_accordion_menu_of_category():
    catalog_page.open_catalog_page()
    catalog_page.open_woman_category_in_right_menu()
    catalog_page.check_woman_category_is_opened()
    catalog_page.open_men_category_in_right_menu()
    catalog_page.check_men_category_is_opened()
    catalog_page.open_kids_category_in_right_menu()
    catalog_page.check_kids_category_is_opened()


brand = [Brands.POLO, Brands.BABYHUG, Brands.H_and_M]


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров")
@allure.story("Проверка отображения товаров по фильтрам по бренду")
@pytest.mark.parametrize("brand", brand)
def test_brands_menu_by_category(brand):
    catalog_page.open_catalog_page()
    catalog_page.open_list_of_products_by_brand_category(brand)
    catalog_page.check_brand_title(brand)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Каталог товаров")
@allure.story("Проверка добавления товара в корзину по кнопке на карточке товара в каталоге")
def test_add_to_cart():
    catalog_page.open_catalog_page()
    catalog_page.add_product_to_cart_by_order(1)
    catalog_page.check_success_add_at_cart_alert_is_displayed_and_close()
