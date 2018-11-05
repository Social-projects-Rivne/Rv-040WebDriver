"""Base page"""


class BasePage:
    """Class for base page"""

    def __init__(self, driver):
        """Initialize webriver"""
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30
