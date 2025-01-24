# decorator

def deco(fun):
    def wrapper():
        print('emotion!')
        fun()
        print('emotion!')
    return wrapper

@deco
def smile():
    print('^_^')

# 여러번 중첩 가능
@deco
@deco
@deco
@deco
def confused():
    print('@_@')

smile()
print('')

confused()