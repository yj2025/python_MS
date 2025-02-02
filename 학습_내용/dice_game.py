# 주사위 게임
# 1번 참가자 이름 입력
# 2번 참가자 이름 입력
# first = input('참가자1 이름 입력 : ')
# second = input('참가자2 이름 입력 : ')

# n1 = random.randint(1,6)
# n2 = random.randint(1,6)

# print(f'{first} : {n1}')
# print(f'{second} : {n2}')
# if n1 > n2:
#   print(f'{first} 승리')
# elif n1 < n2:
#   print(f'{second} 승리')
# else:
#   print('무승부')

import random
from ast import Try

class DiceGame:
    def __init__(self):
        while True:
            try:
                self.first = input('참가자1 이름 입력 : ')
                self.second = input('참가자2 이름 입력 : ')

            except:
                print('입력이 잘못되었습니다.')
            break

    def run(self):
        n1 = random.randint(1,6)
        n2 = random.randint(1,6)
        print(f'{self.first} 주사위 숫자는 : {n1}')
        print(f'{self.second} 주사위 숫자는 : {n2}')
        if n1 > n2:
            print(f'{self.first}가 이겼습니다.')
        elif n1 < n2:
            print(f'{self.second}가 이겼습니다.')
        else:
            print('무승부입니다.')

dice_game = DiceGame()
dice_game.run()