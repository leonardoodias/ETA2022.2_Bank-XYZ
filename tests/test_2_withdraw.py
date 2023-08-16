import pdb
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.AccountPage import AccountPage

class TestWithdraw:
    def test_make_a_withdraw(self, open_home_page):
        # Abre a página de login do cliente
        open_home_page.click_btn_customer_login()
        print("Clicou no botão de Login do cliente")

        # Página de login do cliente
        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)

        # Realiza o login do cliente
        login_customer_page.select_user_withdraw(login_customer_page.user_name_withdraw)
        login_customer_page.click_on_login()
        print("Selecionou cliente e clicou no botão login")

        # Instancia a página de conta
        account_page = AccountPage(driver=login_customer_page.driver)
        print("Página de conta instanciada")

        # Obtém o saldo antes do saque
        initial_balance = account_page.get_balance()
        print("Saldo antes do saque é:", initial_balance)

        # pdb.set_trace()  # Isso inicia o depurador

        # Realiza um saque
        account_page.make_a_withdraw()
        print("Realizou o saque")

        # Aguarda a atualização do saldo após o saque
        account_page.wait_for_balance_update(initial_balance - float(account_page.value_withdraw))
        print("Saldo atualizado após o saque")

        # Verifica a mensagem de sucesso
        assert account_page.message_sucess_withdraw(), 'Mensagem não encontrada'

        # Obtém o novo saldo após o saque
        new_balance_after_withdraw = account_page.get_balance()

        print("Saldo após o saque é:", new_balance_after_withdraw)

        # Verifica se o valor do novo saldo é igual ao saldo anterior menos o valor do saque
        expected_balance = initial_balance - float(account_page.value_withdraw)
        assert new_balance_after_withdraw == expected_balance, 'Saldo após o saque incorreto'

        # Realiza logout
        account_page.make_a_logout()
        print("Realiza logout")
