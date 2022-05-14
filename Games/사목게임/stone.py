from tkinter import *
from tkinter.tix import COLUMN # Import tkinter

class Cell(Canvas):
    def __init__(self, parent, row, col, width = 20, height = 20):
        Canvas.__init__(self, parent, width = width, height = height, \
        bg = "blue", borderwidth = 2)

        self.color = "white"
        self.row = row
        self.col = col
        self.isEmpty = True

        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)

    def clicked(self, event): # red 또는 yellow 돌 놓기.
        if self.isEmpty:
            nextcolor = "red" if self.color != "red" else "yellow"
            self.setColor(nextcolor)
            self.isEmpty = False

    def setColor(self, color):
        self.delete("oval") 
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")

    def __checkVertical(self):  # 열 방향 확인
        pass

    def __Horizontal(self):     # 행 방향 확인
        pass

    def __checkDiag1(self):     # /방향 대각선 확인
        pass

    def __checkDiag2(self):     # \방향 대각선 확인
        pass

def restart():
    print("새로 시작")

# Global Variables
_MAXROW = 6
_MAXCOL = 7

turn = "red"    # 다음 놓을 차례 (red, yellow, none(game over))
cells = []

# loop
window = Tk() # Create a window
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()

# cell = Cell(frame1, 0, 0, width = 20, height = 20)
# cell.grid(row = 0, column = 0)

for i in range(6):
    cells.append([])
    for j in range(7):
        cells[i].append(Cell(frame1, i, j, width = 20, height = 20))
        cells[i][j].grid(row=i, column=j)

restart_text = "새로 시작"
process_button = Button(window, text = restart_text, command=restart).pack()  # restart button

window.mainloop() # Create an event loop