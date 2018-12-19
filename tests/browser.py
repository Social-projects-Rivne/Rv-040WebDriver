
class Browser:

    def __init__(self, driver):
        driver.implicitly_wait(30)
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def get_driver(self):
        return self.driver

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)
