## 데이터 구조를 확인하는 함수 - shape, head() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import pandas as pd
import numpy as np

# 지시사항 1번을 참고하여 코드를 작성하세요.
test_data = pd.read_csv('testfile.csv')

# 지시사항 2번을 참고하여 코드를 작성하세요.
print(test_data.shape)

## (*) 지시사항 2번이랑 3번이 제대로 안 나눠진듯
## 지시사항 3: head 속성을 통해 test_data 데이터의 상단 5개의 데이터를 출력하세요 
print(test_data.head())

# Quiz. test_data 데이터의 상단 2개의 데이터만 출력
# test_data.head(2)
