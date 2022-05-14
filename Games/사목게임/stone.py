from tkinter import * # Import tkinter

class Cell(Label):
    def __init__(self, container):
        Label.__init__(self, container, image = _images[' '])
        self.bind("<Button-1>", self.flip)
        self.token = " "
      
    def flip(self, event):
        global currentToken, statusLabel
        if self.token == " " and currentToken != "Over":
            self.token = currentToken
            self["image"] = _images[self.token]
            currentToken = "X" if (currentToken == "O") else "O"
            statusLabel["text"] = currentToken+" 차례"
                
        checkStatus(self.token)

def checkStatus(token):
    global currentToken
    if isWon(token):
        statusLabel["text"] = token + " 승리! 게임이 끝났습니다"
        currentToken = "Over"
    elif isFull():
        statusLabel["text"] = "비김! 게임이 끝났습니다"
        currentToken = "Over"
        
# Determine whether the cells are all occupied 
def isFull():
    for i in range(3):
        for j in range(3):
            if cells[i][j].token == ' ':
                return False

    return True

# Determine whether the player with the specified token wins 
def isWon(token):
    for i in range(3):
        if cells[i][0].token == token and cells[i][1].token == token \
            and cells[i][2].token == token:
            return True

    for j in range(3):
      if cells[0][j].token == token and cells[1][j].token == token \
          and cells[2][j].token == token:
        return True

    if cells[0][0].token == token and cells[1][1].token == token \
        and cells[2][2].token == token:
      return True

    if cells[0][2].token == token and cells[1][1].token == token \
        and cells[2][0].token == token:
      return True

    return False

window = Tk() # Create a window
window.title("TicTacToe") # Set title

_images = {' ': None, 'X': None, 'O': None }
_images['X'] = PhotoImage(file = "image/x.gif")
_images['O'] = PhotoImage(file = "image/o.gif")
_images[' '] = PhotoImage(file = "image/empty.gif")

# 게임 진행 토큰 : 현재 차례에 따라 "X" 또는 "O"를 가지다가 게임이 끝나면 "Over"를 가짐.
currentToken = "X"
    
frame = Frame(window)
frame.pack()

cells = []
for i in range(3):
    cells.append([])
    for j in range(3):
        cells[i].append(Cell(frame))
        cells[i][j].grid(row = i, column = j)

statusLabel = Label(window, text = "Game status: continue")
statusLabel["text"] = currentToken+" 차례"
statusLabel.pack()

window.mainloop() # Create an event loop
