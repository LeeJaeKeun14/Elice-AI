## 데이터를 분석하는 방법 - value_counts() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
# print(test_data['class'])
print(test_data['class'].value_counts())
# 시리즈 형식으로 뽑은 후 value_counts를 한거임
# 기본적으로 내림차순 정렬. 오름차순 정렬하고 싶으면 ascending=True
# print(test_data['class'].value_counts(ascending=True))