from tkinter import *
from turtle import Turtle

class Main:
    def __init__(self):
        window = Tk()
        window.title('Tic-Tac-Toe')

        frame = Frame(window)
        frame.pack()

        self.xImage = PhotoImage(file='image/x.gif')
        self.oImage = PhotoImage(file='image/o.gif')
        self.eImage = PhotoImage(file='image/empty.gif')
        self.matrix = []
        self.turn = True
        self.done = False

        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(Button(frame, image=self.eImage, text=' ',
                command= lambda row=i, col=j: self.pressed(row, col)))
                self.matrix[i][j].grid(row=i, column=j)
        
        self.explain = StringVar()
        self.explain.set('플레이어 X 차례')
        Label(window, textvariable=self.explain).pack()
        Button(window, text='다시 시작', command=self.refresh).pack()

        window.mainloop()

    def pressed(self, row, col):
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.xImage
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.oImage
                self.matrix[row][col]['text'] = 'O'

            self.turn = not self.turn

            if self.check() == '@':
                self.explain.set('비겼습니다.')
            elif self.check() != ' ':
                self.explain.set(self.check()+'가 이겼습니다.')
                self.done = True
            elif self.turn:
                self.explain.set('플레이어 X 차례')
            else:
                self.explain.set('플레이어 O 차례')

    
    def check(self):
        for i in range(3):
            ch = self.matrix[i][0]['text']
            if ch != ' ' and ch == self.matrix[i][1]['text'] and ch == self.matrix[i][2]['text']:
                return ch
            ch = self.matrix[0][i]['text']
            if ch != ' ' and ch == self.matrix[1][i]['text'] and ch == self.matrix[2][i]['text']:
                return ch
        
        ch = self.matrix[1][1]['text']
        if ch != ' ' and ch == self.matrix[0][0]['text'] and ch == self.matrix[2][2]['text']:
            return ch
        if ch != ' ' and ch == self.matrix[0][2]['text'] and ch == self.matrix[2][0]['text']:
            return ch
        
        flag = True
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j]['text'] == ' ':
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
        self.explain.set('플레이어 X 차례')
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.eImage
                self.matrix[i][j]['text'] = ' '
            
Main()