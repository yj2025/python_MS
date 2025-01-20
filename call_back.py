# 1
def func1(n):
    print('hello')

print(type(func1))

def say1():
    print('hello')

def say2():
    print('hi')

def caller(fct):    # callback 함수
    fct()

caller(say1)    # hello
caller(say2)    # hi

# 2
def fct_fac(n):
    def exp(x):
        return x ** n

    return exp

f2 = fct_fac(2)
f3 = fct_fac(3)
f4 = fct_fac(4)

print(f2(10))   # 100
print(f3(10))   # 1000
print(f4(10))   # 10000