from lib.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, context):
       BasePage.__init__(self, context.browser, base_url=BasePage.base_url)
    
    locator_dictionary = {
    "email" : (By.NAME, 'session[username_or_email]'),
    "password" : (By.NAME, 'session[password]'),
    "submit" : (By.CSS_SELECTOR, 'input[type="submit"]'),
    "error_message" : 'The email and password you entered did not match our records. Please double-check and try again.'
    }