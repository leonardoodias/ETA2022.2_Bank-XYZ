from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageObject import PageObject


class TransactionPage(PageObject):

    # Locators
    _url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    _btn_back = '[ng-click="back()"]'
    _btn_reset = '[ng-click="reset()"]'
    _css_start_date = 'input#start'
    _css_end_date = 'input#end'
    _css_transaction_rows = 'table.table tbody tr'
    _css_actual_date_locator = 'td:nth-child(1)'
    _css_actual_amount_locator = 'td:nth-child(2)'
    _css_actual_type_locator = 'td:nth-child(3)'
    _text_btn_back = 'Back'
    _text_btn_reset = 'Reset'
    _css_table = "table.table"
    _css_tbody = "tbody"
    _tag_name_tr = "tr"

    def __init__(self, driver):
        super(TransactionPage, self).__init__(driver=driver)
        self.driver.get(self._url_transactions)
        self.wait = WebDriverWait(self.driver, 10)

    def is_url_list_tx(self):
        return self.check_page(self._url_transactions)

    def get_transaction_rows(self):
        """
        Pega a lista de elementos de linha de transação

        :return: Lista de elementos
        """
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self._css_transaction_rows)))

    def verify_transaction_in_table(self, row_number, expected_amount, expected_type):
        """
        Verifica as transações na tabela

        :param row_number: Numero de linhas
        :param expected_amount: Valor esperado
        :param expected_type: Tipo esperado
        :return: None
        """
        transaction_rows = self.get_transaction_rows()
        transaction_row = transaction_rows[row_number - 1]

        actual_amount = transaction_row.find_element(By.CSS_SELECTOR, self._css_actual_amount_locator).text
        actual_type = transaction_row.find_element(By.CSS_SELECTOR, self._css_actual_type_locator).text

        assert actual_amount == expected_amount
        assert actual_type == expected_type

    def verify_expected_transactions(self, expected_transactions):
        """
        Verifica as transações esperadas

        :param expected_transactions: Transações esperadas
        :return: None
        """
        for idx, expected_tx in enumerate(expected_transactions, start=1):
            self.verify_transaction_in_table(
                row_number=idx,
                expected_amount=expected_tx["amount"],
                expected_type=expected_tx["type"]
            )

    def go_back(self):
        """
        Sai da tela de transações

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, self._btn_back).click()

    def click_button_reset_list(self):
        """
        Reseta a lista

        :return: None
        """
        reset = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self._btn_reset)))
        reset.click()

    def validate_if_table_contains_transaction(self):
        """
        Valida se a tabela contem transações

        :return: True or False
        """
        table_element = self.driver.find_element(By.CSS_SELECTOR, self._css_table)

        # Localize o corpo da tabela onde as linhas de dados estão contidas
        tbody_element = table_element.find_element(By.CSS_SELECTOR, self._css_tbody)

        # Verifique se não existem elementos de linha (ou seja, <tr>) dentro do corpo da tabela
        rows = tbody_element.find_elements(By.TAG_NAME, self._tag_name_tr)

        if len(rows) == 0:
            print("A tabela está vazia.")
            return False
        else:
            print(f"A tabela contém {len(rows)} linhas de dados.")
            return True
