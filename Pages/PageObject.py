from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_matches(url))

    def check_page(self, url):
        """
        Verifica a url da pagina atual

        :param url: url da pagina
        :return: Url da pagina
        """
        return self.is_url(url)

    def check_popup_and_accept(self, expected_text):
        """
        Verifica o popup de sucesso e da ok no alert

        :param expected_text: mensagem esperada
        :return: True or False
        """
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        text_present = alert.text
        print("Texto esperado", expected_text)
        print(text_present)
        if expected_text in text_present:
            alert.accept()
            return True
        else:
            return False
