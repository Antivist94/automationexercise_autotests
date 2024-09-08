import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from utils import attach

DEFAULT_BROWSER = "chrome"


def pytest_addoption(parser):
    parser.addoption('--browser', help = 'Браузер для запуска тестов')


@pytest.fixture(scope = 'session')
def browser_name(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope = "function")
def browser_manager_selenoid(browser_name):
    browser_name = browser_name if browser_name != "" else DEFAULT_BROWSER
    browser.config.base_url = 'https://automationexercise.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    load_dotenv()
    options = Options()
    options.page_load_strategy.page_load_strategy = 'eager'

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": '100',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options = options)

    browser.config.driver = driver

    yield browser

    attach.add_html()
    attach.add_logs()
    attach.add_screenshot()
    attach.add_video_selenoid()

    browser.quit()


@pytest.fixture(scope = "function")
def browser_manager():
    browser.config.base_url = 'https://automationexercise.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    load_dotenv()
    options = Options()
    options.page_load_strategy.page_load_strategy = 'eager'

    yield browser

    attach.add_html()
    attach.add_logs()
    attach.add_screenshot()
    attach.add_video_selenoid()

    browser.quit()
