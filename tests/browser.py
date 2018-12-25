"""Browser"""


class Browser:
    """Class browser"""

    def __init__(self, driver):
        """Initialize driver"""
        self._driver = driver

    def go_to_url(self, url):
        """Navigate to url"""
        self._driver.get(url)

    def get_driver(self):
        """Get driver for browser"""
        return self._driver

    def find_element(self, by, selector):
        """Find element by selector"""
        return self._driver.find_element(by, selector)
