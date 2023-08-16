import pdb
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.AccountPage import AccountPage
from Pages.ListTxPage import ListTxPage

class TestTransaction:

    def test_transaction_history(self, open_home_page):
        # Abre a página de login e realiza o login
        open_home_page.click_btn_customer_login()
        print("Clicou no botão Login do cliente")

        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)
        login_customer_page.select_user_withdraw(login_customer_page.user_name_withdraw)
        login_customer_page.click_on_login()
        print("Selecionou cliente e clicou no botão login")

        # # Clica no botão de transação
        account_page = AccountPage(driver=login_customer_page.driver)
        account_page.click_transaction_button()
        print("Clicou no botão de transação")

        # pdb.set_trace()  # Isso inicia o depurador

        # Instancia a página de histórico de transações
        list_tx_page = ListTxPage(account_page.driver)
        print("Página de histórico de transações instanciada")

        # Verifica se a URL é a da página de histórico de transações
        assert list_tx_page.is_url_list_tx(), 'URL incorreta'
        print("URL de histórico de transações correta")

        # Realiza a pesquisa de transação na página de histórico de transações
        expected_transactions = [
            {"amount": "30", "type": "Credit"},
            {"amount": "4", "type": "Debit"}
        ]

        print("Verificando transações esperadas:")
        for idx, tx in enumerate(expected_transactions, start=1):
            print(f"Transação {idx}: Amount={tx['amount']}, Type={tx['type']}")

        list_tx_page.verify_expected_transactions(expected_transactions)
        print("Verificações de transações esperadas concluídas")

        list_tx_page.go_back()
        print("Voltou para a página de transações")

        # Realiza logout
        account_page.make_a_logout()
        print("Realiza logout")