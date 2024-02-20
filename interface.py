from tkinter import Button, OptionMenu, Scale, DoubleVar, StringVar, Label, font

class ButtonInstance():
    def __init__(self, win:object, input_text:str, x:int, y:int, height:int, width:int, font_size:int, action):
        self._win = win
        self._active_canvas = self._win.return_canvas()
        self.input_text = input_text
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.action = action
        self.font_size = font_size
        
        self.create()
    
    def create(self):
        btn = Button(self._active_canvas, text=self.input_text, command=self.action, bg="White", highlightbackground="white")
        btn['font'] = font.Font(size=self.font_size)
        self._win.create_widget_window(self.x, self.y, self.height, self.width, btn)

class DropDownMenu():
    def __init__(self, win:object, x:int, y:int, height:int, width:int, options:list):
        self._win = win
        self._active_canvas = self._win.return_canvas()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.options = options
        self.var = StringVar()

        self.create()

    def create(self):
        self.var.set(self.options[0])
        dd = OptionMenu(self._active_canvas, self.var, *self.options )
        self._win.create_widget_window(self.x, self.y, self.height, self.width, dd)

    def get_value(self):
        return self.var.get()

class Slider():
    def __init__(self, win:object, x:int, y:int, height:int, width:int, begin:int, end:int, orient:str):
        self._win = win
        self._active_canvas = self._win.return_canvas()
        self.begin = begin
        self.end = end
        self.orient = orient
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.var = DoubleVar()

        self.create()

    def create(self):
        slider = Scale(self._active_canvas, from_=self.begin, to=self.end, orient=self.orient,  variable=self.var)
        self._win.create_widget_window(self.x, self.y, self.height, self.width, slider)

    def get_value(self):
        return self.var.get()
    
class LabelBox():
    def __init__(self, win:object, x:int, y:int, height:str, width:str, input_text:str):
        self._win = win
        self._active_canvas = self._win.return_canvas()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = input_text

        self.create()

    def create(self):
        text_box = Label(self._active_canvas, bg="white", text= self.text)
        self._win.create_widget_window(self.x, self.y, self.height, self.width, text_box)