from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageObject import PageObject

class ListTxPage(PageObject):

    # Locators
    url_transactions = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    btn_back = '[ng-click="back()"]'
    btn_reset = '[ng-click="reset()"]'
    css_start_date = 'input#start'
    css_end_date = 'input#end'
    css_transaction_rows = 'table.table tbody tr'
    css_actual_date_locator = 'td:nth-child(1)'
    css_actual_amount_locator = 'td:nth-child(2)'
    css_actual_type_locator = 'td:nth-child(3)'
    text_btn_back = 'Back'
    text_btn_reset = 'Reset'

    def __init__(self, driver):
        super(ListTxPage, self).__init__(driver=driver)
        self.driver.get(self.url_transactions)
        self.wait = WebDriverWait(self.driver, 10)

    def is_url_list_tx(self):
        return self.is_url(url=self.url_transactions)

    def get_transaction_rows(self):
        # Retorna a lista de elementos de linha de transação
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.css_transaction_rows))
        )
    def verify_transaction_in_table(self, row_number, expected_amount, expected_type):
        transaction_rows = self.get_transaction_rows()
        transaction_row = transaction_rows[row_number - 1]

        actual_amount = transaction_row.find_element(By.CSS_SELECTOR, self.css_actual_amount_locator).text
        actual_type = transaction_row.find_element(By.CSS_SELECTOR, self.css_actual_type_locator).text

        # assert actual_date == expected_date
        assert actual_amount == expected_amount
        assert actual_type == expected_type

    def verify_expected_transactions(self, expected_transactions):
        for idx, expected_tx in enumerate(expected_transactions, start=1):
            self.verify_transaction_in_table(
                row_number=idx,
                expected_amount=expected_tx["amount"],
                expected_type=expected_tx["type"]
            )
    def go_back(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_back).click()

    def del_list(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_reset).click()

