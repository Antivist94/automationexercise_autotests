import allure
from dotenv import load_dotenv
from selene import browser, have, command, be

load_dotenv()


class CatalogPage:
    @allure.step("Открыть страницу Каталога")
    def open_catalog_page(self):
        browser.open("/")
        browser.all('button p').element_by(have.exact_text('Consent')).click()

    @allure.step("Нажать View Product у второй карточки товара")
    def open_product_detail(self):
        browser.all('.choose').second.perform(command.js.scroll_into_view).click()

    @allure.step("Проверить, что открылась карточка товара и отображается блок 'Write Your Review'")
    def check_review_tab_is_show(self):
        browser.element('.shop-details-tab').should(be.present)

    @allure.step("Раскрыть категорию WOMEN")
    def open_woman_category_in_right_menu(self):
        browser.element('#accordian [href="#Women"]').perform(command.js.scroll_into_view).click()

    @allure.step("Проверить, что категория WOMEN раскрылась")
    def check_woman_category_is_opened(self):
        browser.element('#Women.panel-collapse.in').should(be.present)

    @allure.step("Раскрыть категорию MEN")
    def open_men_category_in_right_menu(self):
        browser.element('#accordian [href="#Men"]').perform(command.js.scroll_into_view).click()

    @allure.step("Проверить, что категория MEN раскрылась")
    def check_men_category_is_opened(self):
        browser.element('#Men.panel-collapse.in').should(be.present)

    @allure.step("Раскрыть категорию KIDS")
    def open_kids_category_in_right_menu(self):
        browser.element('#accordian [href="#Kids"]').perform(command.js.scroll_into_view).perform(command.js.click)

    @allure.step("Проверить, что категория KIDS раскрылась")
    def check_kids_category_is_opened(self):
        browser.element('#Kids.panel-collapse.in').should(be.present)

    @allure.step("Выбрать товар бренда {brand}")
    def open_list_of_products_by_brand_category(self, brand):
        browser.element('.brands_products').perform(command.js.scroll_into_view)
        browser.element(f".brands-name a[href='/brand_products/{brand}']").perform(command.js.click)

    @allure.step("Проверить, что отображаются отфильтрованные товары бренда {brand}")
    def check_brand_title(self, brand):
        brand = brand.upper()
        browser.element('.title').should(have.text(f"BRAND - {brand} PRODUCTS"))

    @allure.step("Добавить товар #{order} в корзину нажав на 'Add to cart' в карточке товара")
    def add_product_to_cart_by_order(self, order):
        browser.all('.productinfo.text-center a.add-to-cart').element(order).perform(
            command.js.scroll_into_view).click()

    @allure.step("Проверить, что вышло модальное окно с подтверждением добавления товара в корзину")
    def check_success_add_at_cart_alert_is_displayed_and_close(self):
        browser.element('#cartModal').should(be.present)
        browser.element('#cartModal .close-modal').click()


catalog_page = CatalogPage()
