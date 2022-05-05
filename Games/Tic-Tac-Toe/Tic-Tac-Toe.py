from tkinter import *

class Main:
    def __init__(self):
        window = Tk()
        window.title('Tic-Tac-Toe')

        frame = Frame(window)
        frame.pack()

        self.xImage = PhotoImage(file='image/x.gif')
        self.oImage = PhotoImage(file='image/o.gif')
        self.eImage = PhotoImage(file='image/empty.gif')

        self.cells = []     # 3x3 cell
        self.turn = True
        self.done = False

        for i in range(3):
            self.cells.append([])
            for j in range(3):
                self.cells[i].append(Button(frame, image = self.eImage, \
                text= ''))
                self.cells[i][j](row=i, column=j)

        self.explain = StringVar()
        self.explain.set('플레이어 X 차례')
        Label(window, textvariable=self.explain).pack()
        Button(window, text='다시 시작').pack()

        window.mainloop()

Main()