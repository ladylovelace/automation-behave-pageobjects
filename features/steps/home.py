from behave import given, when, then
from config import USER
from features.lib.pages.homepage import HomePage
from features.steps import login

@given(u'the "{user_type}" user is logged in on the homepage')
def step_impl(context,user_type):
    login.visit_login(context, user_type)
    login.login(context, user_type)

@when(u'user post the tweet "{tweet_message}"')
def tweet(context, tweet_message):
    element = context.browser.find(HomePage.locator_dictionary['tweet_input'])
    element.clear()
    element.send_keys(tweet_message)


@then(u'the tweet button should be disabled')
def dont_tweet(context):
    element = context.browser.find(HomePage.locator_dictionary['submit_disabled'])
    assert element.is_enabled() == False



@then(u'the tweet button should be enabled')
def dont_tweet(context):
    element = context.browser.find(HomePage.locator_dictionary['submit'])
    assert element.is_enabled() == True