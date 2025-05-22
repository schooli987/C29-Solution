from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window

SYMPTOMS_LIST = ["Fever", "Cough", "Headache", "Fatigue"]

class PatientApp(App):
    def build(self):
    
        return self.build_form_screen()

    def build_form_screen(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        form = GridLayout(cols=2, spacing=10, row_force_default=True, row_default_height=40)

        self.name_input = TextInput()
        self.age_input = TextInput(input_filter='int')
        self.gender_spinner = Spinner(text='Select', values=['Male', 'Female', 'Other'])
        self.contact_input = TextInput()
        self.address_input = TextInput()

        form.add_widget(Label(text="Name:"))
        form.add_widget(self.name_input)
        form.add_widget(Label(text="Age:"))
        form.add_widget(self.age_input)
        form.add_widget(Label(text="Gender:"))
        form.add_widget(self.gender_spinner)
        form.add_widget(Label(text="Contact No:"))
        form.add_widget(self.contact_input)
        form.add_widget(Label(text="Address:"))
        form.add_widget(self.address_input)

        layout.add_widget(form)

        layout.add_widget(Label(text="Select Symptoms:", size_hint_y=None, height=30))

       
        for symptom in SYMPTOMS_LIST:
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, padding=(10, 0))
            cb = CheckBox()
            row.add_widget(cb)
            row.add_widget(Label(text=symptom))
          
            layout.add_widget(row)


        return layout
if __name__ == '__main__':
    PatientApp().run()
