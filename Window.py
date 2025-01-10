from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width=0, height=0):
        #Create the root window
        self.root = Tk()
        # Set the title
        self.root.title("Maze solver")
        # Create canvas window
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        
    def wait_for_close(self):
        self.root.mainloop()