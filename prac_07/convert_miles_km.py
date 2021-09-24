from kivy.app import App
from kivy.lang import Builder


class ConvertToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_conversion(self):
        conversion_result = float(self.root.ids.input_text.text) * 1.609344
        self.root.ids.output_label.text = str(conversion_result)

    def handle_increment(self, increment):
        self.root.ids.input_text.text = str(int(self.root.ids.input_text.text) + increment)


ConvertToKilometers().run()
