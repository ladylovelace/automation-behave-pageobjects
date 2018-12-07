import os

from lib.pages.basepage import BasePage
from features.steps import logout


def before_all(context):
    # cwd = os.getcwd() Usar depois o path nas configs do projeto
    context.browser = BasePage()


def after_scenario(context, scenario):
    logout.visit_logout(context)
    logout.logout_confirm(context)
    context.browser.screenshot(str(scenario))


def after_all(context):
    context.browser.close()
