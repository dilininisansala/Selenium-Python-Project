# utils/browser_setup.py

from selenium import webdriver

def get_browser(browser_name):
    if browser_name == "Chrome":
        options = webdriver.ChromeOptions()
        # Add any specific options for Chrome if needed
        return webdriver.Chrome(options=options)
    elif browser_name == "Firefox":
        options = webdriver.FirefoxOptions()
        # Add any specific options for Firefox if needed
        return webdriver.Firefox(options=options)
    elif browser_name == "Edge":
        options = webdriver.EdgeOptions()
        # Add any specific options for Edge if needed
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported")
