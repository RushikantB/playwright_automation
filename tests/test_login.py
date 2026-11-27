from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_login(page):
    login = LoginPage(page)

    login.login_test()
    assert page.title() == "OrangeHRM"
