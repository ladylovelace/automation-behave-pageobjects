from lib.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class LogoutPage(BasePage):
    def __init__(self, context):
       BasePage.__init__(self, context.browser, base_url='http://twitter.com/logout')
    
    locator_dictionary = {
    "submit" : (By.CSS_SELECTOR, 'button[type="submit"]'),
}