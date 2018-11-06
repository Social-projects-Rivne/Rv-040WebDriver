
class Browser:

    def __init__(self, driver):
        self._driver = driver

    def go_to_url(self, url):
        self._driver.get(url)

    def get_driver(self):
        return self._driver
