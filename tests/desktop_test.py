import pytest
from conftest import browser
from selene import have


def test_desktop(browser_settings_desktop):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_skip_desktop(browser_settings_skip):
    size = browser_settings_skip
    if size == 'mobile':
        pytest.skip('ЭТО ДЕСКТОПНЫЙ ТЕСТ')
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-body mt-3"]').should(have.text('Password'))


@pytest.mark.parametrize('browser_settings', ['desktop'], indirect=True)
def test_param_desktop(browser_settings):
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))
