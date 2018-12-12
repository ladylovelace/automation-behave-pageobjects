from behave import given, when, then

from config import USER
from features.lib.pages.homepage import HomePage


@given(u'the "{user_type}" user is logged in on the homepage')
def step_impl(context,user_type):
    home = context.browser.contains_content(USER['valid']['username'], 10)
    if not home:
        context.browser.visit('#')
        context.login.signin(USER[user_type]['email'], USER[user_type]['pass'])


@when(u'user post the tweet "{tweet_message}"')
def tweet(context, tweet_message):
    tweet = context.home.tweet(tweet_message)
    assert tweet


@then(u'the tweet button should be disabled')
def dont_tweet(context):
    element = context.browser.find(HomePage.locator_dictionary['submit_disabled'])
    assert element.is_enabled() == False


@then(u'the tweet button should be enabled')
def dont_tweet(context):
    element = context.browser.find(HomePage.locator_dictionary['submit'])
    assert element.is_enabled() == True


@then(u'the user should be able to tweet')
def submit_tweet(context):
    element = context.browser.find(HomePage.locator_dictionary['submit'])
    element.click()
