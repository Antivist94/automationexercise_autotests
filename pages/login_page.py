from selene import browser, have, command, be

class LoginPage:
    def open_login_page(self):
        browser.open('https://automationexercise.com/login')


    def input_email_address(self, value):
        browser.element('[data-qa="login-email"]').send_keys(value)

    def input_password(self, value):
        browser.element('[data-qa="login-password"]').send_keys(value)

    def submit_log_in_values(self):
        browser.element('[data-qa="login-button"]').click()

    def check_sing_up_login_button(self,value):
        browser.element('.navbar-nav > li:last-child').should(have.text(f'Logged in as f{value}'))

    def sing_up_by_user(self, email, password):
        self.open_login_page()
        self.input_email_address(email)
        self.input_password(password)
        self.submit_log_in_values()
