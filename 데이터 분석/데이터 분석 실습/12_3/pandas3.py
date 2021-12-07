##### [실습6] DataFrame 다루기 #####

import numpy as np
import pandas as pd


A = pd.DataFrame(np.random.randint(0, 10, (2, 2)))
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)))
print(A,'\n',B)

# 함수를 이용해서 연산을 해보세요.
# NaN 값이 생기지 않도록 fill_value에 값을 넣어보세요: 0말고 다른 값들 넣어도 됨!
# A + B
# cf.add = A.add(B) ; print(add,'\n') : 3x3인 B에는 있지만 2x2인 A에는 없는 부분들의 값들이 NaN값으로 채워짐
add = A.add(B, fill_value=0) # 3x3인 B에는 있지만 2x2인 A에는 없는 부분들의 값을 fill_value인 0으로 채운 후 연산 진행
print(add,'\n')
# A - B
sub = A.sub(B, fill_value=0)
print(sub)
# A * B
mul = A.mul(B,fill_value=0)
print(mul,'\n')
# A / B
div = A.div(B,fill_value=0)
print(div,'\n') # 여기서 [2,0]에 NaN이 나온 이유는 0/0을 했기 때문


# 3 x 3 데이터프레임을 정렬해보세요.
C = pd.DataFrame([[1,3,5],[15,10,5],[2,8,5]], index = ['a','b','c'], columns = ['d','e','f'])
print(C)

# c 행에 대해 오름차순 정렬
row_C = C.sort_values('c',axis=1,ascending=True) # c행에 의해 '열들이' 오름차순으로 정렬되는 것이므로 axis=1

# e 열에 대해 내림차순 정렬
column_C = C.sort_values('e',axis=0,ascending=False) # e열에 의해 '행들이' 내림차순으로 정렬되는 것이므로 axis=0
# cf)
# print(C.loc['c',:].sort_values()) # C dataframe의 c 행만 뽑아 오름차순으로. 마찬가지로 ascending=False를 통해 내림차순 가능
# print(C.loc['c',:].sort_values().values) # .values를 통해 series의 값들만(index 제외) 뽑아올 수 있음
# print(C['e'].sort_values().values) # C dataframe의 c 행의 값들만 뽑아 오름차순으로 정렬. 보통 열에 feature가 있기 때문에 이런식으로 많이 씀

print(row_C,'\n')
print(column_C,'\n')

# 데이터 csv로 저장 및 불러오기
# index를 False로 설정하면 저장할 때 추가 인덱스를 달지 않습니다.
## 주의! row_C =의 형태가 아님 & './data.csv'로 저장
# row_C.to_csv('./data.csv') <- dataframe의 index값이 새로운 열로 저장되어버림
row_C.to_csv('./data.csv', index=False) # * index=False * <- index가 특수한 경우를 제외하곤 대부분 index=False 사용
load_C = pd.read_csv('./data.csv')

print(load_C)
