from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.AccountPage import AccountPage
from Pages.TransactionPage import TransactionPage


class TestTransaction:

    def test_transaction_history(self, open_home_page):

        # Abre a página de login e realiza o login
        open_home_page.open_customer_login()

        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)
        login_customer_page.select_user_withdraw()
        login_customer_page.click_on_login()

        # Clica no botão de transação
        account_page = AccountPage(driver=login_customer_page.driver)
        account_page.click_transaction_button()

        # Instancia a página de histórico de transações
        transaction_page = TransactionPage(account_page.driver)

        # Verifica se a URL é a da página de histórico de transações
        assert transaction_page.is_url_list_tx(), 'URL incorreta'

        # Realiza a pesquisa de transação na página de histórico de transações
        expected_transactions = [
            {"amount": "30", "type": "Credit"},
            {"amount": "4", "type": "Debit"}
        ]

        transaction_page.verify_expected_transactions(expected_transactions)

        # Volta da pagina de transações
        transaction_page.go_back()

        # Realiza logout
        account_page.make_a_logout()
