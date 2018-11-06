"""Locators"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """A class for main page locators. All main page locators should come here"""

    login_button = (By.CLASS_NAME, 'btn-login')
    email = (By.ID, 'user_email')
    password = (By.ID, 'user_password')
