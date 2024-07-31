import os

import pytest

from pages.login_page import *
from pages.catalog_page import *
from utils.brands import Brands


def test_login():
    page = LoginPage()
    page.open_login_page()
    page.input_email_address(os.getenv('user_email'))
    page.input_password(os.getenv('password'))
    page.submit_log_in_values()
    page.check_sing_up_login_button(os.getenv('user'))


def test_catalog_page(login_user):
    page = CatalogPage()
    page.open_catalog_page()
    page.open_product_detail()
    page.check_review_tab_is_show()


def test_accordion_menu_woman_category(login_user):
    page = CatalogPage()
    page.open_catalog_page()
    page.open_woman_category_in_right_menu()
    page.check_woman_category_is_opened()
    page.open_men_category_in_right_menu()
    page.check_men_category_is_opened()
    page.open_kids_category_in_right_menu()
    page.check_kids_category_is_opened()


brand = [Brands.BIBA, Brands.POLO, Brands.MADAME,
         Brands.BABYHUG, Brands.H_and_M]


@pytest.mark.parametrize("brand", brand)
def test_brands_menu_by_category(brand):
    page = CatalogPage()
    page.open_catalog_page()
    page.open_Polo_brand_by_category(brand)
    page.check_brand_title(brand)


def test_add_to_cart():
    page = CatalogPage()
    page.open_catalog_page()
    page.add_product_to_cart_by_order(1)
    page.check_success_add_at_cart_alert_is_displayed_and_close()
