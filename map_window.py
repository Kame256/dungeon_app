import random

# my_file---
import map_system
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

# オプション
Builder.load_file('map_window.kv')
resource_add_path("./font")
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '650')
#Config.set('modules', 'showborder','0')
Config.write()

#マップ画面
class Map_screen(BoxLayout):
    def __init__(self,**kwargs):
        super(Map_screen,self).__init__(**kwargs)
        pass
    def map_paint(self):

        return 1

class Floor(GridLayout):
    def __init__(self,**kwargs):
        super(Floor,self).__init__(**kwargs)
        color_list=[[[random.randint(0,1),random.randint(0,1),random.randint(0,1),1] for x in range(5)] for y in range(4)]
        self.sys_floor=map_system.Floor()
        self.room_list=self.sys_floor.room_list
        anko=1
        room_list=[[Room(text="hoge",background_color=color_list[y][x],anko=x) for x in range(5)] for y in range(4)]
        for x in room_list:
            for y in x:
                self.add_widget(y)



class Room(Button):

    def __init__(self,anko=5,**kwargs):
        super(Room,self).__init__(**kwargs)
        self.background_color=[1,0,0,1]
        self.text=str(anko)


        pass


class Map_window(GridLayout):
    def __init__(self,**kwargs):
        super(Map_window,self).__init__(**kwargs)
        pass

class Item_window(BoxLayout):
    def __init__(self,**kwargs):
        super(Operation_move,self).__init__(**kwargs)
        pass


# 操作画面
class Operation(GridLayout):
    def __init__(self,**kwargs):
        super(Operation,self).__init__(**kwargs)

class Operation_move(GridLayout):
    def __init__(self,**kwargs):
        super(Operation_move,self).__init__(**kwargs)
        pass

class Operation_action(BoxLayout):
    def __init__(self,**kwargs):
        super(Operation_action,self).__init__(**kwargs)

        pass

class Move_command(Button):
    def __init__(self,**kwargs):
        super(Move_command,self).__init__(**kwargs)

        pass

#アプリ-------
class Map_mode(App):
    def __init__(self, **kwargs):
        super(Map_mode,self).__init__(**kwargs)
        self.title="map"

    def build(self):
        map_screen=Map_screen()
        return map_screen
if __name__=="__main__":
    Map_mode().run()
