"""Okr page"""

from constants.constants import PagesPath
from pages.base_page import BasePage
from ui.button import Button
from ui.text_box import TextBox
from locators.okr_page_locators import OkrPageLocators
from util.utils import get_full_url


class OkrPage(BasePage):
    """Okr page action methods come here."""

    def __init__(self, browser, base_url):
        """Initialize OKR Page"""
        super().__init__(browser)
        self.base_url = base_url
        self.okr_button = Button(self.browser.driver, OkrPageLocators.okr_button_locator)
        self.new_okr_button = Button(self.browser.driver, OkrPageLocators.new_okr_button_locator)
        self.okr_name = TextBox(self.browser.driver, OkrPageLocators.okr_name_textbox_locator)
        self.okr_start_date = Button(self.browser.driver, OkrPageLocators.okr_start_date_textbox_locator)
        self.okr_end_date = Button(self.browser.driver, OkrPageLocators.okr_end_date_textbox_locator)

    def navigate_okr(self):
        """Navigate okr page"""
        self.browser.go_to_url(get_full_url(self.base_url, PagesPath.okr))
        self.okr_button.click()

    def new_okr(self):
        """New OKR"""
        self.new_okr_button.click()

    def navigate_new_okr(self):
        """Navigate new okr"""
        self.browser.go_to_url(get_full_url(self.base_url, PagesPath.okr + "/new"))

    def set_okr_name(self, name):
        self.okr_name.send_keys(name)

    def set_okr_dates(self, start_date, end_date):
        # self.okr_start_date.send_keys(start_date)
        # self.okr_end_date.send_keys(end_date)
        self.okr_start_date.click()
