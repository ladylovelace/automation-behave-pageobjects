from behave import given, when, then
from config import USER
from features.lib.pages.logoutpage import LogoutPage


@given(u'a user navigates to page "logout"')
def visit_logout(context):
    context.browser.visit('/logout')

@given(u'"the user confirms he wants to logout"')
def logout_confirm(context):
    confirm = context.browser.find(LogoutPage.locator_dictionary['submit'])
    confirm.click()