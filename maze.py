import time, random
from cells import *


class Maze:
    # Creates a maze using a 2D grid of cells
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win # Window used for maze
        self.seed = seed
        if seed is not None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit() # Break opening and closing walls
        self._break_walls_r(0, 0) # Break walls starting at top-left corner (0, 0)
        self._reset_cells_visited() # Reset the visited flag after using them to break walls for maze creation

    def _create_cells(self):
        # Iterate through all columns in maze and make a list for them
        for i in range(self.num_cols):
            column = []
            # Iterate through all rows in maze 
            for j in range(self.num_rows):
                # Calculate positions for cells
                start_x = self.x1 + (i * self.cell_size_x)
                start_y = self.y1 + (j * self.cell_size_y)
                end_x = start_x + self.cell_size_x
                end_y = start_y + self.cell_size_y

                # Create cells and add them to columns list for 2d array
                cell = Cell(start_x, start_y, end_x, end_y, self.win)
                column.append(cell)
            self._cells.append(column)

        # Draw all of the cells after they've been added to the list
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        # Implementation to draw cell at the stored location
        cell = self._cells[i][j]
        cell.draw()
        # Animate maze to see changes in real time
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        last_row = self.num_rows - 1
        last_col = self.num_cols - 1

        # Remove top wall of starting cell
        self._cells[0][0].has_top_wall = False
        # Draw the updated cell
        self._draw_cell(0,0)
            
        # Remove bottom wall of ending cell
        self._cells[last_col][last_row].has_bottom_wall = False
        # Draw the updated cell
        self._draw_cell(last_col, last_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            unvisited = []

            # Top
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                unvisited.append((i, j-1))

            # Bottom
            if j+1 < self.num_rows and not self._cells[i][j+1].visited:
                unvisited.append((i, j+1))

            # Right
            if i+1 < self.num_cols and not self._cells[i+1][j].visited:
                unvisited.append((i+1, j))
            
            # Left
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                unvisited.append((i-1, j))
            
            # If there is nowhere adjacent left to visit, simply draw the current cell and return
            if not unvisited:
                self._draw_cell(i, j)
                return
            # Randomly select which direction to go in from unvisited cells list
            selected_cell = random.choice(unvisited)
            
            # Conditionals to "knock down" appropriate walls for navigation to selected cell
            if selected_cell == (i, j-1): # Top
                self._cells[i][j].has_top_wall = False
                self._cells[selected_cell[0]][selected_cell[1]].has_bottom_wall = False
            elif selected_cell == (i, j+1): #Bottom
                self._cells[i][j].has_bottom_wall = False
                self._cells[selected_cell[0]][selected_cell[1]].has_top_wall = False
            elif selected_cell == (i+1, j): # Right
                self._cells[i][j].has_right_wall = False
                self._cells[selected_cell[0]][selected_cell[1]].has_left_wall = False
            elif selected_cell == (i-1, j): # Left
                self._cells[i][j].has_left_wall = False
                self._cells[selected_cell[0]][selected_cell[1]].has_right_wall = False
            self._break_walls_r(selected_cell[0], selected_cell[1])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, i, j):
        self._animate()

        # For last cell reference
        last_row = self.num_rows - 1
        last_col = self.num_cols - 1

        # Mark the current cell as visited
        self._cells[i][j].visited = True
        # If the current cell is the last cell, we've solved the maze
        if self._cells[i][j] == self._cells[last_col][last_row]:
            return True
        
        # Conditionals for navigation to cells

        # Top
        if j-1 >= 0:
            top_cell = self._cells[i][j-1]
            if not top_cell.has_bottom_wall and not top_cell.visited:
                self._cells[i][j].draw_move(top_cell)
                if self._solve_r(i, j-1):
                    return True
                self._cells[i][j].draw_move(top_cell, undo=True)
        # Bottom
        if j + 1 < self.num_rows:
            bottom_cell = self._cells[i][j+1]
            if not bottom_cell.has_top_wall and not bottom_cell.visited:
                self._cells[i][j].draw_move(bottom_cell)
                if self._solve_r(i, j + 1):
                    return True
                self._cells[i][j].draw_move(bottom_cell, undo=True)
        # Right
        if i + 1 < self.num_cols:
            right_cell = self._cells[i+1][j]
            if not right_cell.has_left_wall and not right_cell.visited:
                self._cells[i][j].draw_move(right_cell)
                if self._solve_r(i + 1, j):
                    return True
                self._cells[i][j].draw_move(right_cell, undo=True)
        # Left
        if i - 1 >= 0:
            left_cell = self._cells[i-1][j]
            if not left_cell.has_right_wall and not left_cell.visited:
                self._cells[i][j].draw_move(left_cell)
                if self._solve_r(i - 1, j):
                    return True
                self._cells[i][j].draw_move(left_cell, undo=True)
        return False
        






