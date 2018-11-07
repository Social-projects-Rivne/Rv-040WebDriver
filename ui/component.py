
class Component:

    def __init__(self, browser, selector):
        self.browser = browser
        self.selector = selector

    def get_element(self):
        return self.browser.find_element(*self.selector)
