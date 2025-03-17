import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "126.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }
    options.capabilities.update(capabilities)
    driver = webdriver.Remote(
        command_executor="https://selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
