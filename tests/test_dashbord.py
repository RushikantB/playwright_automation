from playwright.sync_api import sync_playwright, Page
from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_dashboard(page):
    login = LoginPage(page)
    dashboard = HomePage(page)

    login.login_test()
    dashboard.verify_dashboard_title()
    dashboard.click_on_admin_tab()
