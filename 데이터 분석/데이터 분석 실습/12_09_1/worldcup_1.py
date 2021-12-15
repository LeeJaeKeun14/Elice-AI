## 역대 월드컵의 관중 수 출력하기 ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''
## Q1. WorldCups.csv파일을 pandas의 DataFrame으로 만들기
world_cups = pd.read_csv('WorldCups.csv')

## Q2. Year와 Attendance 칼럼만 추출하여 출력
world_cups = world_cups[['Year','Attendance']]

## Q3. 역대 월드컵의 관중 수가 제대로 출력되었는지 확인
world_cups

