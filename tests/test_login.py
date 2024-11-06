# tests/test_login.py

import pytest
from utils.browser_setup import get_browser
from pages.login_page import LoginPage

@pytest.fixture
def browser(request):
    # Get the browser name from the command line option
    browser_name = request.config.getoption("--browser")
    driver = get_browser(browser_name)  # This should now work
    yield driver
    driver.quit()

def test_login_valid_credentials(browser):
    login_page = LoginPage(browser)
    browser.get("https://the-internet.herokuapp.com/login") 

    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    assert login_page.is_login_successful(), "Login failed with valid credentials"

