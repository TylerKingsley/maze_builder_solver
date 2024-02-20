from cell import Cell
import random
import time

class Maze:
    def __init__(self ,x1 ,y1 , num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None, build_speed= 0.01, show_wrong_paths=True):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._build_speed = build_speed
        self._win = window
        self._seed = seed
        self._show_wrong_paths = show_wrong_paths
        if seed:
            random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j, self._build_speed)

    def _draw_cell(self, i, j, draw_speed=0.01):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(draw_speed)

    def _animate(self, speed=0.03):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(speed)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Get cell left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append([i-1, j])
            # Get right cell
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append([i+1, j])
            # Get top cell
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append([i, j-1])
            # Get bottom cell
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append([i, j+1])

            if len(to_visit) == 0:
                self._draw_cell(i,j,0.03)
                return
            
            random_num = random.randrange(len(to_visit))
            cell_to_visit = to_visit[random_num]

            # Left cell chosen  
            if cell_to_visit[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # Right cell chosen
            if cell_to_visit[0] == i+ 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # Top cell chosen
            if cell_to_visit[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[cell_to_visit[0]][cell_to_visit[1]].has_bottom_wall = False
            # Bottom cell chosen
            if cell_to_visit[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[cell_to_visit[0]][cell_to_visit[1]].has_top_wall = False

            self._break_walls_r(cell_to_visit[0],cell_to_visit[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        start_cell = self._cells[0][0].insert_start()
        result = self._solve_r(0, 0)
        end_cell = self._cells[self._num_cols-1][self._num_rows-1].insert_end()
        return result

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        possible_direc = []
        # Get cell left
        if not self._cells[i][j].has_left_wall and i > 0 and not self._cells[i-1][j].visited:
            possible_direc.append([i-1, j])
        # Get right cell
        if not self._cells[i][j].has_right_wall and i < self._num_cols-1 and not self._cells[i+1][j].visited:
            possible_direc.append([i+1, j])
        # Get top cell
        if not self._cells[i][j].has_top_wall and j > 0 and not self._cells[i][j-1].visited:
            possible_direc.append([i, j-1])
        # Get bottom cell
        if not self._cells[i][j].has_bottom_wall and j < self._num_rows-1 and not self._cells[i][j+1].visited:
            possible_direc.append([i, j+1])

        for direc in possible_direc:
            self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]],self._show_wrong_paths, False)
            solve_result = self._solve_r(direc[0],direc[1])
            if solve_result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[direc[0]][direc[1]], self._show_wrong_paths, True)