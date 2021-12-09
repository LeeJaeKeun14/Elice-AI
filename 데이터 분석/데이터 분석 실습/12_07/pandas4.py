## 데이터 정리하기 - 특정 열 선택하기 ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
print(test_data.head())


# 지시사항 2번을 참고하여 코드를 작성하세요.
print(test_data[['math']])

# 지시사항 2번의 경우 수학점수의 열만 '데이터프레임' 형식으로 뽑아낸 것
# print(test_data.math) ; print(test_data['math'])
# 위의 경우 '시리즈' 형식으로 뽑아낸 경우
# 엘리스에선 데이터프레임과 시리즈 형식이 차이가 나지 않는데, 코랩이나 쥬피터노트북으로 보면 확실하게 차이가 보임 
# Quiz. loc으로 math만 뽑아내려면? df.loc[:,'math'] : 마찬가지로 시리즈 형식임

# Quiz. 수학(math), 국어(korean) 열을 선택
# print(test_data[['math','korean']])
# test_data['math','korean'] <- error 발생. 두개이상(데이터프레임 형식) 뽑고 싶을 때는 [[]]를 사용!