## 역대 월드컵의 국가별 득점 수 ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preprocess
from elice_utils import EliceUtils
elice_utils = EliceUtils()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''

goal_per_country = preprocess.goal_per_country # 이전 실습에서 진행한 goal_per_country (국가별 총 득점 수)
goal_per_country = goal_per_country[:10] # goal_per_country 데이터(총 득점 수가 많은 나라 순서대로 나열되어 있음)에서 상위 10개국만 뽑기
# print(goal_per_country)

# x, y값 저장
x = goal_per_country.index # 나라의 이름들
y = goal_per_country.values # 나라별 골 획득의 수

#그래프 그리기
fig, ax = plt.subplots()
# 데이터에서 상위 10개국의 데이터를 bar 함수로 막대그래프를 그림
ax.bar(x, y, width = 0.5)

# x축 항목 이름 지정, 30도 회전
plt.xticks(x, rotation=30)
plt.tight_layout() # 글자가 넘쳐서 잘리는 현상 방지

## Tips
# goal_per_country.plot(x=x, y=y, kind='bar') # 로도 가능
# -> 시리즈 데이터에서도 직접 plot 호출 가능. kind를 통해 어떤 그래프를 그릴지 정함. ex. bar, hist, line, pie..

#그래프 출력
plt.savefig("image.svg", format="svg")
elice_utils.send_image("image.svg")

