from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class MenuPage(PageObject):

    id_menu_btn = 'react-burger-menu-btn'
    id_menu_close_btn = 'react-burger-cross-btn'
    class_menu_items = 'bm-item-list'
    id_logout_menu_item = 'logout_sidebar_link'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_btn).click()

    def is_menu_open(self):
        try:
            self.driver.find_element(By.ID, self.id_menu_close_btn)
            self.driver.find_element(By.CLASS_NAME, self.class_menu_items)
            return True
        except NoSuchElementException:
            return False

    def click_logout(self):
        logout_menu_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.ID, self.id_logout_menu_item)))
        logout_menu_item.click()