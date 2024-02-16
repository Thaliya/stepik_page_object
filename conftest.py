import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: e.g. 'fr' or 'es'")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "user_add_to_basket: mark test to run only on TestUserAddToBasketFromProductPage class tests"
    )
    config.addinivalue_line(
        "markers", "add_to_basket: mark test to run only on TestAddToBasketFromProductPage class tests"
    )
    config.addinivalue_line(
        "markers", "need_review: mark test to run only on tests that need review"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        f_options = webdriver.FirefoxOptions()
        f_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=f_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
