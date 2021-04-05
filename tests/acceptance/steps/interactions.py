from behave import *

# that is used to enables the regular expression matching, that we will use above
use_step_matcher('re')


# here, we insert a regular expression statement, that makes the part inside double quotes turns into a variable, what is very useful
@when('I click on the link id "(.*)"')
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()


