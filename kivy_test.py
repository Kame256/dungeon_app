import random
import random

# my_file---
#import
# kivy----
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.config import Config
# layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
# widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput

Builder.load_file('map_window.kv')
resource_add_path("./font")
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")


class Anko(BoxLayout):
    def __init__(self,**kwargs):
        super(Anko,self).__init__(**kwargs)




class Run(App):
    def __init__(self,**kwargs):
        super(Run,self).__init__(**kwargs)
    def build(self):
        mozi=Label(text="yeah")
        ankoo=Anko()
        ankoo.add_widget(mozi)

        return ankoo
Run().run()
