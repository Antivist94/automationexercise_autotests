import os

import allure
from dotenv import load_dotenv
from selene import browser, have, command


class LoginPage:
    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        browser.open('https://automationexercise.com/login')
        browser.all('button p').element_by(have.exact_text('Consent')).click()

    @allure.step("Ввести email")
    def input_email_address(self):
        browser.element('.login-form [type="email"]').click().send_keys(os.getenv('USER_EMAIL'))

    @allure.step("Ввести пароль")
    def input_password(self):
        browser.element('.login-form [type="password"]').click().send_keys(os.getenv('USER_PASSWORD'))

    @allure.step("Нажать Login")
    def submit_log_in_values(self):
        browser.element('.login-form .btn-default').perform(command.js.scroll_into_view).click()

    @allure.step("Проверить, что входи произведён и появилась надпись Logged in as *имя пользователя* в хэддере")
    def check_sing_up_login_button(self):
        browser.element('.navbar-nav > li:last-child').should(have.text(f'Logged in as {os.getenv('USER_NAME')}'))

    @allure.step("Авторизоваться пользователем")
    def sing_up_by_user(self, email, password):
        self.open_login_page()
        self.input_email_address(email)
        self.input_password(password)
        self.submit_log_in_values()
