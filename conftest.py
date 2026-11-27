
import pytest
from playwright.sync_api import (
    sync_playwright,
    Browser,
    BrowserContext,
    Page
)


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


def pytest_addoption(parser):
    parser.addoption(
        "--custom-browser",
        action="store",
        default="chromium",
        help="Browser: chromium, webkit"
    )


@pytest.fixture(scope="session")
def browser_type(playwright, request):
    browser_name = request.config.getoption("--custom-browser").lower()

    if browser_name == "chromium":
        return playwright.chromium
    elif browser_name == "webkit":
        return playwright.webkit
    else:
        raise pytest.UsageError(
            f"Unsupported browser: {browser_name}"
        )


@pytest.fixture(scope="session")
def browser(browser_type):
    browser = browser_type.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def context(browser: Browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()
