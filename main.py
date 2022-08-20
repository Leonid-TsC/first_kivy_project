#This is education project. Thanks to Oleg Shpagin for his lessons on Youtube https://www.youtube.com/watch?v=fmkX_3ynHsc
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="This is education project. Thanks to Oleg Shpagin for his lessons on Youtube https://www.youtube.com/watch?v=fmkX_3ynHsc", halign="center")


if __name__ == '__main__':
    MainApp().run()