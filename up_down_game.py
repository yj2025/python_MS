import random

class UpDownGame:
    n = 0

    def __init__(self):
        self.player = 0
        self.cp = 0
        self.get_create_num()

    def get_create_num(self):
        while True:
            try:
                self.player = int(input("1~100 숫자를 입력하세요: "))
                if 1 <= self.player <= 100:
                    self.cp = random.randint(1, 100)
                    break
                else:
                    print("입력 범위는 1부터 100까지입니다. 다시 입력하세요.")

            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력하세요.")

    def run(self):
        while True:
            if self.cp > self.player:
                print("UP")
                self.get_create_num()
            elif self.cp < self.player:
                print("DOWN")
                self.get_create_num()
            else:
                print("정답입니다.")
                break

            self.n += 1
            if self.n >= 9:
                print('실패')
                break

game = UpDownGame()
game.run()
