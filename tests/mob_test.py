import pytest
from conftest import browser
from selene import have


def test_mobile(browser_settings_mobile):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_skip_mobile(browser_settings_skip):
    size = browser_settings_skip
    if size == 'desktop':
        pytest.skip('ЭТО МОБИЛЬНЫЙ ТЕСТ')
    browser.element('[class="Button-label"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('[class="auth-form-body mt-3"]').should(have.text('Password'))


@pytest.mark.parametrize('browser_settings', ['mobile'], indirect=True)
def test_param_mobile(browser_settings):
    browser.element('[class="Button-label"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('[class="application-main "]').should(have.text('Password'))
