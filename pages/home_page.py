from playwright.sync_api import sync_playwright, Page
import json


class HomePage():
    def __init__(self, page: Page):
        self.page = page

        self.dashboard_text = page.locator("//h6[text()='Dashboard']")
        self.admin_tab = page.locator("//span[text()='Admin']")

    def verify_dashboard_title(self):
        actual_dashboard_text = self.dashboard_text.text_content()
        print("Header of dasboard :", actual_dashboard_text)
        expected_dashboard_text = "Dashboard"
        if actual_dashboard_text == expected_dashboard_text:
            print("Dashboard Page is displayed: ", actual_dashboard_text)
        else:
            print("Incorrect/Missing Dashboard: ", actual_dashboard_text)

    def click_on_admin_tab(self):
        self.admin_tab.click()
        self.page.wait_for_url("**/admin/viewSystemUsers")
        return self.page.url
