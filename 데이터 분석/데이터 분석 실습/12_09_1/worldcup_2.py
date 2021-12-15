## 역대 월드컵의 경기당 득점 수 ##

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

## Q1. WorldCups.csv파일을 pandas의 DataFrame으로 만들어보기
# csv 파일을 데이터프레임으로 불러오라는 의미
world_cups = pd.read_csv('WorldCups.csv')

## Q2. Year 와 GoalsScored(총 득점 수), MatchesPlayed(총 경기 수) 칼럼만 추출
world_cups = world_cups[['Year','GoalsScored','MatchesPlayed']]

## Q3. 새로운 칼럼 GoalsPerMatch를 추가
world_cups['GoalsPerMatch'] = world_cups['GoalsScored'] / world_cups['MatchesPlayed']

## Q4. 데이터 프레임을 출력: 칼럼이 제대로 추가되었나 확인
print(world_cups) 
