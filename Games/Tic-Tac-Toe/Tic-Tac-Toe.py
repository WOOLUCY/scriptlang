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

        window.mainloop()

Main()