"""Locators"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """A class for main page locators. All main page locators should come here"""

    login_button_locator = (By.CLASS_NAME, 'btn-login')
    login_textbox_locator = (By.ID, 'user_email')
    password_textbox_locator = (By.ID, 'user_password')
    message_locator = (By.XPATH, '/html/body/script')
