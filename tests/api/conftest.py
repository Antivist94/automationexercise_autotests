import pytest


@pytest.fixture(scope = "function")
def api_base_url():
    return 'https://automationexercise.com/'
