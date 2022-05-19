import math
from tkinter import *   # Import tkinter
import random
from tkinter import font

class Hangman:
    def __init__(self):
        # Initialize words, get the words from a file
        infile = open('hangman.txt', 'r')
        # 텍스트 파일은 https://github.com/Xethron/Hangman/blob/master/words.txt 참고
        self.words = infile.read().split()

        window = Tk()           # Create a window
        window.title('행맨')    # Set a title

        # 선, 다각형, 원등을 그리기 위한 캔버스를 생성
        self.canvas = Canvas(window, bg='white', width=400, height=280)
        self.canvas.pack()

        self.selectWord()
        self.draw()
        self.canvas.bind('<Key>', self.processKeyEvent)
        # key 입력 받기 위해 canvas가 focus 가지도록 함.
        self.canvas.focus_set()

        window.mainloop() # Create an event loop

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        self.canvas.delete('hangman')
        self.font = font.Font(family="굴림체", size=11)

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        self.canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        self.canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        self.canvas.create_line(60, 20, 160, 20, tags = "hangman")  # Draw the hanger

        # text rendering
        # todo: 행맨이랑 안 겹치게 텍스트 위치 조절하기
        if self.dFlag:      # 패배 시
            self.canvas.create_text(200, 230, text='정답: '+self.answer, tags='hangman', font=self.font)
            self.canvas.create_text(200, 245, text='계속하려면 ENTER', tags='hangman', font=self.font)
 
        elif self.vFlag:    # 승리 시
            self.canvas.create_text(200, 230, text=self.answer+' 맞았습니다', tags='hangman', font=self.font)
            self.canvas.create_text(200, 245, text='계속하려면 ENTER', tags='hangman', font=self.font)
        
        else:   # in progress
            self.canvas.create_text(200, 230, text='단어 추측: '+self.toString(self.input), tags='hangman', font=self.font) 
            if self.missNum > 0:
                self.canvas.create_text(200, 245, text='틀린 글자: '+self.toString(self.missChars), tags='hangman', font=self.font)
        
        if self.isIncluded:
            self.canvas.create_text(200, 260, text=self.key+'는 이전에 입력되었습니다.', tags='hangman', font=self.font)
            self.isIncluded = False

        # draw hangman
        # 1. Draw the hanger
        if self.missNum < 1:
            return
        self.canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        if self.missNum < 2:
            return            
        # 2. Draw the circle
        self.canvas.create_oval(140, 40, 180, 80, tags = "hangman") 

        radius = 20 # 반지름

        if self.missNum < 3:
            return
        # 3. Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
        x1 = 160 - radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 - (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))

        self.canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.missNum < 4:
            return
        # 4. Draw the right arm
        x1 = 160 + radius * math.cos(math.radians(45))
        y1 = 60 + radius * math.sin(math.radians(45))
        x2 = 160 + (radius+60) * math.cos(math.radians(45))
        y2 = 60 + (radius+60) * math.sin(math.radians(45))

        self.canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.missNum < 5:
            return
        # 5. Draw the body
        x1, y1 = 160, 80
        x2, y2 = 160, 140
        self.canvas.create_line(x1, y1, x2, y2, tags = "hangman")   

        if self.missNum < 6:
            return
        # 6. Draw the left leg
        x1 = 160 - radius * math.cos(math.radians(45)) + 14
        y1 = 140 + radius * math.sin(math.radians(45)) - 14
        x2 = 160 - (radius+60) * math.cos(math.radians(45)) + 14
        y2 = 140 + (radius+60) * math.sin(math.radians(45)) - 14

        self.canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.missNum < 7:
            return
        # 7. Draw the right arm
        x1 = 160 + radius * math.cos(math.radians(45)) - 14
        y1 = 140 + radius * math.sin(math.radians(45)) - 14
        x2 = 160 + (radius+60) * math.cos(math.radians(45)) - 14
        y2 = 140 + (radius+60) * math.sin(math.radians(45)) - 14

        self.canvas.create_line(x1, y1, x2, y2, tags = "hangman")
        self.canvas.configure(bg = 'red')
    
    def toString(self, wordList):
        result = ''
        for ch in wordList:
            result += ch
        return result

    def selectWord(self): 
        index = random.randint(0, len(self.words)-1)
        self.answer = self.words[index]
        self.input = ['*'] * len(self.answer)

        self.correctNum = 0
        self.missNum = 0
        self.missChars = []

        self.dFlag = False
        self.vFlag = False

        self.isIncluded = False
        self.key = None
    
    def processKeyEvent(self, Key):
        if 'a' <= Key.char <= 'z':  # 문자 입력 처리
            if Key.char in self.input or Key.char in self.missChars: 
            # 이전에 글자를 다시 입력 
                print("이전에 입력했던 글자를 다시 입력했습니다.")  
                self.isIncluded = True
                self.key = Key.char         
            elif Key.char not in self.answer:    
            # 틀린 글자
                self.missNum += 1
                if not Key.char in self.missChars:
                    self.missChars.append(Key.char)
                if self.missNum == 7:
                    self.dFlag = True
            else:   # 맞는 글자
                for i in range(len(self.answer)):
                    if self.answer[i] == Key.char:
                        self.input[i] = Key.char
                        self.correctNum += 1
                if self.correctNum == len(self.answer):
                    self.vFlag = True

        elif Key.keycode == 13:     # 엔터 쳤을 때 처리 reset
            if self.vFlag or self.dFlag:
                self.vFlag = False
                self.dFlag = False
                self.correctNum = 0
                self.missNum = 0
                self.selectWord()
                self.canvas.configure(bg='white')
        
        self.draw()

Hangman()