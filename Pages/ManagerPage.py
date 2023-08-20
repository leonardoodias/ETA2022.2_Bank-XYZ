from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageObject import PageObject


class ManagerPage(PageObject):
    _url_ManagerPage = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    _btn_add_customer = '[ng-class="btnClass1"]'
    _btn_open_account = '[ng-class="btnClass2"]'
    _btn_customers = '[ng-class="btnClass3"]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)

    def click_add_customer(self):
        """
        Clica no botão para adicionar um customer

        :return: None
        """
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._btn_add_customer)))
        btn.click()

    def click_open_account(self):
        """
        Clica no botão open account

        :return: None
        """
        btn_open_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                                  self._btn_open_account)))
        btn_open_account.click()

    def click_customers(self):
        """
        Clica no botão customers
        :return:
        """
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._btn_customers)))
        btn.click()

    def is_url_manager_page(self):
        return self.check_page(self._url_ManagerPage)
