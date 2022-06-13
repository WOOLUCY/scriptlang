from dice import *

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        # TODO: 구현
        if (row >=0 and row <= 6): # Ones ~ Upper Scores
            return Configuration.scoreUpper(dices, row+1)
        elif (row == 8): # Three of a kind
            if Configuration.scoreThreeOfAKind(dices) == None:
                return 0
            return Configuration.scoreThreeOfAKind(dices)
        elif (row == 9): # Four of a kind
            if Configuration.scoreFourOfAKind(dices) == None:
                return 0
            return Configuration.scoreFourOfAKind(dices)
        elif (row == 10): # Full House(25)
            return Configuration.scoreFullHouse(dices)
        elif (row == 11): # Small Straight(30)
            return Configuration.scoreSmallStraight(dices)
        elif (row == 12): # Large Straight(40)
            return Configuration.scoreLargeStraight(dices)
        elif (row == 13): # Yahtzee(50)
            return Configuration.scoreYahtzee(dices)
        elif (row == 14): # Chance
            return Configuration.sumDie(dices)
        else:
            return -1

    def scoreUpper(dices, num):
        sum = 0
        for i in range(5):
            if(dices[i].getRoll() == num):
                sum += num
        return sum

    def scoreThreeOfAKind(dices):
        dices.sort(key=lambda i : i.getRoll())
        for i in range(3):
            if dices[i].getRoll() == dices[i+1].getRoll() and dices[i].getRoll() == dices[i+2].getRoll():
                return Configuration.sumDie(dices)

    def scoreFourOfAKind(dices):
        dices.sort(key=lambda i : i.getRoll())
        for i in range(2):
            if dices[i].getRoll() == dices[i+1].getRoll() and dices[i].getRoll() == dices[i+2].getRoll() and dices[i].getRoll() == dices[i+3].getRoll():
                return Configuration.sumDie(dices)


    def scoreFullHouse(dices):
        dices.sort(key=lambda i : i.getRoll())
        if dices[0].getRoll() == dices[1].getRoll() and\
            dices[2].getRoll() == dices[3].getRoll() and dices[2].getRoll() == dices[4].getRoll():
            return 25
        elif dices[0].getRoll() == dices[1].getRoll() and dices[0].getRoll() == dices[2].getRoll() and\
                dices[3].getRoll() == dices[4].getRoll():
            return 25
        else: return 0

    def scoreSmallStraight(dices):
        # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
        # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
        dices.sort(key=lambda i : i.getRoll())
        NotSame = True
        times = 0
        for i in range(4):
            if dices[i].getRoll()+1 == dices[i+1].getRoll():
                times += 1
            elif dices[i].getRoll() == dices[i+1].getRoll():
                if NotSame:
                    NotSame = False
                else:
                    return 0
        if times >= 3:
            return 30
        else:
            return 0

    def scoreLargeStraight(dices):
        # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        dices.sort(key=lambda i : i.getRoll())
        for i in range(4):
            if dices[i].getRoll()+1 != dices[i+1].getRoll():
                return 0
        return 40

    def scoreYahtzee(dices):
        for i in range(5):
            if dices[i].getRoll() != dices[0].getRoll():
                return 0
        return 50

    def sumDie(dices):
        sum = 0
        for i in range(5):
            sum += dices[i].getRoll()
        return sum