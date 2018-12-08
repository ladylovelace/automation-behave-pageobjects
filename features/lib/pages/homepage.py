from lib.pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, context):
       BasePage.__init__(self, context.browser, base_url=context.base_url)
    
    locator_dictionary = {
    "tweet_input" : (By.ID, 'tweet-box-home-timeline'),
    "media_input" : (By.NAME, 'media[]'),
    "submit" : (By.CSS_SELECTOR, '.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn'),
    "submit_disabled" : (By.CSS_SELECTOR, '.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn.disabled'),
    }