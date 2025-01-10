from Window import Window
from shapes import Point, Line

def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(300, 300)

    my_line = Line(point1, point2)

    win.draw_line(my_line, "green")

    win.wait_for_close()

if __name__ == "__main__":
    main()