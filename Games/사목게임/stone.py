from tkinter import * # Import tkinter

class Cell(Canvas):
    def __init__(self, parent, row, col, width = 20, height = 20):
        Canvas.__init__(self, parent, width = width, height = height, \
        bg = "blue", borderwidth = 2)

        self.color = "white"
        self.row = row
        self.col = col

        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)

    def clicked(self, event): # red 또는 yellow 돌 놓기.
        nextcolor = "red" if self.color != "red" else "yellow"
        self.setColor(nextcolor)

    def setColor(self, color):
        self.delete("oval") 
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")

# Global Variables
_MAXROW = 6
_MAXCOL = 7

turn = "red"    # 다음 놓을 차례 (red, yellow, none(game over))
cells = []

process_button = None   # 하단의 버튼
restart_text = "새로 시작"



# loop
window = Tk() # Create a window
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()

cell = Cell(frame1, 0, 0, width = 20, height = 20)
cell.grid(row = 0, column = 0)

Button(window, text = restart_text).pack()  # restart button

window.mainloop() # Create an event loop