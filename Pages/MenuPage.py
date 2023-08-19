from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage(PageObject):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    name_btn_bank_manager = 'Bank Manager Login'
    css_btn_customer_login = '[ng-click="customer()"]'
    btn_bank_manager = 'button.btn.btn-primary.btn-lg[ng-click="manager()"]'
    btn_customer_login = 'button.btn.btn-primary.btn-lg[ng-click="customer()"]'

    def __init__(self, browser):
        super(MenuPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def click_btn_customer_login(self):
        wait = WebDriverWait(self.driver, 10)
        customer_login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_btn_customer_login)))
        customer_login_button.click()

    def open_customer_login(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_customer_login)))
        btn.click()

    def open_bank_manager_login(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_bank_manager)))
        btn.click()
