class MyClass:
    def __init__(self):
        self.__hidden = 42

    def get_hidden(self):
        return self.__hidden    # 접근 가능 메서드

    def set_hidden(self, value):
        self.__hidden = value   # 값을 설정하는 메서드

obj = MyClass()
# print(obj.__hidden)   AttributeError 발생
print(obj.get_hidden())
obj.set_hidden(100) # __hidden 값을 100으로 변경
print(obj.get_hidden()) # 100 출력
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def add_age(self, age):
        if age < 0:
            print('나이는 0보다 커야 합니다. 나이 정보 오류')
        else:
            self.__age += age

    def __str__(self):
        return f'이름: {self.__name}, 나이: {self.__age}'

p = Person('진병권', 20)
p.__age = 30
'''
기존의 private 변수 self.__age를 수정하는 것이 아닌,
객체 p에 새로운 public 속성 __age를 추가하는 것
private 변수에 영향을 미치지 않음
'''
print(p)    # 이름: 진병권, 나이: 20
p.add_age(30)
print(p)    # 이름: 진병권, 나이: 50