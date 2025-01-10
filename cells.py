from Window import *
from shapes import *

class Cell:
    def __init__(self, _win, _x1, _x2, _y1, _y2):
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
    
    def draw(self):
        if self.has_left_wall:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            left_line.draw(self._win)
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            right_line.draw(self._win)
        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            top_line.draw(self._win)
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            bottom_line.draw(self._win)