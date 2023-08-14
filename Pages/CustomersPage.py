from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject

class CustomersPage(PageObject):
    url_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'

    def __init__(self, driver):
        super(CustomersPage,self).__init__(driver=driver)
        self.driver.get(self.url_customers)

    def is_url_customers_page(self):
        return self.is_url(url=self.url_customers)
