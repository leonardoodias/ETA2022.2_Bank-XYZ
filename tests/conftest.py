import pytest
from Pages.AccountPage import AccountPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.MenuPage import MenuPage
from Pages.PageObject import PageObject

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Choose browser")

@pytest.fixture
def select_browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture
def open_home_page(select_browser):
    menu_page = MenuPage(browser=select_browser)
    yield menu_page
    menu_page.close()

@pytest.fixture
def page_login(open_home_page):
    open_home_page.open_customer_login()
    is_login = CustomerLoginPage(driver=open_home_page.driver)
    yield is_login
    open_home_page.close()

@pytest.fixture
def make_deposit(page_login):
    is_deposit = AccountPage(driver=page_login.driver)
    yield is_deposit
    page_login.close()
