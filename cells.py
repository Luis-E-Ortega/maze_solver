from Window import *
from shapes import *

class Cell:
    def __init__(self, _win, _x1, _y1, _x2, _y2):
        # Window to draw itself on
        self._win = _win

        # Coordinates of the cell
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2

        # Has all walls by default
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def get_center(self):
        center_point = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        return center_point
    
    def draw(self):
        if self.has_left_wall:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_line, "black")
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line, "black")
        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line, "black")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line, "black")
    
    def draw_move(self, to_cell, undo=False):
        # Get the center point of starting cell and destination cell
        from_center = self.get_center()
        dest_center = to_cell.get_center()

        # Set the trajectory of the line based on the centers
        through_line = Line(from_center, dest_center)

        # Draw the line as red if undo is unset and gray if it is
        self._win.draw_line(through_line, fill_color="red" if not undo else "gray")

