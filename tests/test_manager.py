import time

from pages.MenuPage import MenuPage


class TestManager:

    def test_open_menu(self):
        menu_page = MenuPage(browser='chrome')
        time.sleep(4)
        menu_page.open_customer_login()
        time.sleep(4)
        menu_page.open_bank_manager_login()
