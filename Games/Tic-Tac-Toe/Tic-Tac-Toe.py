from tkinter import *

class TicTacToe:
    def __init__(self):         # initiating window
        # frame
        tk = Tk()
        frame = Frame(tk)
        frame.pack()

        # variables
        self.cells = []
        self.turn = True    # true: X, false: O
        self.isDone = False
        
        # image load
        self.xImage = PhotoImage(file='image/x.gif')        # X image
        self.oImage = PhotoImage(file='image/o.gif')        # O image
        self.eImage = PhotoImage(file='image/empty.gif')    # empty image

        # cells
        for i in range(3):
            self.cells.append([])
            for j in range(3):
                self.cells[i].append(Button(frame, image=self.eImage, text=' ', command= lambda row=i, col=j: self.pressed(row, col)))
                self.cells[i][j].grid(row=i, column=j)
        
        # result
        self.result = StringVar()
        self.result.set('X 차례')
        Label(tk, textvariable=self.result).pack()

        tk.mainloop()

    def pressed(self, row, col):
        if not self.isDone and self.cells[row][col]['text'] == ' ':     # empty
            if self.turn:   # X
                self.cells[row][col]['image'] = self.xImage
                self.cells[row][col]['text'] = 'X'
            else:           # O
                self.cells[row][col]['image'] = self.oImage
                self.cells[row][col]['text'] = 'O'

            self.turn = not self.turn

            if self.check() == '@':
                self.result.set('비김! 게임이 끝났습니다')
            elif self.check() != ' ':
                self.result.set(self.check()+' 승리! 게임이 끝났습니다')
                self.isDone = True
            elif self.turn:
                self.result.set('X 차례')
            else:
                self.result.set('O 차례')

    
    def check(self):
        for i in range(3):
            cell = self.cells[i][0]['text']
            if cell != ' ' and cell == self.cells[i][1]['text'] and cell == self.cells[i][2]['text']:
                return cell
            cell = self.cells[0][i]['text']
            if cell != ' ' and cell == self.cells[1][i]['text'] and cell == self.cells[2][i]['text']:
                return cell
        
        cell = self.cells[1][1]['text']
        if cell != ' ' and cell == self.cells[0][0]['text'] and cell == self.cells[2][2]['text']:
            return cell
        if cell != ' ' and cell == self.cells[0][2]['text'] and cell == self.cells[2][0]['text']:
            return cell
        
        flag = True
        for i in range(3):
            for j in range(3):
                if self.cells[i][j]['text'] == ' ':
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            return '@'

        return ' '
            
TicTacToe()