"""Base page"""

from selenium import webdriver


class BasePage:
    """Class for base page"""

    def __init__(self):
        """Initialize webriver Chrome"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.timeout = 30
