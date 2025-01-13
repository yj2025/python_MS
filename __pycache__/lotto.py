# random 모듈
import random
print(random.random()) # 0 이상 1 미만 임의의 실수 반환
print(random.randrange(1,6)) # 주사위 (1~6)
print(random.randint(1,45)) # 1-45 중 랜덤 정수 반환

abc = [1,2,3,4,5]
random.shuffle(abc)
print(abc)

menu = ("쫄면","육개장",'비빔밥')
random.choice(menu)
random.choice([True, False])

# 로또
# 1 - 45 까지 번호 6개 추출
# 리스트로 뽑기
# 중복 제거
# for문 리스트 제공 함수등으로 구성

class LottoNum:
    def __init__(self):
        self.lst = []

    def get_lotto_nums(self):
        while len(self.lst) < 6:
            num = random.randint(1, 45)
            if num not in self.lst:
                self.lst.append(num)

        return self.lst

lotto = LottoNum()
print(lotto.get_lotto_nums())

