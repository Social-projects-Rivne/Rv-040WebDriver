"""Base page"""


class BasePage:
    """Class for base page"""

    def __init__(self, browser):
        """Initialize webdriver Chrome"""
        self.browser = browser
