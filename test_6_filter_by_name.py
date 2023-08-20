from Pages.CustomersPage import CustomersPage


class TestFilterCustomer:

    def test_filter_customer(self, add_customer):
        menu_page, manager_page = add_customer

        # Listagem do cliente
        manager_page.click_customers()

        # Valida que está na página de listar clientes
        customers_page = CustomersPage(driver=manager_page.driver)

        assert customers_page.is_url_customers_page(), 'Página de listar clientes não encontrada!'

        # Busca Cliente
        customers_page.find_customer('Maria')

        # Valida busca do cliente
        assert customers_page.check_table() == 1, 'Cliente não encontrado'
