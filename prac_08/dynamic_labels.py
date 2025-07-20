from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to dynamically create labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

    def build(self):
        """Build the Kivy app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels dynamically and add them to the GUI."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name, font_size=24)
            # Add the label to the "main" BoxLayout
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
