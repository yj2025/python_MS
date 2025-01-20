class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # if 문의 해당 함수에서 0이 들어 가지 않도록 막음
    def add_age(self,age):
        if age < 0:
            print('나이는 0보다 커야 합니다. 나이 정보 오류')
        else:
            self.__age += age

    def __str__(self):
        return f'이름은 {self.__name}, 나이는 {self.__age}'


p = Person('홍길동', 20)
p.__age = 30


def deco(fun):
    def wrapper():
        print('emotion!')
        fun()
        print('emotion!')
    return wrapper

@deco
def smile():
    print('^_^')

def confused():
    print('@_@')

smile()

