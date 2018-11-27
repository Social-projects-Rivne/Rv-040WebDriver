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
    """A class for users page locators. All users page locators should come here"""

    def __init__(self, browser, base_url):
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
