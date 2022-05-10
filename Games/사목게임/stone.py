from tkinter import * 

class Main():
    def __init__(self):
        tk = Tk()
        tk.title('사목게임')

        frame = Frame(tk)
        frame.pack()

        self.matrix = []
        self.imageX = PhotoImage(file='image/x.gif')
        self.imageO = PhotoImage(file='image/o.gif')
        self.imageE = PhotoImage(file='image/empty.gif')

        self.turn = True
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame, text=' ', image=self.imageE))   # clicked 추가
                self.matrix[i][j].grid(row=i, column=j)
        
        Button(tk, text='새로 시작').pack() # refresh 추가

        tk.mainloop()

Main()