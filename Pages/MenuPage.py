from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage(PageObject):

    _url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    _name_btn_bank_manager = 'Bank Manager Login'
    _css_btn_customer_login = '[ng-click="customer()"]'
    _btn_bank_manager = 'button.btn.btn-primary.btn-lg[ng-click="manager()"]'
    _btn_customer_login = 'button.btn.btn-primary.btn-lg[ng-click="customer()"]'

    def __init__(self, browser):
        super(MenuPage, self).__init__(browser=browser)
        self.driver.get(self._url)

    def open_customer_login(self):
        """
        Clica no botão Customer Login

        :return: None
        """
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self._btn_customer_login)))
        btn.click()

    def open_bank_manager_login(self):
        """
        Clica no botão Bank Manager Login

        :return: None
        """
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self._btn_bank_manager)))
        btn.click()
