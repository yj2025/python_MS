# 정보 은닉

class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age     # private 속성으로 선언
    
    def add_age(self, age):
        if age < 0:
            print('나이 정보 오류')
        else:
            self.__age += age
    
    def get_age(self):
        return self.__age

    def __str__(self):
        return f"이름 : {self._name}, 나이 : {self.__age}"

p = Person('진병권', 20)
print(p)

p.add_age(1)
print(p)

# p.add_age(-30)
# print(p)

# p.age += -30
# print(p)