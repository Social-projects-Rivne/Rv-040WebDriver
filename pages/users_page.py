"""Users page"""

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import PagesPath
from pages.base_page import BasePage
from ui.button import Button
from ui.text_box import TextBox
from util.utils import get_full_url
from locators.user_page_locators import UsrPageLocators


class UserPage(BasePage):
    """A class for users page actions"""

    def __init__(self, browser, base_url):
        """Initialize Users Page"""
        super().__init__(browser)

        self.base_url = (get_full_url(base_url, PagesPath.users))

        self.user_button = Button(self.browser.driver, UsrPageLocators.user_button_locator)
        self.new_user_button = Button(self.browser.driver, UsrPageLocators.new_user_button_locator)

        self.new_name_textbox = TextBox(self.browser.driver, UsrPageLocators.new_name_textbox_locator)
        self.new_nickname_textbox = TextBox(self.browser.driver, UsrPageLocators.new_nickname_textbox_locator)
        self.new_email_textbox = TextBox(self.browser.driver, UsrPageLocators.new_email_textbox_locator)
        self.new_employee_code_textbox = TextBox(self.browser.driver, UsrPageLocators.new_employee_code_textbox_locator)
        self.new_role_button = Button(self.browser.driver, UsrPageLocators.new_role_button_locator)
        self.new_password_textbox = TextBox(self.browser.driver, UsrPageLocators.new_password_textbox_locator)
        self.new_confirm_password_textbox = TextBox(self.browser.driver,
                                                    UsrPageLocators.new_confirm_password_textbox_locator)
        self.new_user_save_button = Button(self.browser.driver, UsrPageLocators.new_user_save_button_locator)

    def add_user(self, new_name, new_nickname, new_email, new_employee_code,
                 new_password, new_confirm_password):
        """Add User"""
        self.user_button.click()
        self.new_user_button.click()
        self.new_name_textbox.send_keys(new_name)
        self.new_nickname_textbox.send_keys(new_nickname)
        self.new_email_textbox.send_keys(new_email)
        self.new_employee_code_textbox.send_keys(new_employee_code)
        self.new_password_textbox.send_keys(new_password)
        self.new_confirm_password_textbox.send_keys(new_confirm_password)
        self.new_user_save_button.click()

    def message_window(self):
        """javascript message"""
        return WebDriverWait(self.browser.driver, 5).until(ec.visibility_of_element_located                                                            (UsrPageLocators.new_user_message))

    def message_window_text(self):
        """javascript message text"""
        return WebDriverWait(self.browser.driver, 5).until(ec.text_to_be_present_in_element
                                                            (UsrPageLocators.new_user_message,
                                                             "User was successfully created."))
