from Window import Window
from shapes import Point, Line
from cells import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    # Create a maze 
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()