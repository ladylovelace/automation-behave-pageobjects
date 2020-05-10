from lib.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, context):
       BasePage.__init__(self, context.browser, base_url='https://twitter.com/')
    
    locator_dictionary = {
    "tweet_input" : (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]'),
    "media_input" : (By.NAME, 'media[]'),
    "submit" : (By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]'),
    "submit_disabled" : (By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]'),
    }

    def tweet(self, text):
        element = self.driver.find(self.locator_dictionary['tweet_input'])
        element.clear()
        element.send_keys(text)
        return element
