from Classes import create_recipe, recipe
import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('2.1.0')


cr = create_recipe.create_recipe
cr(recipe.Recipe)


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()

