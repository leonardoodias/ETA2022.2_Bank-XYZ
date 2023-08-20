import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from Pages.PageObject import PageObject


class AccountPage(PageObject):
    # Locators
    _url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    _id_account_select = 'accountSelect'
    _css_btn_deposit = '[ng-click="deposit()"]'
    _css_btn_withdraw = '[ng-click="withdrawl()"]'
    _css_btn_transaction = '[ng-click="transactions()"]'
    _css_amount = '[placeholder="amount"]'
    _class_btn_deposit = 'btn-default'
    _class_btn_withdraw = 'btn-default'
    _css_logout = ".btn.logout"
    _class_message_deposit = '[ng-show="message"]'
    _class_message_withdraw = '[ng-show="message"]'
    _amount_balance = 'div.center strong.ng-binding:nth-of-type(2)'
    _value_deposit = '100'
    _value_withdraw = '50'
    _text_message_deposit = 'Deposit Successful'
    _text_message_withdraw = 'Transaction successful'

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)
        self.wait = WebDriverWait(driver, 10)
        self.driver.get(self._url_account_page)

    def click_type_account(self):
        """
        Clica no dropdown e seleciona a conta

        :return: None
        """
        select_element = self.wait.until(
            EC.presence_of_element_located((By.ID, self._id_account_select))
        )
        select = Select(select_element)
        select.select_by_index(1)

    def get_balance(self):
        """
        Obtém o saldo atual

        :return: None
        """
        balance_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._amount_balance))
        )

        return float(balance_element.text)

    def make_a_deposit(self, value_deposit=100):
        """
        Realiza um deposito

        :param value_deposit: valor do deposito em numero inteiro
        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._css_btn_deposit))
        ).click()

        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "form-group"), "Amount to be Deposited"))

        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._css_amount))
        )

        amount_field = self.driver.find_element(By.CSS_SELECTOR, self._css_amount)
        amount_field.send_keys(value_deposit)

        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, self._class_btn_deposit))
        ).click()

    def message_success_deposit(self):
        """
        Verifica a mensagem de sucesso após o deposito

        :return: None
        """
        success_message = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._class_message_deposit))
        ).text

        return success_message == self._text_message_deposit

    def wait_for_balance_update(self, expected_balance, timeout=5, interval=1):
        """
        Aguarda a atualização do saldo após a transação

        :param expected_balance: Valor do balanço esperado
        :param timeout: Tempo maximo de espera
        :param interval: Intervalo de tempo
        :return: True or False
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_balance = self.get_balance()
            if current_balance == expected_balance:
                return True
            time.sleep(interval)
        return False

    def validate_balance_after_transaction(self, initial_balance, transaction_value):
        """
        Valida o saldo após uma transação (depósito ou saque)

        :param initial_balance: valor do balanço inicial
        :param transaction_value: Valor da transação
        :return: Novo valor do balanço
        """
        new_balance = self.get_balance()

        return new_balance == initial_balance + transaction_value

    def make_a_withdraw(self, value_withdraw=50):
        """
        Realiza um saque

        :param value_withdraw: Valor do saque em numero inteiro
        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._css_btn_withdraw))
        ).click()

        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "form-group"), "Amount to be Withdrawn"))

        amount_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._css_amount))
        )

        amount_field.clear()  # Limpa o campo de valor antes de preencher
        amount_field.send_keys(value_withdraw) # Insere o valor do saque

        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, self._class_btn_withdraw))
        ).click()

    def message_success_withdraw(self):
        """
        Verifica a mensagem de sucesso após o saque

        :return: None
        """
        success_message = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._class_message_withdraw))
        ).text

        return success_message == self._text_message_withdraw

    def validate_balance_after_withdraw(self, initial_balance):
        """
        Valida o saldo após o saque

        :param initial_balance: Valor inicial do balanço
        :return: Novo valor do balanço
        """
        new_balance = self.get_balance()
        return new_balance == initial_balance - float(self._value_withdraw)

    def click_transaction_button(self):
        """
        Clica no botão de histórico de transações
        :return: None
        """
        transaction_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self._css_btn_transaction))
        )
        transaction_button.click()

    def make_a_logout(self):
        """
        Faz logout da conta

        :return: None
        """
        logout_button = self.driver.find_element(By.CSS_SELECTOR, self._css_logout)
        logout_button.click()

    def is_url_account(self):
        return self.check_page(self._url_account_page)