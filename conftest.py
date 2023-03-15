import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_desktop_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 1000
    browser.open('https://github.com')


@pytest.fixture()
def open_mobile_browser():
    browser.config.window_width = 800
    browser.config.window_height = 800
    browser.open('https://github.com')
