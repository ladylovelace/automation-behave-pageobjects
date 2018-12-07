import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


class BasePage(object):

    # Browser init configs
    base_url = 'http://twitter.com/'
    chrome_options = Options()
    # chrome_options.binary_location = CHROME_BINARY
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = os.getcwd() + '/features/lib/chromedriver'
    # Call Chrome Browser
    driver = webdriver.Chrome(
        chrome_options=chrome_options, executable_path=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(10)

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

    def current_url(self, location=''):
        """
        get current pages
        """
        return self.driver.current_url

    def find(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element(selector[0], selector[1])

    def find_selector(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_css_selector(selector)

    def contains_content(self, text, timeout):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text))
            return elem
        except TimeoutException as ex:
            return False

    def contains_element(self, selector, timeout):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(selector))
            return elem
        except TimeoutException as ex:
            return False

    def screenshot(self, filename):
        self.driver.save_screenshot('./screenshot/' + filename + '.png')

    def move_offset(self, element, x, y):
        ActionChains(self.driver).move_to_element_with_offset(
            element, x, y).perform()

    def move_element(self, element):
        ActionChains(self.driver).move_to_element(
            element).perform()
