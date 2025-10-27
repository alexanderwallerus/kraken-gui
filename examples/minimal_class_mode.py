from py5 import Sketch
import py5gui as ui

def hello():
    print('hello world')

class My_Sketch(Sketch):
    def settings(self):
        self.size(250, 250)

    def setup(self):
        ui.Button(label='simple button', pos=(20, 50), on_click=hello)

    def draw(self):
        self.background(0)

my_sketch = My_Sketch()

my_sketch.run_sketch()