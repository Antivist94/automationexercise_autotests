import allure
from selene import browser, have, command


class LoginPage:
    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        browser.open('https://automationexercise.com/login')
        browser.all('button p').element_by(have.exact_text('Consent')).click()
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout = 10).wait_until(have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    @allure.step("Ввести email {value}")
    def input_email_address(self, value):
        browser.element('[data-qa="login-email"]').send_keys(value)

    @allure.step("Ввести пароль {value}")
    def input_password(self, value):
        browser.element('[data-qa="login-password"]').send_keys(value)

    @allure.step("Нажать Login")
    def submit_log_in_values(self):
        browser.element('[data-qa="login-button"]').click()
    @allure.step("Проверить, что входи произведён и появилась надпись Logged in as {value} в хэддере")
    def check_sing_up_login_button(self, value):
        browser.element('.navbar-nav > li:last-child').should(have.text(f'Logged in as f{value}'))

    @allure.step("Авторизоваться пользователем {email}")
    def sing_up_by_user(self, email, password):
        self.open_login_page()
        self.input_email_address(email)
        self.input_password(password)
        self.submit_log_in_values()
