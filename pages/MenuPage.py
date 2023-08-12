from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class MenuPage(PageObject):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    name_btn_bank_manager = 'Bank Manager Login'
    name_btn_customer_login = 'Customer Login'

    def __init__(self, browser):
        super(MenuPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def open_customer_login(self):
        a = self.driver.find_element(By.CLASS_NAME, 'center')

        a.find_element(By.LINK_TEXT, self.name_btn_customer_login).click()

    def open_bank_manager_login(self):
        self.driver.find_element(By.LINK_TEXT, self.name_btn_bank_manager).click()
