class Counter:
    def __init__(self, stop):
        self.current = 0        # 현재 숫자 유지, 0부터 지정된 숫자까지 반복
        self.stop = stop        # 반복을 끝낼 숫자

    def __iter__(self):
        return self             # 현재 인스턴스를 반환
    
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 r(변수)에 저장
            self.current += 1           
            return r
        else:
            raise StopIteration         # iterator가 더이상 반환할 값이 없을 때 발생

counter = Counter(10)

for i in counter.__iter__():
    print(i, end=' ')

# 0 1 2 3 4 5 6 7 8 9 