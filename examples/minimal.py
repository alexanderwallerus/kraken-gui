import py5
import krakengui as ui

def hello():
    print('hello world')

def setup():
    py5.size(250, 250)
    ui.Button(label='simple button', pos=(20, 50), on_click=hello)

def draw():
    py5.background(0)

py5.run_sketch()