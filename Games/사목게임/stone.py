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

        self.create_oval(7, 7, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)
    
    def getEmpty(self):
        return self.isEmpty

    def clicked(self, event): # red 또는 yellow 돌 놓기.
        global turn, cells, done, process_button
        if not done:
            if self.isEmpty and (self.row == 5 or not cells[self.row + 1][self.col].getEmpty()):
                nextcolor = turn
                self.setColor(nextcolor)
                self.isEmpty = False
                
                if turn == "red":
                    turn = "yellow"
                elif turn == "yellow":
                    turn = "red"    

            if self.check():
                if turn == "red":
                    process_button["text"] = yellow_text
                else: 
                    process_button["text"] = red_text
                done = True

    def setColor(self, color):
        self.delete("oval") 
        self.color = color
        self.create_oval(7, 7, 20, 20, fill = self.color, tags="oval")

    def setBG(self, color):
        self.configure(bg = color)

    def check(self):        # check and change background color
        for i in range(6):
            for j in range(4):
                if cells[i][j].color != 'white' and\
                    cells[i][j].color == cells[i][j+1].color and\
                    cells[i][j].color == cells[i][j+2].color and\
                    cells[i][j].color == cells[i][j+3].color:
                    cells[i][j].setBG(self.color)
                    cells[i][j+1].setBG(self.color)
                    cells[i][j+2].setBG(self.color)
                    cells[i][j+3].setBG(self.color)
                    return True

        for i in range(3):
            for j in range(7):
                if cells[i][j].color != 'white' and\
                    cells[i][j].color == cells[i+1][j].color and\
                    cells[i][j].color == cells[i+2][j].color and\
                    cells[i][j].color == cells[i+3][j].color:
                    cells[i][j].setBG(self.color)
                    cells[i+1][j].setBG(self.color)
                    cells[i+2][j].setBG(self.color)
                    cells[i+3][j].setBG(self.color)
                    return True

        for i in range(3):
            for j in range(4):
                if cells[i][j].color != 'white' and\
                    cells[i][j].color == cells[i+1][j+1].color and\
                    cells[i][j].color == cells[i+2][j+2].color and\
                    cells[i][j].color == cells[i+3][j+3].color:
                    cells[i][j].setBG(self.color)
                    cells[i+1][j+1].setBG(self.color)
                    cells[i+2][j+2].setBG(self.color)
                    cells[i+3][j+3].setBG(self.color)
                    return True

        for i in range(3):
            for j in range(3, 7):
                if cells[i][j].color != 'white' and\
                    cells[i][j].color == cells[i+1][j-1].color and\
                    cells[i][j].color == cells[i+2][j-2].color and\
                    cells[i][j].color == cells[i+3][j-3].color:
                    cells[i][j].setBG(self.color)
                    cells[i+1][j-1].setBG(self.color)
                    cells[i+2][j-2].setBG(self.color)
                    cells[i+3][j-3].setBG(self.color)
                    return True

        # check draw
        dFlag = True
        for i in range(_MAXROW):
            for j in range(_MAXCOL):
                if cells[i][j].isEmpty:
                    dFlag = False
                    break
            if dFlag == False:
                break
        if dFlag:
            process_button["text"] = draw_text

def restart():
    global turn, done
    for i in range(_MAXROW):
        for j in range(_MAXCOL):
            cells[i][j].setColor("white")
            cells[i][j].isEmpty = True
            cells[i][j].setBG("blue")
            
    turn = "red"
    done = False
    process_button["text"] = restart_text




# Global Variables
_MAXROW = 6
_MAXCOL = 7

turn = "red"    # 다음 놓을 차례 (red, yellow, none(game over))
cells = []
done = False    # flag for game over

# loop
window = Tk() # Create a window
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()

# cell = Cell(frame1, 0, 0, width = 20, height = 20)
# cell.grid(row = 0, column = 0)

for i in range(_MAXROW):
    cells.append([])
    for j in range(_MAXCOL):
        cells[i].append(Cell(frame1, i, j, width = 20, height = 20))
        cells[i][j].grid(row=i, column=j)


restart_text = "새로 시작"
red_text = "red 승리!"
yellow_text = "yellow 승리!"
draw_text = "승자가 없습니다"

process_button = Button(window, text = restart_text, command=restart)
process_button.pack()

window.mainloop() # Create an event loop