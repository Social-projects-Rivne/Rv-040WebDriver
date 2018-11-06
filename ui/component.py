
class Component:

    def __init__(self, driver, selector):
        self.driver = driver
        self.selector = selector

    def get_element(self):
        return self.driver.find_element(*self.selector)
