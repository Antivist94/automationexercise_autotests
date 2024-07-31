import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from utils import attach
from pages.login_page import LoginPage


#
# def pytest_addoption(parser):
#     parser.addoption('--browser', help = 'Браузер для запуска тестов')
#
#
# @pytest.fixture(scope = 'session')
# def browser_name(request):
#     return request.config.getoption('--browser')
#
#
@pytest.fixture()
def login_user(browser_manager):
    email = os.getenv('user_email')
    password = os.getenv('password')
    if email is None or password is None:
        raise EnvironmentError("Environment variables 'user_email' and 'password' must be set.")

    login_page = LoginPage()

    login_page.sing_up_by_user(email = email, password = password)


@pytest.fixture(scope = "function", autouse = True)
def browser_manager():
    browser.config.window_height = 780
    browser.config.window_width = 1220
    load_dotenv()
    options = Options()
    options.page_load_strategy.page_load_strategy = 'eager'

    # selenoid_capabilities = {
    #     "browserName": browser_name,
    #     "browserVersion": '100',
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }

    # selenoid_login = os.getenv("SELENOID_LOGIN")
    # selenoid_pass = os.getenv("SELENOID_PASS")
    # selenoid_url = os.getenv("SELENOID_URL")
    #
    # options.capabilities.update(selenoid_capabilities)
    # driver = webdriver.Remote(
    #     command_executor = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
    #     options = options)
    #
    # browser.config.driver = driver

    # yield browser
    #
    # attach.add_html(browser)
    # attach.add_logs(browser)
    # attach.add_screenshot(browser)
    # attach.add_video(browser)

    browser.quit()