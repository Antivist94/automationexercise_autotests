from selene import browser, have, command, be


class CatalogPage:
    def open_catalog_page(self):
        browser.open("https://automationexercise.com/")

    def open_product_detail(self):
        browser.element('a[href="/product_details/2"]').click()

    def check_review_tab_is_show(self):
        browser.element('.shop-details-tab').should(be.present)

    def open_woman_category_in_right_menu(self):
        browser.element('#accordian [href="#Women"]').perform(command.js.scroll_into_view)
        browser.element('#accordian [href="#Women"]').click()

    def check_woman_category_is_opened(self):
        browser.element('div#Women.panel-collapse.in').should(be.present)

    def open_men_category_in_right_menu(self):
        browser.element('#accordian [href="#Men"]').perform(command.js.scroll_into_view)
        browser.element('#accordian [href="#Men"]').click()

    def check_men_category_is_opened(self):
        browser.element('div#Men.panel-collapse.in').should(be.present)

    def open_kids_category_in_right_menu(self):
        browser.element('#accordian [href="#Kids"]').perform(command.js.scroll_into_view)
        browser.element('#accordian [href="#Kids"]').click()

    def check_kids_category_is_opened(self):
        browser.element('div#Kids.panel-collapse.in').should(be.present)

    def open_Polo_brand_by_category(self, brand):
        browser.element(f".brands-name a[href='/brand_products/{brand}']").perform(command.js.scroll_into_view)
        browser.element(f".brands-name a[href='/brand_products/{brand}']").click()

    def check_brand_title(self, brand):
        brand = brand.upper()
        browser.element('.title').should(have.text(f"BRAND - {brand} PRODUCTS"))

    def add_product_to_cart_by_order(self, order):
        element = browser.all('.productinfo.text-center a.add-to-cart').element(order)
        element.perform(command.js.scroll_into_view)
        element.click()

    def check_success_add_at_cart_alert_is_displayed_and_close(self):
        browser.element('#cartModal').should(be.present)
        browser.element('#cartModal .close-modal').click()
