import pdb
from Pages.CustomerLoginPage import CustomerLoginPage
from Pages.AccountPage import AccountPage

class TestDeposit:
    def test_make_a_deposit(self, open_home_page):
        # Abre a página de login do cliente
        open_home_page.click_btn_customer_login()
        print("Clicou no botão de login do cliente")

        # Página de login do cliente
        login_customer_page = CustomerLoginPage(driver=open_home_page.driver)

        # Realiza o login do cliente
        login_customer_page.select_user_deposit(login_customer_page.user_name_deposit)
        login_customer_page.click_on_login()
        print("Realizou o login do cliente")

        # Instancia a página de conta e seleciona o tipo de conta
        account_page = AccountPage(driver=login_customer_page.driver)
        account_page.click_type_account()
        print("Página de conta instanciada")

        # Obtém o saldo antes do depósito
        initial_balance = account_page.get_balance()
        print("Saldo antes do depósito é:", initial_balance)

        # pdb.set_trace()  # Isso inicia o depurador

        # Realiza um depósito
        account_page.make_a_deposit()
        print("Realizou o depósito")

        # Aguarda a atualização do saldo após o depósito
        account_page.wait_for_balance_update(initial_balance + float(account_page.value_deposit))
        print("Saldo atualizado após o depósito")

        # Verifica a mensagem de sucesso
        assert account_page.message_sucess_deposit(), 'Mensagem não encontrada'

        # Verifica se o valor foi adicionado ao Balance após o depósito
        new_balance = account_page.get_balance()
        print("Saldo após o depósito é:", new_balance)
        assert new_balance == initial_balance + float(account_page.value_deposit), 'Saldo após o depósito incorreto'

        # Realiza logout
        account_page.make_a_logout()
        print("Realizou o logout")
