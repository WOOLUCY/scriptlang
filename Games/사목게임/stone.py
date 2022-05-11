from tkinter import * 

class Main():
    def __init__(self):
        tk = Tk()
        tk.title('사목게임')

        frame = Frame(tk)
        frame.pack()

        self.matrix = []
        self.xImage = PhotoImage(file='image/x.gif')
        self.oImage = PhotoImage(file='image/o.gif')
        self.eImage = PhotoImage(file='image/empty.gif')

        self.turn = True
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame, text=' ', image=self.imageE))   # clicked 추가
                self.matrix[i][j].grid(row=i, column=j)
        
        Button(tk, text='새로 시작').pack() # refresh 추가

        tk.mainloop()

    def check():    # todo: 체크 함수 추가
        pass

    def refresh():  # todo: 새로 시작 함수 추가
        pass

    def clicked(self, row, col):  # todo: 눌렸을 시 함수 추가
        pass

Main()