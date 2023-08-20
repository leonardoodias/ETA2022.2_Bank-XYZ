from Pages.AddCustomerPage import AddCustomerPage
from Pages.ManagerPage import ManagerPage


class TestAddCustomer:

    def test_add_customer(self, open_home_page):
        menu_page = open_home_page
        menu_page.open_bank_manager_login()
        manager_page = ManagerPage(driver=menu_page.driver)

        # valida que está na pagína de gerenciamento de cliente
        assert manager_page.is_url_manager_page(), 'Página de gerenciamento não encontrada!'

        # Add cliente
        manager_page.click_add_customer()
        add_customer = AddCustomerPage(driver=manager_page.driver)

        # valida que está na página de add cliente
        assert add_customer.is_url_add_customer(), 'Página de adicionar cliente não encontrada!'

        add_customer.fill_first_name('Maria')
        add_customer.fill_last_name('Silva')
        add_customer.fill_post_code('13174-100')
        add_customer.click_add_customer()

        # Valida adição de cliente com sucesso
        assert add_customer.check_popup_success(), 'Cliente não adicionado!'
