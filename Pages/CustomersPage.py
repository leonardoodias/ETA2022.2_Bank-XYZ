from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomersPage(PageObject):

    _link_sort_first_name = "//a[contains(text(), 'First Name')]"
    _url_customersPage = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    _name_search = '[ng-model="searchCustomer"]'
    _btn_delete = '[ng-click="deleteCust(cust)"]'
    _table_trs = '[ng-repeat="cust in Customers | orderBy:sortType:sortReverse | filter:searchCustomer"]'
    _css_first_column_names = 'tbody tr td:first-child'

    def __init__(self, driver):
        super(CustomersPage, self).__init__(driver=driver)

    def click_sort_by_first_name(self):
        """
        Ordenar lista pelo nome

        :return: None
        """
        first_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          self._link_sort_first_name)))
        first_name.click()

    def is_url_customers_page(self):
        """
        Verifica a url da pagina

        :return: True or False
        """
        return self.check_page(self._url_customersPage)

    def find_customer(self, name):
        """
        Busca pelo nome do customer

        :param name: Nome do customer
        :return: None
        """
        campo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._name_search)))
        campo.send_keys(name)

    def delete_customer(self):
        """
        Delete o customer

        :return: None
        """
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._btn_delete)))
        btn.click()

    def check_table(self):
        """
        Verifica o tamanho da lista da tabela

        :return: Tamanho da lista da tabela
        """
        table = self.driver.find_elements(By.CSS_SELECTOR, self._table_trs)
        return len(table)

    def check_order_first_name_dec(self):
        """
        Verifica o nome na lista por ordem decrescente

        :return: True or False
        """
        all_names = self.driver.find_elements(By.CSS_SELECTOR, self._css_first_column_names)

        for i in range(1, len(all_names) - 1):
            if all_names[i].text < all_names[i + 1].text:
                return False
        return True
