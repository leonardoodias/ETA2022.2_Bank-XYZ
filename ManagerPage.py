from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageObject import PageObject


class ManagerPage(PageObject):
    url_ManagerPage = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    btn_add_customer = '[ng-class="btnClass1"]'
    btn_open_account = '[ng-class="btnClass2"]'
    btn_customers = '[ng-class="btnClass3"]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)

    def click_add_customer(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_add_customer)))
        btn.click()
    def click_open_account(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.btn_open_account).click()
    def click_customers(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_customers)))
        btn.click()

    def is_url_manager_page(self):
        return self.is_url(self.url_ManagerPage)

