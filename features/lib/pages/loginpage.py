from lib.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, context):
       BasePage.__init__(self, context.browser, base_url='http://twitter.com/')
    
    locator_dictionary = {
    "email" : (By.NAME, 'session[username_or_email]'),
    "password" : (By.NAME, 'session[password]'),
    "submit" : (By.CSS_SELECTOR, 'input[type="submit"]'),
    "error_message" : 'The email and password you entered did not match our records. Please double-check and try again.'
    }

    def signin(self, email, password):
        username_field = self.driver.find(self .locator_dictionary['email'])
        password_field = self.driver.find(self.locator_dictionary['password'])
        username_field.send_keys(email)
        password_field.send_keys(password)
        submit_button = self.driver.find(self.locator_dictionary['submit'])
        submit = submit_button.click()
        return submit_button