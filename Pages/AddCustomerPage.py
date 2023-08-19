from selenium.common import TimeoutException
from Pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class AddCustomerPage(PageObject):

    url_AssCustomerPage = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    css_first_name = '[ng-model="fName"]'
    css_last_name = '[ng-model="lName"]'
    css_post_code = '[ng-model="postCd"]'
    class_btn_add = 'btn.btn-default'

    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)

    def fill_first_name(self, first_name):
        campo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_first_name)))
        campo.send_keys(first_name)

    def fill_last_name(self, last_name):
        campo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_last_name)))
        campo.send_keys(last_name)

    def fill_post_code(self, post_code):
        campo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_post_code)))
        campo.send_keys(post_code)

    def click_add_customer(self):
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.class_btn_add)))
        btn.click()

    def is_url_add_customer(self):
        return self.is_url(self.url_AssCustomerPage)

    def check_message_success(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present(),
                                            'Timed out esperando o alerta')
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            print("no alert")
