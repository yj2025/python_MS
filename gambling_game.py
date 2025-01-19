import random

class Person:
    def __init__(self, name):
        self.name = name
        self.list_numbers = []

    def set_list_numbers(self):
        input(self.name + "의 turn. <Press the Enter Key> ")
        self.list_numbers = [random.randint(1, 3) for i in range(3)]
        print(self.name + "의 숫자 : " + str(self.list_numbers) + "입니다.")
        # self.list_numbers가 리스트이기 떄문에 문자열과 결합할 때 str로 변환해줘야 함

    def get_list_numbers(self):
        return self.list_numbers

while True:
    try:
        player1_name = input("첫 번째 사람의 이름을 입력하세요: ")
        player2_name = input("두 번째 사람의 이름을 입력하세요: ")
        break
    except:
        print("잘못된 입력입니다. 다시 입력하세요")
        continue

player1 = Person(player1_name)
player2 = Person(player2_name)
tuple_player = (player1, player2)
# tuple_player = (Person(player1_name), Person(player2_name))
is_stop = False

while True:
    for player in tuple_player:
        player.set_list_numbers()

        numbers = player.get_list_numbers()
        
        #if (numbers[0] == numbers[1]) and (numbers[1] == numbers[2]) and (numbers[0] == numbers[2]) :
        #    print(player.name + "가 이겼습니다!" + str(numbers))
        #    break
        
        if len(set(player.get_list_numbers())) == 1:
            print(player.name + "가 이겼습니다!" + str(player.get_list_numbers()))
            is_stop = True

            break

    if is_stop:
        break