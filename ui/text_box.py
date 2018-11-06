from ui.component import Component


class TextBox(Component):

    def send_keys(self, text_to_send):
        self.get_element().send_keys(text_to_send)
