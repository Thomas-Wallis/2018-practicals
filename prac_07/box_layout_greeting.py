from kivy.app import App
from kivy.lang import Builder


class BoxLayoutGreeting(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout_greeting.kv")
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"

BoxLayoutGreeting().run()
