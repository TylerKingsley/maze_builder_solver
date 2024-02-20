from graphics import Line, Point

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = window

    def draw(self, x1 , y1, x2 , y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall_line = Line(Point(x1, y1), Point(x1, y2))
        top_wall_line = Line(Point(x1, y1), Point(x2, y1))
        right_wall_line = Line(Point(x2, y1), Point(x2, y2))
        bottom_wall_line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_left_wall:
            self._win.draw_line(left_wall_line)
        else:
            self._win.draw_line(left_wall_line, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall_line)
        else:
            self._win.draw_line(top_wall_line, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall_line)
        else:
            self._win.draw_line(right_wall_line, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall_line)
        else:
            self._win.draw_line(bottom_wall_line, "white")
        
    def draw_move(self, to_cell, show_wrong_paths=True, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2
        line_color = "red"
        if undo:
            if show_wrong_paths:
                line_color = "gray"
            else:
                line_color = "white"
        
        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, line_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, line_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, line_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, line_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, line_color)

    def insert_start(self):
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        line = Line(Point(x_mid, self._y1), Point(x_mid,y_mid))
        self._win.draw_line(line, "red")
    
    def insert_end(self):
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        line = Line(Point(x_mid, self._y2), Point(x_mid,y_mid))
        self._win.draw_line(line, "red")