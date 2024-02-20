from graphics import Window
from maze import Maze
from interface import ButtonInstance, DropDownMenu, Slider, LabelBox

def main():
    def start_maze():
        num_cols = int(column_slider.get_value())
        num_rows = int(row_slider.get_value())
        win.clear_canvas()
        close_btn.create()
        reset_btn = ButtonInstance(win, "♻️", 40,40, 40,40,15,home_screen)
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        show_wrong_path = dd.get_value() == "Yes"
        print(f"SHOW_WRONG_PATH: {show_wrong_path}")
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, None, 0.01, show_wrong_path)
        maze.solve() 
    
    def home_screen():
        win.clear_canvas()
        close_btn.create()
        btn.create()
        label.create()
        dd.create()
        label1.create()
        column_slider.create()
        label2.create()
        row_slider.create()
    
    margin = 75
    screen_x = 1200
    screen_y = 900
    win = Window(screen_x, screen_y)
    position_x = screen_x/2
    position_y = screen_y/2
    close_btn = ButtonInstance(win, "❌",screen_x-40,40,40,40,15,win.close)
    btn = ButtonInstance(win, "Start Maze", position_x, position_y-130, 100, 250, 30 , start_maze)
    label = LabelBox(win, position_x, position_y-55, 15, 200, "SHOW ALL ROUTES TRAVELLED")
    dd = DropDownMenu(win, position_x, position_y-20,50,200, ["Yes", "No"])
    label1 = LabelBox(win, position_x, position_y+10, 15, 200, "SELECT NUMBER OF ROW")
    row_slider = Slider(win, position_x, position_y+60, 75, 230, 2, 20, "horizontal")
    label2 = LabelBox(win, position_x, position_y+80, 15, 200, "SELECT NUMBER OF COLUMN")
    column_slider = Slider(win, position_x, position_y + 130, 75, 230, 2, 20, "horizontal")
    
    win.wait_for_close()

main()