import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage(object):


    base_url = 'http://twitter.com/'

    def __init__(self, browser):
        self.driver = browser


    def close(self):
        """
        close the webdriver instance
        """
        # self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)


    def find(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element(selector[0], selector[1])

    def contains_content(self, text, timeout):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text))
            return elem
        except TimeoutException as ex:
            return False

    def screenshot(self, filename):
        self.driver.save_screenshot('./screenshot/' + filename + '.png')
