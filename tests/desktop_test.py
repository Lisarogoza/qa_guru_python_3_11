from conftest import browser
from selene import have


def test_github_desktop(open_desktop_browser):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
