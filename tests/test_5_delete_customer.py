from Pages.CustomersPage import CustomersPage


class TestDeleteCustomer:

    def test_delete_customer(self, add_customer):
        menu_page, manager_page = add_customer

        # Listagem de clientes
        manager_page.click_customers()

        # valida que está na página de listar clientes
        customers_page = CustomersPage(driver=manager_page.driver)
        assert customers_page.is_url_customers_page(), 'Página de listar clientes não encontrada!'

        # Busca Cliente
        customers_page.find_customer('Maria')
        customers_page.delete_customer()

        # Valida que cliente foi deletado
        assert customers_page.check_table() == 0, 'Cliente não deletado'
