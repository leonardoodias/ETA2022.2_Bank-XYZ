import time
import pdb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from Pages.PageObject import PageObject

class AccountPage(PageObject):
    # Locators
    url_account_page = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    id_account_select = 'accountSelect'
    css_btn_deposit = '[ng-click="deposit()"]'
    css_btn_withdraw = '[ng-click="withdrawl()"]'
    css_amount = '[placeholder="amount"]'
    class_btn_deposit = 'btn-default'
    class_btn_withdraw = 'btn-default'
    css_logout = ".btn.logout"
    class_message_deposit = '[ng-show="message"]'
    class_message_withdraw = '[ng-show="message"]'
    amount_balance = 'div.center strong.ng-binding:nth-of-type(2)'
    value_deposit = '100'
    value_withdraw = '50'
    text_message_deposit = 'Deposit Successful'
    text_message_withdraw = 'Transaction successful'

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver=driver)
        self.wait = WebDriverWait(driver, 5)
        self.driver.get(self.url_account_page)

    def click_type_account(self):
        # Clica no dropdown e seleciona a conta
        select_element = self.wait.until(
            EC.presence_of_element_located((By.ID, self.id_account_select))
        )
        select = Select(select_element)
        select.select_by_index(1)  # Seleciona a conta

    def get_balance(self):
        # Obtém o saldo atual
        balance_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.amount_balance))
        )

        return float(balance_element.text)

    def make_a_deposit(self):
        # Realiza um depósito
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_btn_deposit))
        ).click()

        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.css_amount))
        )

        amount_field = self.driver.find_element(By.CSS_SELECTOR, self.css_amount)
        amount_field.send_keys(self.value_deposit)

        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.class_btn_deposit))
        ).click()

    def message_sucess_deposit(self):
        # Verifica a mensagem de sucesso após o depósito
        success_message = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.class_message_deposit))
        ).text

        return success_message == self.text_message_deposit

    def wait_for_balance_update(self, expected_balance, timeout=5, interval=1):
        # Aguarda a atualização do saldo após a transação
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_balance = self.get_balance()
            if current_balance == expected_balance:
                return True
            time.sleep(interval)
        return False

    def validate_balance_after_transaction(self, initial_balance, transaction_value):
        # Valida o saldo após uma transação (depósito ou saque)
        new_balance = self.get_balance()

        return new_balance == initial_balance + transaction_value

    def make_a_withdraw(self):
        # Realiza um saque
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_btn_withdraw))
        ).click()

        amount_field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.css_amount))
        )

        amount_field.clear()  # Limpa o campo de valor antes de preencher
        amount_field.send_keys(self.value_withdraw) # Insere o valor do saque

        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.class_btn_withdraw))
        ).click()


    def message_sucess_withdraw(self):
        # Verifica a mensagem de sucesso após o saque
        success_message = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.class_message_withdraw))
        ).text

        print("Mensagem de sucesso após saque:", success_message)

        return success_message == self.text_message_withdraw

    def validate_balance_after_withdraw(self, initial_balance):
        # Valida o saldo após o saque
        new_balance = self.get_balance()
        return new_balance == initial_balance - float(self.value_withdraw)

    def make_a_logout(self):
        logout_button = self.driver.find_element(By.CSS_SELECTOR, self.css_logout)
        logout_button.click()
