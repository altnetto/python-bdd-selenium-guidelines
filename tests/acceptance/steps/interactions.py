from tests.acceptance.page_model.base_page import BasePage
from behave import *

# that is used to enables the regular expression matching, that we will use above
use_step_matcher('re')


# here, we insert a regular expression statement, that makes the part inside double quotes turns into a variable, what is very useful
@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError(f'Matching link ({link_text!r}) not found')
