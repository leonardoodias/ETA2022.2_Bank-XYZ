from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.PageObject import PageObject

class CustomerLoginPage(PageObject):
    url_customer_login = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    id_user_select = 'userSelect'
    user_name_deposit = 'Harry Potter'
    user_name_withdraw = 'Hermoine Granger'
    css_selector_login = "[name=myForm] button"

    def __init__(self, driver):
        super(CustomerLoginPage, self).__init__(driver=driver)

    def select_user_deposit(self, user_name_deposit):
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, self.id_user_select)))
        select = Select(select_element)
        select.select_by_visible_text(user_name_deposit)

    def select_user_withdraw(self, user_name_withdraw):
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, self.id_user_select)))
        select = Select(select_element)
        select.select_by_visible_text(user_name_withdraw)
    def click_on_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.css_selector_login)))
        login_button.click()
