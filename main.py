from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("main.kv")

class MainLayout(BoxLayout):
    def submit_form(self):
        name = self.ids.name_input.text
        gender = self.ids.gender_spinner.text
        agree = self.ids.agree_checkbox.active
        self.ids.result_label.text = f"Tên: {name}\nGiới tính: {gender}\nĐồng ý: {'Có' if agree else 'Không'}"

    def clear_form(self):
        self.ids.name_input.text = ""
        self.ids.gender_spinner.text = "Chọn"
        self.ids.agree_checkbox.active = False
        self.ids.result_label.text = ""

class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    MyApp().run()
