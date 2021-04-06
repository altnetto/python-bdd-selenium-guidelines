from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.new_post_page import NewPostPageLocators


class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        
