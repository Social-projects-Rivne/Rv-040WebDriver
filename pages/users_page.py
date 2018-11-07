"""Locators of users page"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """A class for users page locators. All users page locators should come here"""

    add_user_button_locator = (By.CLASS_NAME, 'dashed_link transition')
