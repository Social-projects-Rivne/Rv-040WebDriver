"""Login page"""

from constants.constants import InitUrls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page action methods come here."""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.driver.get(InitUrls.login)
        self.login_button = self.driver.find_element(LoginPageLocators.login_button[0],
                                                     LoginPageLocators.login_button[1])
        self.email_field = self.driver.find_element(LoginPageLocators.email[0],
                                                    LoginPageLocators.email[1])
        self.password_field = self.driver.find_element(LoginPageLocators.password[0],
                                                       LoginPageLocators.password[1])

    def login(self, email, password):
        """Send keys"""
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.login_button.click()
