import os

from lib.pages.basepage import BasePage


def before_all(context):
    context.browser = BasePage()


def after_scenario(context, scenario):
    context.browser.screenshot(str(scenario))


def after_all(context):
    print("===== That's all folks =====")
    context.browser.close()