"""
If you want to run your test in headless mode, please uncomment line 17
"""

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lib.pages.basepage import BasePage
from lib.pages.loginpage import LoginPage
from lib.pages.homepage import HomePage

def before_all(context):

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = os.getcwd() + '/features/lib/chromedriver'

    driver = webdriver.Chrome(
        chrome_options=chrome_options, executable_path=chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(10)

    context.browser = BasePage(driver)
    context.login   = LoginPage(context)
    context.home    = HomePage(context)


def after_scenario(context, scenario):
    context.browser.screenshot(str(scenario))


def after_all(context):
    print("===== That's all folks =====")
    context.browser.close()