import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.auth_page import AuthPage


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture(scope='function')
def auto_auth(auth_page):
    auth_page.auth("talamanov01@mail.ru", "qwerty123456")
    return auth_page.driver


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://target.my.com/')
    browser.maximize_window()
    yield browser
    browser.close()
    browser.quit()
