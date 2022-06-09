import random

class Dice:
    def rollDie(self):
        self.roll = random.randint(1, 6)    # 1~6까지의 랜덤 숫자 나오게 함

    def getRoll(self):
        return self.roll
