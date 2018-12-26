"""Okr page"""

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import PagesPath
from locators.okr_page_locators import OkrPageLocators
from pages.base_page import BasePage
from ui.button import Button
from ui.text_box import TextBox
from util.utils import get_full_url


class OkrPage(BasePage):
    """Okr page action methods come here."""

    def __init__(self, browser, base_url):
        """Initialize OKR Page"""
        super().__init__(browser)
        self.base_url = (get_full_url(base_url, PagesPath.okr))

        self.okr_button = Button(self.browser,
                                 OkrPageLocators.okr_button_locator)
        self.okr_new_button = Button(self.browser,
                                     OkrPageLocators.okr_new_button_locator)
        self.okr_name = TextBox(self.browser,
                                OkrPageLocators.okr_name_textbox_locator)
        self.okr_start_date_home_button = Button(self.browser,
                                                 OkrPageLocators.okr_start_date_home_button_locator)
        self.okr_start_date_button1 = Button(self.browser,
                                             OkrPageLocators.okr_start_date_button1_locator)
        self.okr_start_date_button2 = Button(self.browser,
                                             OkrPageLocators.okr_start_date_button2_locator)
        self.okr_end_date_home_button = Button(self.browser,
                                               OkrPageLocators.okr_end_date_home_button_locator)
        self.okr_end_date_button1 = Button(self.browser,
                                           OkrPageLocators.okr_end_date_button1_locator)
        self.okr_end_date_button2 = Button(self.browser,
                                           OkrPageLocators.okr_end_date_button2_locator)
        self.okr_objective_textbox = TextBox(self.browser,
                                             OkrPageLocators.okr_objective_textbox_locator)
        self.okr_objective_key1_textbox = TextBox(self.browser,
                                                  OkrPageLocators.okr_objective_key1_textbox_locator)
        self.okr_objective_key2_textbox = TextBox(self.browser,
                                                  OkrPageLocators.okr_objective_key2_textbox_locator)
        self.okr_save_button = Button(self.browser,
                                      OkrPageLocators.okr_save_button_locator)

    def add_okr(self, name, objective, obj_key1, obj_key2):
        """Add OKR"""
        self.okr_button.click()
        self.okr_new_button.click()
        self.okr_name.send_keys(name)

        self.okr_start_date_button1.click()
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable
                                              (OkrPageLocators.okr_start_date_home_button_locator))
        self.okr_start_date_home_button.click()
        self.okr_start_date_button2.click()

        self.okr_end_date_button1.click()
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable
                                              (OkrPageLocators.okr_end_date_home_button_locator))
        self.okr_end_date_home_button.click()
        self.okr_end_date_button2.click()

        self.okr_objective_textbox.send_keys(objective)
        self.okr_objective_key1_textbox.send_keys(obj_key1)
        self.okr_objective_key2_textbox.send_keys(obj_key2)

        self.okr_save_button.click()

    def message_window(self):
        """javascript message"""
        return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                     (OkrPageLocators.okr_message))

    def message_window_text(self):
        """javascript message text"""
        return WebDriverWait(self.browser, 10).until(ec.text_to_be_present_in_element
                                                     (OkrPageLocators.okr_message,
                                                      "Okr was successfully created."))
