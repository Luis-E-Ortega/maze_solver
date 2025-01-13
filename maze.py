import time
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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win # Window used for maze

        self._cells = []
        self._create_cells()

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
                # Draw the cell after its been added
                self._draw_cell(i, j)
            self._cells.append(column)

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