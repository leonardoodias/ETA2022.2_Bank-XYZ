from Pages.AccountPage import AccountPage
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.TransactionPage import TransactionPage


class TestCleanTransactionHistoryCustomer:

    def test_clean_transaction_history_customer(self, open_home_page):

        # Acessa a pagina principal e clica em de login
        home_page = open_home_page
        home_page.open_customer_login()

        # Seleciona um usuario e faz login
        customersL_page = CustomerLoginPage(open_home_page.driver)
        customersL_page.select_user_deposit()
        customersL_page.click_on_login()

        account_page = AccountPage(open_home_page.driver)
        assert account_page.is_url_account(), 'Wrong url open account'

        # Obtém o saldo antes do depósito
        initial_balance = account_page.get_balance()

        # Faz deposito e saque
        account_page.make_a_deposit(200)
        account_page.make_a_withdraw(10)

        # Aguarda a atualização do saldo após o depósito
        account_page.wait_for_balance_update(initial_balance + float(account_page._value_deposit))

        # Vai para as transações
        account_page.click_transaction_button()

        transaction_page = TransactionPage(account_page.driver)

        assert transaction_page.is_url_list_tx(), 'Wrong url transaction'

        # Verifica as transações esperadas
        expected_transactions = [
            {"amount": "200", "type": "Credit"},
            {"amount": "10", "type": "Debit"}
        ]

        transaction_page.verify_expected_transactions(expected_transactions)

        # Reseta a lista de transações
        transaction_page.click_button_reset_list()

        assert not transaction_page.validate_if_table_contains_transaction(), 'Did not reset the table'
