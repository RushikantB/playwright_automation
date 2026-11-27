from playwright.sync_api import sync_playwright, Page
from pathlib import Path
import json


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        json_path = Path(__file__).resolve().parent.parent / \
            "config" / "env_config.json"
        with open(json_path, "r") as file:
            self.login_data = json.load(file)

        self.username = page.locator("//input[@name='username']")
        self.password = page.locator(
            "//input[@name='password']")
        self.login_button = page.locator("//button[text()=' Login ']")

    def login_test(self):
        self.page.goto(self.login_data["url"])
        print("Page Title: ", self.page.title())
        self.username.fill(self.login_data["username"])
        self.password.fill(self.login_data["password"])
        self.login_button.click()
        self.page.wait_for_timeout(5000)
        assert self.page.title() == "OrangeHRM"
