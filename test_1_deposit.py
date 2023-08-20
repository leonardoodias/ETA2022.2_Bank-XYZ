from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.AccountPage import AccountPage


class TestDeposit:
    def test_make_a_deposit(self, open_home_page):

        # Abre a página de login do cliente
        open_home_page.open_customer_login()

        # Página de login do cliente
        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)

        # Realiza o login do cliente
        login_customer_page.select_user_deposit()
        login_customer_page.click_on_login()

        # Instancia a página de conta e seleciona o tipo de conta
        account_page = AccountPage(driver=login_customer_page.driver)
        account_page.click_type_account()

        # Obtém o saldo antes do depósito
        initial_balance = account_page.get_balance()

        # Realiza um depósito
        account_page.make_a_deposit()

        # Aguarda a atualização do saldo após o depósito
        account_page.wait_for_balance_update(initial_balance + float(account_page._value_deposit))

        # Verifica a mensagem de sucesso
        assert account_page.message_success_deposit(), 'Mensagem não encontrada'

        # Verifica se o valor foi adicionado ao Balance após o depósito
        new_balance = account_page.get_balance()
        assert new_balance == initial_balance + float(account_page._value_deposit), 'Saldo após o depósito incorreto'

        # Realiza logout
        account_page.make_a_logout()
        print("Realiza o logout")
