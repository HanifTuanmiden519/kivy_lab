import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class HelloApp(App):
   def build(self):
     f = FloatLayout()
     s = Scatter()
     l = Label(text='Hello!',
               font_size=150)
     f.add_widget(s)
     s.add_widget(l)
     return f
   
if __name__ == "__main__":
   HelloApp().run()
   
   
   
#class MyApp(App):
 #  def build(self):
  #   return Label(text='Hanif Tuanmiden', font_size='150sp')

#if __name__ == '__main__':
 #  MyApp().run()