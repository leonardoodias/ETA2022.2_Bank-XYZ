from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageObject import PageObject


class CustomerLoginPage(PageObject):
    _url_customer_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    _id_user_select = 'userSelect'
    _css_selector_login = "[name=myForm] button"

    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)

    def select_user_deposit(self, user_name_deposit='Harry Potter'):
        """
        Seleciona um usuario para depositar

        :param user_name_deposit: Nome do usuario
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, self._id_user_select)))
        select = Select(select_element)
        select.select_by_visible_text(user_name_deposit)

    def select_user_withdraw(self, user_name_withdraw='Hermoine Granger'):
        """
        Seleciona um usuario para saque

        :param user_name_withdraw: Nome do usuario
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, self._id_user_select)))
        select = Select(select_element)
        select.select_by_visible_text(user_name_withdraw)

    def click_on_login(self):
        """
        Clicar no botão login

        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._css_selector_login)))
        login_button.click()
