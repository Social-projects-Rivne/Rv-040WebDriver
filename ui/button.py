from ui.component import Component


class Button(Component):

    def click(self):
        self.get_element().click()
