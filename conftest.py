import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', 
                    action='store',
                    default='chrome',
                    help="Choose browser: chrome or firefox")

    parser.addoption('--language', 
                    action='store',
                    default='en',
                    help="Set language")

@pytest.fixture(scope='function')
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    if browser_name == "chrome":
        print("Starting Chrome...")
        
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("Starting Firefox...")
        
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")
    yield browser
    print("Closing browser...")
    browser.quit()
