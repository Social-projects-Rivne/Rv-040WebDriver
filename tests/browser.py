"""Browser"""


class Browser:
    """Class browser"""

    def __init__(self, driver):
        """Initialize driver"""
        self.driver = driver

    def go_to_url(self, url):
        """Navigate to url"""
        self.driver.get(url)

    def get_driver(self):
        """Get driver for browser"""
        return self.driver

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)