from tkinter import *
from tkinter import font
from player import *
from dice import *
from configuration import *
from tkinter import messagebox

class YahtzeeBoard:
    # index들.
    UPPERTOTAL = 6  # "Upper Scores" 위치의 index.
    UPPERBONUS = 7  # "Upper Bonus(35)" 위치의 index.
    LOWERTOTAL = 15  # "Lower Scores" 위치의 index.
    TOTAL = 16  # "Total" 위치의 index.

    # 객체 리스트
    dice = []       # Dice() 객체의 리스트.
    diceButtons = [] # 각 주사위를 표현하는 Button 객체의 리스트.
    fields = []     # 각 플레이어별 점수판(카테고리). Button 객체의 2차원 리스트.
                    # 열: 플레이어 (0열=플레이어1, 1열=플레이어2,…)
                    # 17행: upper카테고리6행, upperScore, upperBonus, lower카테고리7행, LowerScore, Total
    players = []    # 플레이어 수 만큼의 Player 인스턴스를 가짐.
    numPlayers = 0  # # 플레이어 수
    player = 0      # players 리스트에서 현재 플레이어의 index.
    round = 0       # 13 라운드 중 몇번째인지 (0~12 사이의 값을 가짐)
    roll = 0        # 각 라운드에서 3번 중 몇번째 굴리기인지 (0~2 사이의 값을 가짐)
    # 색깔
    color_btn_bg = 'SystemButtonFace'

    def __init__(self):
        self.InitGame()

    def InitGame(self):     #player window 생성하고 최대 10명까지 플레이어 설정
        self.pwindow = Tk()
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append( Label(self.pwindow, text='플레이어 수', font=self.TempFont ) )
        self.label[0].grid(row=0, column=0)

        for i in range(1,11):
            self.label.append( Label(self.pwindow, text='플레이어'+str(i)+' 이름', font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text='Yahtzee 플레이어 설정 완료', font=self.TempFont, command=self.InitAllPlayers).grid(row=11, column=0)

        self.pwindow.mainloop()

    def InitAllPlayers(self):
        '''
        [플레이어 설정 완료 버튼 누르면 실행되는 함수]
        numPlayers를 결정하고 이 숫자에 따라 각 player에게 필요한 정보들을 초기화.
        기존 toplebel 윈도우를 닫고 Yahtzee 보드 윈도우 생성.
        '''
        self.numPlayers = int(self.entry[0].get())
        for i in range(1, self.numPlayers+1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()

        ##################################################       
        # Yahtzee 보드판: 플레이어 수 만큼 생성
        
        self.window = Tk('Yahtzee Game')
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')

        for i in range(5): #Dice 객체 5개 생성
            self.dice.append(Dice())

        self.rollDice = Button(self.window, text='Roll Dice', font=self.TempFont, command=self.rollDiceListener, bg=self.color_btn_bg)  # Roll Dice 버튼
        self.rollDice.grid(row=0, column=0)
        for i in range(5):  #dice 버튼 5개 생성
	        #각각의 dice 버튼에 대한 이벤트 처리 diceListener 연결
            #람다 함수를 이용하여 diceListener 매개변수 설정하면 하나의 Listener로 해결
            self.diceButtons.append(Button(self.window, text='?', font=self.TempFont, width=8, bg=self.color_btn_bg, command=lambda row=i: self.diceListener(row))) 
            self.diceButtons[i].grid(row=i + 1, column=0)
        
        for i in range(self.TOTAL + 2):  # i행 : 점수
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):  # j열 : 플레이어
                if (i == 0):  # 플레이어 이름 표시
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont).grid(row=i, column=2 + j)
                else:
                    if (j==0): #각 행마다 한번씩 리스트 추가, 다중 플레이어 지원
                        self.fields.append(list())
                    #i-1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변수 설정
                    self.fields[i-1].append(Button(self.window, text="", font=self.TempFont, width=8,
                        command=lambda row=i-1: self.categoryListener(row)))
                    self.fields[i-1][j].grid(row=i,column=2 + j)
                    # 누를 필요없는 버튼은 disable 시킴
                    if (j != self.player or (i-1) == self.UPPERTOTAL or (i-1) == self.UPPERBONUS 
                        or (i-1) == self.LOWERTOTAL or (i-1) == self.TOTAL):
                        self.fields[i-1][j]['state'] = 'disabled'
                        self.fields[i-1][j]['bg'] = 'light gray'
        
        #상태 메시지 출력
        self.bottomLabel=Label(self.window, text=self.players[self.player].toString()+
            "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0, columnspan=2)
        self.window.mainloop()

    # 주사위 굴리기 함수.
    def rollDiceListener(self):
        # 'state' 값이 'disabled'가 아닌 모든 주사위 값을 새로 할당하고 화면에 표시.
        # TODO: 구현

        # self.roll 이 0, 1 일 때 : 
        if (self.roll == 0 or self.roll ==1):
            self.roll += 1
            self.rollDice.configure(text="Roll Again")
            self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")
        elif (self.roll==2):
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = 'light gray'
            self.roll = 0

    # 각 주사위에 해당되는 버튼 클릭 : disable 시키고 배경색을 어둡게 바꿔 표현해 주기.
    def diceListener(self, row):
        self.diceButtons[row]['state'] = 'disabled'
        self.diceButtons[row]['bg'] = 'light gray'

    # 카레고리 버튼 눌렀을 때의 처리.
    #   row: 0~5, 8~14
    def categoryListener(self, row):
        score = Configuration.score(row, self.dice)      #점수 계산
        # index : 0~12
        index = row
        if (row>7):
            index = row-2
        cur_player = self.players[self.player]

        # 선택한 카테고리의 점수를 버튼에 적고 버튼을 disable 시킴.
        # TODO: 구현
        
        # UPPER category가 전부 사용되었으면 UpperScore, UpperBonus 계산
        # TODO: 구현

        # LOWER category 전부 사용되었으면 LowerScore 계산
        # TODO: 구현
            
        # UPPER category와 LOWER category가 전부 사용되었으면 TOTAL 계산
        # TODO: 구현

        # 다음 플레이어로 가기.
        self.player = (self.player + 1) % self.numPlayers

        # 선택할 수 없는 카테고리들과 현재 player 것이 아닌 버튼들은 disable 시키기.
        # TODO: 구현

        # 라운드 증가 시키기.
        if self.player == 0:
            self.round += 1

        # 게임이 종료되었는지 검사 -> 이긴 사람을 알리고 새 게임 시작.
        # TODO: 구현

        # 다시 Roll Dice 버튼과 diceButtons 버튼들을 활성화.
        self.rollDice.configure(text="Roll Dice")
        self.rollDice['state'] = 'normal'
        self.rollDice['bg'] = self.color_btn_bg
        for i in range(5):  #dice 버튼 5개 생성
            self.diceButtons[i].configure(text='')
            self.diceButtons[i]['state'] = 'normal'
            self.diceButtons[i]['bg'] = self.color_btn_bg

        # bottomLabel 초기화.
        self.bottomLabel.configure(text=cur_player.toString()+
            "차례: Roll Dice 버튼을 누르세요")

if __name__ == '__main__':
    YahtzeeBoard()
