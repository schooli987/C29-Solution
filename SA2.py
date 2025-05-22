from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner

class StudentApp(App):
    def build(self):
        return self.build_form_screen()

    def build_form_screen(self):
        layout = BoxLayout(orientation='vertical')

        # --- Form Inputs ---
        form = GridLayout(cols=2)

        self.name_input = TextInput()
        self.age_input = TextInput(input_filter='int')
        self.gender_spinner = Spinner(text='Select', values=['Male', 'Female'])
        self.class_input = TextInput()
        self.address_input = TextInput()

        form.add_widget(Label(text="Name:"))
        form.add_widget(self.name_input)
        form.add_widget(Label(text="Age:"))
        form.add_widget(self.age_input)
        form.add_widget(Label(text="Gender:"))
        form.add_widget(self.gender_spinner)
        form.add_widget(Label(text="Class/Grade:"))
        form.add_widget(self.class_input)
        form.add_widget(Label(text="Address:"))
        form.add_widget(self.address_input)

        layout.add_widget(form)
        return layout

if __name__ == '__main__':
    StudentApp().run()
