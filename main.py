import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

import random

class slots(GridLayout):
    s1=ObjectProperty(None)
    s2=ObjectProperty(None)
    s3=ObjectProperty(None)
    c=ObjectProperty(None)
    r=ObjectProperty(None)
    def btn(self):
        if int(self.c.text[0])<=0:
            self.r.text='You have no Chips!'
        else:
            self.c.text=(str(int(self.c.text.split()[0])-1)+" chips")
            self.s1.text=str(random.randint(1,10))
            self.s2.text=str(random.randint(1,10))
            self.s3.text=str(random.randint(1,10))
            if self.s1.text==self.s2.text==self.s3.text==7:
                self.r.text="!!Nah I'd Win!!"
                self.c.text=(str(int(self.c.text.split()[0])+1000)+" chips")
            else:
                self.r.text='No Win'

class MyApp(App):
    def build(self):
        return slots()

MyApp().run()
