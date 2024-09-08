import os

import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

from tests.mobile import config
from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default = "bstack",
        help = "Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path = env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope = 'function', autouse = True)
def mobile_management(context):
    options = config.to_driver_options(context = context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options = options)
    browser.config.timeout = 10.0

    yield

    attach.add_screenshot()
    attach.add_xml()
    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        load_dotenv()
        attach.add_video_bstack(session_id, os.getenv('BROWSERSTACK_USER'), os.getenv('BROWSERSTACK_KEY'))