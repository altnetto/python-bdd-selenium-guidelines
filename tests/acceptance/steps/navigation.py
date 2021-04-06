from behave import *
from selenium import webdriver
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.blog_page import BlogPage


use_step_matcher('re')


base_url = 'http://127.0.0.1:5000'


@given('I am on the Homepage')
def step_impl(context):
    context.driver = webdriver.Firefox()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Firefox()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the Homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url


@step('Close the window')
def step_impl(context):
    context.driver.close()