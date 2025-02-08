# 데이터 프레임

import pandas as pd
import numpy as np

# 데이터 프레임 생성 3가지 방법 -> 딕셔너리 / 리스트 / 넘파이 배열

# 딕셔너리
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# 리스트
data = [
    [1, 4],
    [2, 5],
    [3, 6]
]
df = pd.DataFrame(data, columns=['A', 'B'])

# 넘파이 배열
data = np.array([[1, 4], [2, 5], [3, 6]])
df = pd.DataFrame(data, columns=['A', 'B'])




# 1
data = {
    "시가" : [980,980,980],
    '고가' : [80,80,80],
    '저가' : [70,70,70],
    '종가' : [90,90,90],
}

index = ['삼성전자', '카카오', '네이버']

stock_df = pd.DataFrame(data=data, index=index)
print(stock_df)

# 로우 단위 생성
data = [
        [980, 80, 70, 90],
        [980, 80, 70, 90],
        [980, 80, 70, 90]
    ]

column = ["시가","고가","저가","종가"]
index = ["삼성전자","카카오","네이버"]

df_stock = pd.DataFrame(data=data, columns=column, index=index)
print(df_stock)

# 로우 단위를 딕셔너리로 표현하여 생성
data2 =[
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
         {"시가":980, "고가":80 , "저가":70 , "종가":90},
]
index2 = ["삼성전자","카카오","네이버"]

df_stock = pd.DataFrame(data=data2,index=index2)
print(df_stock)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

# 2
close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = pd.Series(data=open, index=index)
close = pd.Series(data=close, index=index)

cond = close > open
print(close[cond])

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

# 3
s = pd.Series([1234, 5678, 9876])

def fun_s(x):
    if x > 5000:
        return '크다'
    else:
        return '작다'

result = s.map(fun_s)
print(result)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

# 정렬 및 순위
data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']

s = pd.Series(data=data, index=index)

# 정렬
s1 = s.sort_values()    # 기본 올림차순
print(s1)

# 내림차순
s2 = s.sort_values(ascending=False)
print(s2)

# 인덱스 정렬
s3 = s.sort_index()
print(s3)

# 랭킹
s4 = s.rank() # float 64 소수점 
print(s4)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

