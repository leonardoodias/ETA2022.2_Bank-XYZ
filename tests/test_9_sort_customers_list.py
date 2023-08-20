from Pages.ManagerPage import ManagerPage
from Pages.CustomersPage import CustomersPage


class TestSortCustomersList:

    def test_sort_by_first_name(self, open_home_page):
        menu_page = open_home_page

        # Login em bank manager
        menu_page.open_bank_manager_login()
        manager_page = ManagerPage(driver=menu_page.driver)

        # Clicar no botão customers
        manager_page.click_customers()

        assert manager_page.is_url_manager_page(), 'Manager Page not found'

        customers_page = CustomersPage(menu_page.driver)

        # Ordena os nomes na lista
        customers_page.click_sort_by_first_name()

        assert customers_page.check_order_first_name_dec()
