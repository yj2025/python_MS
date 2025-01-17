# packing
def sum(*nums):
    s = 0
    for i in nums:
        s += i
    return s

print(sum(1,2,3))

# unpacking
# 튜플로 함수를 호출할때 언패킹 사용
def show_man(name,age,height):
    print(name,age,height)

p = ('kim',20,160) 
show_man(*p) # p에 담긴 값을 풀어서 각각의 매개변수에 전달

pp = 'hong', (32,178), '010-1111-1111', 'korea'
na, (age, height), ph, ad = pp
print(na, (age, height), ph, ad, sep = ', ')

na, (_, he), _, _ = pp
print(na, he, sep = ', ',end='=======') # print(*arg,*,/,sep='',end='\n')

print('')

ps = [('Lee',172),('Jung',182),('Yoon',179)] #리스트에 담긴 튜플
for n,h in ps:
    print(n,h, sep = ', ')
