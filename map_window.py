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
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '650')
Config.write()

class Map_screen(BoxLayout):
    def __init__(self,**kwargs):
        super(Map_screen,self).__init__(**kwargs)
        pass
    def map_paint(self):

        return 1

class Room(Bottun):
    def __init__(self,**kwargs):
        super(Map_screen,self).__init__(**kwargs)
        pass


class Map_window(GridLayout):
    def __init__(self,**kwargs):
        super(Map_window,self).__init__(**kwargs)
        pass

class Item_window(BoxLayout):
    def __init__(self,**kwargs):
        super(Operation_move,self).__init__(**kwargs)
        pass

class Operation_move(GridLayout):
    def __init__(self,**kwargs):
        super(Operation_move,self).__init__(**kwargs)
        pass

class Operation_action(BoxLayout):
    def __init__(self,**kwargs):
        super(Operation_action,self).__init__(**kwargs)

        pass
class Map_mode(App):
    def __init__(self, **kwargs):
        super(Map_mode,self).__init__(**kwargs)
        self.title="map"

    def build(self):
        map_screen=Map_screen()
        return map_screen
if __name__=="__main__":
    Map_mode().run()
