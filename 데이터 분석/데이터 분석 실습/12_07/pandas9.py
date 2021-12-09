## 데이터를 분석하는 방법 - unique() ## 

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
# print(test_data['class'])
print(test_data['class'].unique())

# print(type(test_data['class'].unique())) <- <class 'numpy.ndarray'>
# class가 현재 int64형이라서 numpy의 배열 형태로 반환 (print(test_data.info()))
# class를 category형으로 바꾼 후 type확인하면 <class 'pandas.core.arrays.categorical.Categorical'>로 나옴
# test_data['class'] = test_data['class'].astype('category') ; print(type(test_data['class'].unique()))

