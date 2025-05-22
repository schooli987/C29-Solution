from kivy.app import App
from kivy.uix.label import Label

class StudentApp(App):
    def build(self):
        return Label(text="Welcome to Student App!")

if __name__ == '__main__':
    StudentApp().run()
