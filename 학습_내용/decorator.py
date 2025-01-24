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