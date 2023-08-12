from pages.PageObject import PageObject
from selenium.webdriver.common.by import By


class ManagerPage(PageObject):
    url = ''
    btn_add_customer = 'Add Customer'
    btn_open_account = ''
    btn_customers = ''

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)

    def click_add_customer(self):
        return self.driver.find_element(By.LINK_TEXT, self.btn_add_customer).click()
