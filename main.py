import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.1.0')
Window.size = (425, 560)


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def calc_symbol(self, symbol):
        if symbol == '.' and '.' in self.calc_field.text:
            return
        if self.calc_field.text == "0":
            self.calc_field.text = symbol
        else:
            self.calc_field.text += symbol

    def delete(self):
        self.calc_field.text = self.calc_field.text[:-1]

    def clear(self):
        self.calc_field.text = ""

    def positive_negative(self):
        prev_number = self.calc_field.text
        if "-" in prev_number:
            self.calc_field.text = f"{prev_number.replace('-', '')}"
        else:
            self.calc_field.text = f"-{prev_number}"

    def square(self):
        try:
            x = float(self.calc_field.text)
            self.calc_field.text = str(x**2)
        except ValueError:
            self.calc_field.text = "Error: Invalid input."

    def get_result(self):
        try:
            self.calc_field.text = str(eval(self.calc_field.text))
        except ZeroDivisionError:
            self.calc_field.text = "Error: Can't divide by zero."
        except SyntaxError:
            self.calc_field.text = "Error: Invalid syntax."


class KivyCalc(App):

    def build(self):
        return MyRoot()


kivycalc = KivyCalc()
kivycalc.run()
