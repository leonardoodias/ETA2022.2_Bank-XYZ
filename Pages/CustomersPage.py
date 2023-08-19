from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomersPage(PageObject):

    link_sort_first_name = "//a[contains(text(), 'First Name')]"
    url_customersPage = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    name_search = '[ng-model="searchCustomer"]'
    btn_delete = '[ng-click="deleteCust(cust)"]'
    table_trs = '[ng-repeat="cust in Customers | orderBy:sortType:sortReverse | filter:searchCustomer"]'


    def _init_(self, browser):
        super(CustomersPage, self)._init_(driver=browser)

    def click_sort_by_first_name(self):
        first_name = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          self.link_sort_first_name)))
        first_name.click()

    def is_url_customers_page(self):
        return self.is_url(self.url_customersPage)

    def find_customer(self, name):
        campo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.name_search)))
        campo.send_keys(name)

    def delete_customer(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_delete)))
        btn.click()

    def check_table(self):
        tabela = self.driver.find_elements(By.CSS_SELECTOR, self.table_trs)
        return len(tabela)
