from tkinter import Tk, BOTH, Canvas, Button, OptionMenu

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("MAZE SOLVER")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width,height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_running = False
        self.height = height
        self.width = width
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
        
    def draw_line(self, line_class, fill_color="black"):
        line_class.draw(self.__canvas, fill_color)

    def return_canvas(self):
        return self.__canvas

    def create_widget_window(self, x, y, height, width, widget):
        widget.config(bg="White")
        self.__canvas.create_window(x ,y , height=height, width=width, window=widget)

    def clear_canvas(self):
        self.__canvas.delete("all")

    def close(self):
        self.__window_running = False

class Point():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def __eq__(self, other):
        return self.point_1 == other.point_1 and self.point_2 == other.point_2

    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y , fill=fill_colour, width = 2
        )