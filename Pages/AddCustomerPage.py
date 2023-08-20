from selenium.common import TimeoutException
from Pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomerPage(PageObject):

    _url_AssCustomerPage = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    _css_first_name = '[ng-model="fName"]'
    _css_last_name = '[ng-model="lName"]'
    _css_post_code = '[ng-model="postCd"]'
    _class_btn_add = 'btn.btn-default'
    _text_alert = 'Customer added successfully with customer id'

    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)

    def fill_first_name(self, first_name):
        """
        Preenche o campo de first name

        :param first_name: Primeiro nome
        :return: None
        """
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._css_first_name)))
        field.send_keys(first_name)

    def fill_last_name(self, last_name):
        """
        Preenche o campo de last name

        :param last_name: Sobrenome
        :return: None
        """
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._css_last_name)))
        field.send_keys(last_name)

    def fill_post_code(self, post_code):
        """
        Preenche o campo post code

        :param post_code: Codigo postal
        :return: None
        """
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._css_post_code)))
        field.send_keys(post_code)

    def click_add_customer(self):
        """
        Clica para dicionar o customer

        :return: None
        """
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self._class_btn_add)))
        btn.click()

    def is_url_add_customer(self):
        return self.check_page(self._url_AssCustomerPage)

    def check_popup_success(self):
        """
        Verifica mensagem de sucesso do alert

        :return: None
        """
        return self.check_popup_and_accept(self._text_alert)
