def decorator(func):
    def wrapper():
        print('*')
        func()
        print('*')
    return wrapper

@decorator
def say_hello():
    print('hello!')

say_hello()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def adder_deco(func):
    def add(*n):
        print("{}".format(func(*n)))
    return add

@adder_deco
def adder1(n1, n2, n3):
    return n1 + n2 + n3

@adder_deco
def adder2(n1, n2 ,n3, n4):
    return n1 + n2 + n3 + n4

@adder_deco
def adder3(n1, n2 ,n3, n4, n5):
    return n1 + n2 + n3 + n4 + n5

adder1(1,2, 3)		# 6
adder2(1,2,3, 4)	# 10
adder3(1,2,3,4, 5)	# 15

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# static method
# 일반 함수처럼 사용
# 클래스 인스턴스를 만들지 않고 직접 호출 가능
# 클래스 내부에서 정의되는 함수지만, 클래스나 인스턴스의 상태에 의존 X

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 5))	# 8     직접 호출

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# classmethod
# 인스턴스를 만들지 않고 클래스 이름으로 바로 호출 가능

class Circle2:
    PI = 3.12419
    @classmethod
    def get_area(cls,radius):
        return cls.PI * radius * radius

print(Circle2.PI)	# 3.12419
res = Circle2.get_area(5)   # Circle2.get_area(Circle2.5)
print(res)			# 78.10475

c2 = Circle2()
print(c2.PI)		# 3.12419
res = c2.get_area(5)
print(res)			# 78.10475

class Korean:
    country = 'korea'

    def i_change(self, name):
        self.country = name
    
    @classmethod
    def c_change(self, name):   # self -> 자기 자신의 인자가 아니라 자기 자신의 소속 클래스를 가리킨다
        self.country = name

a, b = Korean(), Korean()
print(a.country)    # korea
print(b.country)    # korea

a.i_change('south korea')
print(a.country)    # south korea
print(b.country)    # korea

a.c_change('south korea')
print(a.country)    # south korea
print(b.country)    # south korea

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# property
# 함수지만 변수처럼 사용하고 싶을 때 사용1

class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

xy = XY(1, 2)
print(xy.x)		# 1
xy.x = 10
print(xy.x)		# 10	클래스 밖에서 x 값 변경
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
class XY:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

xy = XY(1, 2)
print(xy.x)	# 1

# @property로 정의된 속성은 getter만 정의된 상태라서 값을 변경할 수 없음
xy.x = 10	# AttributeError 발생	
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# self._x는 프로퍼티가 아닌 일반 인스턴스 변수 직접 수정하면 값이 바뀜
xy._x = 10  
print(xy.x)	# 10
