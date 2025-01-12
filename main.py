from Window import Window
from shapes import Point, Line
from cells import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win, 50, 50, 100, 100)
    c1.has_right_wall = False
    c1.draw()

    c2 = Cell(win, 100, 50, 150, 100)
    c2.has_left_wall = False
    c2.has_right_wall = False
    c2.draw()

    c3 = Cell(win, 150, 50, 200, 100)
    c3.has_left_wall = False
    c3.has_bottom_wall = False
    c3.draw()

    c4 = Cell(win, 150, 100, 200, 150)
    c4.has_top_wall = False
    c4.has_right_wall = False
    c4.draw()

    c5 = Cell(win, 200, 100, 250, 150)
    c5.has_left_wall = False
    c5.draw()
    
    c1.draw_move(c2)
    c2.draw_move(c3)
    c3.draw_move(c4)
    c4.draw_move(c5)

    c5.draw_move(c4, undo=True)

    

    win.wait_for_close()

if __name__ == "__main__":
    main()