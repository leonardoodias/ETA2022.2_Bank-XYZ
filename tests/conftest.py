import pytest

from Pages.AccountPage import AccountPage
from Pages.AddCustomerPage import AddCustomerPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.ManagerPage import ManagerPage
from Pages.MenuPage import MenuPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="edge", help="Choose browser")


@pytest.fixture
def select_browser(request):
    return request.config.getoption("--browser").lower()


@pytest.fixture
def open_home_page(select_browser):
    menu_page = MenuPage(browser=select_browser)
    yield menu_page
    menu_page.close()


@pytest.fixture
def page_customer_login(open_home_page):
    open_home_page.open_customer_login()
    is_login = CustomerLoginPage(driver=open_home_page.driver)
    yield is_login
    open_home_page.close()


@pytest.fixture
def make_deposit(page_customer_login):
    is_deposit = AccountPage(driver=page_customer_login.driver)
    yield is_deposit
    page_customer_login.close()


@pytest.fixture
def add_customer(open_home_page):
    open_home_page.open_bank_manager_login()
    manager_page = ManagerPage(driver=open_home_page.driver)
    # valida que está na pagína de gerenciamento de cliente
    assert manager_page.is_url_manager_page(), 'Página de gerenciamento não encontrada!'
    # Add cliente
    manager_page.click_add_customer()
    add_customer = AddCustomerPage(driver=manager_page.driver)
    add_customer.fill_first_name('Maria')
    add_customer.fill_last_name('Silva')
    add_customer.fill_post_code('13174-100')
    add_customer.click_add_customer()
    add_customer.check_popup_success()
    yield open_home_page, manager_page


@pytest.fixture
def run_all_browser(all_browser):
    menu_page = MenuPage(browser=all_browser)
    yield menu_page
