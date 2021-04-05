from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.home_page import HomePageLocators


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'


    @property
    def blog_link(self):
        return self.driver.find_element_by_id(*HomePageLocators.NAV_LINK)