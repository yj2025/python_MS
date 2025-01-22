# map
def pow(n):
    return n ** 2

str1 = [1, 2, 3]

str2 = [pow(str1[0]), pow(str1[1]), pow(str1[2])]
print(str2) # [1, 4, 9]

str2 = list(map(pow, str1)) # map(pow,str1) => 연산이 끝나면 iterator 객체로 리턴

type_str1 = map(pow,str1)
print(type_str1)    # <map object at 0x00000226C7E117B0>

ir = map(pow, str1) # map은 iterator 객체 반환
for i in ir:        # .__liter__().__next__()
    print(i)

# filter (필터) 함수 => 걸러 내는 거

def is_odd(n):
    return n % 2 # 홀수 True

st = [1, 2, 3, 4, 5]
ost = list(filter(is_odd,st))
print(ost)