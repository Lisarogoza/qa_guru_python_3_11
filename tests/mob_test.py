from conftest import browser
from selene import have


def test_github_mobile(open_mobile_browser):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
