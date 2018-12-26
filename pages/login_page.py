"""Login page"""

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from constants.constants import PagesPath
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from ui.button import Button
from ui.text_box import TextBox
from util.utils import get_full_url


class LoginPage(BasePage):
    """Login page action methods come here."""

    def __init__(self, browser, base_url):
        """Initialize Login Page"""
        super().__init__(browser)
        self.base_url = base_url
        self.email_box = TextBox(self.browser, LoginPageLocators.login_textbox_locator)
        self.password_box = TextBox(self.browser, LoginPageLocators.password_textbox_locator)
        self.login_button = Button(self.browser, LoginPageLocators.login_button_locator)

    def login(self, email, password):
        """Navigate to Login Page and do login"""
        self.browser.go_to_url(get_full_url(self.base_url, PagesPath.login))
        self.email_box.send_keys(email)
        self.password_box.send_keys(password)
        self.login_button.click()

    def message(self):
        return WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(LoginPageLocators.message_locator))
