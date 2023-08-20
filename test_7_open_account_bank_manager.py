from Pages.ManagerPage import ManagerPage
from Pages.OpenAccountPage import OpenAccountPage


class TestSortCustomers:
    def test_open_account_bank_manager(self, open_home_page):
        menu_page = open_home_page

        # Faz login em bank manager
        menu_page.open_bank_manager_login()

        manager_page = ManagerPage(driver=menu_page.driver)
        assert manager_page.is_url_manager_page(), "Wrong url manager"

        # Clicar no botão opern account
        manager_page.click_open_account()

        open_page = OpenAccountPage(driver=manager_page.driver)
        assert open_page.is_url_open_account(), "Wrong url open account"

        # Seleciona o customer, currency e clica no botão process
        open_page.select_customer()
        open_page.select_currency()
        open_page.click_button_process()

        assert open_page.check_popup_success(), "Popup did not display"



