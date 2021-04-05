from behave import *
from selenium import webdriver


use_step_matcher('re')


base_url = 'http://127.0.0.1:5000'


@given('I am on the Homepage')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get(base_url)


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get(f'{base_url}/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = f'{base_url}/blog'
    
    assert context.browser.current_url == expected_url


@then('I am on the Homepage')
def step_impl(context):
    expected_url = base_url + '/'
    
    assert context.browser.current_url == expected_url