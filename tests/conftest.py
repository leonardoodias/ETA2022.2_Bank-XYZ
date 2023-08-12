
import pytest

from pages.MenuPage import MenuPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Choose browser")

@pytest.fixture
def select_browser(request):
     return request.config.getoption("--browser").lower()


@pytest.fixture
def setup():
    menu_page = MenuPage(driver='chrome')
    yield menu_page
