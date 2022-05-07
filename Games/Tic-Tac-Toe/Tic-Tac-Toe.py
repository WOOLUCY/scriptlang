from tkinter import *

class TicTacToe:
    def __init__(self):         # initiating window
        tk = Tk()

        frame = Frame(tk)
        frame.pack()
        
        # image load
        self.xImage = PhotoImage(file='image/x.gif')        # X image
        self.oImage = PhotoImage(file='image/o.gif')        # O image
        self.eImage = PhotoImage(file='image/empty.gif')    # empty image
        
        self.cells = []
        self.turn = True
        self.done = False

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
        if not self.done and self.cells[row][col]['text'] == ' ':
            if self.turn:
                self.cells[row][col]['image'] = self.xImage
                self.cells[row][col]['text'] = 'X'
            else:
                self.cells[row][col]['image'] = self.oImage
                self.cells[row][col]['text'] = 'O'

            self.turn = not self.turn

            if self.check() == '@':
                self.result.set('비김! 게임이 끝났습니다')
            elif self.check() != ' ':
                self.result.set(self.check()+' 승리! 게임이 끝났습니다')
                self.done = True
            elif self.turn:
                self.result.set('X 차례')
            else:
                self.result.set('O 차례')

    
    def check(self):
        for i in range(3):
            ch = self.cells[i][0]['text']
            if ch != ' ' and ch == self.cells[i][1]['text'] and ch == self.cells[i][2]['text']:
                return ch
            ch = self.cells[0][i]['text']
            if ch != ' ' and ch == self.cells[1][i]['text'] and ch == self.cells[2][i]['text']:
                return ch
        
        ch = self.cells[1][1]['text']
        if ch != ' ' and ch == self.cells[0][0]['text'] and ch == self.cells[2][2]['text']:
            return ch
        if ch != ' ' and ch == self.cells[0][2]['text'] and ch == self.cells[2][0]['text']:
            return ch
        
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

    def refresh(self):
        self.turn = True
        self.done = False
        self.result.set('X 차례')
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.eImage
                self.matrix[i][j]['text'] = ' '
            
TicTacToe()