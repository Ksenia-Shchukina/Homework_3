import pytest

from selene import browser

browser.config.base_url = 'https://google.com'


@pytest.fixture(scope="function", autouse=True)
def browser_for_test():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.open('')
    yield
    browser.quit()
