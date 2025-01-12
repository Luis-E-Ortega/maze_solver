from tkinter import Tk, BOTH, Canvas
from shapes import *

class Window:
    def __init__(self, width=0, height=0):
        #Create the root window
        self.__root = Tk()
        # Set the title
        self.__root.title("Maze solver")
        # Create canvas window
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        # Set close protocol (links the system's "X" to our close method)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # Running state
        self.__running = False

    def redraw(self):
        # Update and redraw the canvas
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


    def wait_for_close(self):
        # Set the running state to True and start the loop
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        # Stop the running loop
        self.__running = False
    