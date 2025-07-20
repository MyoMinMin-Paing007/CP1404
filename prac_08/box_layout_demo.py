from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greeting button press."""
        # Use the correct 'text' attribute
        input_text = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {input_text}"

    def handle_clear(self):
        """Clear the text input field and output label."""
        # Update the 'text' attributes instead of overwriting the widgets
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
