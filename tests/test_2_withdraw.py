from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.AccountPage import AccountPage


class TestWithdraw:
    def test_make_a_withdraw(self, open_home_page):
        # Abre a página de login do cliente
        open_home_page.open_customer_login()

        # Página de login do cliente
        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)

        # Realiza o login do cliente
        login_customer_page.select_user_withdraw()
        login_customer_page.click_on_login()

        # Instancia a página de conta
        account_page = AccountPage(driver=login_customer_page.driver)

        # Obtém o saldo antes do saque
        initial_balance = account_page.get_balance()

        # Realiza um saque
        account_page.make_a_withdraw()

        # Aguarda a atualização do saldo após o saque
        account_page.wait_for_balance_update(initial_balance - float(account_page._value_withdraw))

        # Verifica a mensagem de sucesso
        assert account_page.message_success_withdraw(), 'Mensagem não encontrada'

        # Obtém o novo saldo após o saque
        new_balance_after_withdraw = account_page.get_balance()

        # Verifica se o valor do novo saldo é igual ao saldo anterior menos o valor do saque
        expected_balance = initial_balance - float(account_page._value_withdraw)
        assert new_balance_after_withdraw == expected_balance, 'Saldo após o saque incorreto'

        # Realiza logout
        account_page.make_a_logout()
