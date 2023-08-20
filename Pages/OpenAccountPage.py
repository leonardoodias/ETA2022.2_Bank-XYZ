from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class OpenAccountPage(PageObject):

    _url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    _id_select_customer = 'userSelect'
    _select_name_albus = 'Albus Dumbledore'
    _id_currency = 'currency'
    _select_currency_rupee = 'Rupee'
    _xpath_btn_process = "//button[text()='Process']"
    _text_displayed_success = 'Account created successfully with account Number'

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver=driver)

    def select_customer(self):
        """
        Seleciona o customer

        :return: None
        """
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.ID, self._id_select_customer)))
        select = Select(select_element)
        select.select_by_visible_text(self._select_name_albus)

    def select_currency(self):
        """
        Seleciona o currency

        :return: None
        """
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.ID, self._id_currency)))
        select = Select(select_element)
        select.select_by_visible_text(self._select_currency_rupee)

    def click_button_process(self):
        """
        Clica no botão process

        :return: None
        """
        self.driver.find_element(By.XPATH, self._xpath_btn_process).click()

    def check_popup_success(self):
        return self.check_popup_and_accept(self._text_displayed_success)

    def is_url_open_account(self):
        return self.check_page(self._url)
