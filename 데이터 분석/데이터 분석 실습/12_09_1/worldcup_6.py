## 월드컵 4강 이상 성적 집계하기 ##

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

world_cups = pd.read_csv("WorldCups.csv")
# 맨 처음에 다뤘던 데이터. 방금 앞까지 다뤘던 WorldCupsMatches.csv 파일과 다름

## Q1.데이터 프레임에서 역대 대회 1위 국가들, 2위 국가들, 3위 국가들, 4위 국가들을 추출
winner = world_cups.Winner # 1위 국가
runners_up = world_cups["Runners-Up"] # 2위 국가
third = world_cups.Third # 3위 국가
fourth = world_cups.Fourth # 4위 국가

## Q2. value_counts 함수를 이용해 각 시리즈 데이터에 저장된 값을 세어주고 저장
# 등수별(1~4위)로 각 국가가 몇변 해당 등수를 달성하였는지가 나타남
winner_count = pd.Series(winner.value_counts())
runners_up_count = pd.Series(runners_up.value_counts())
third_count = pd.Series(third.value_counts())
fourth_count = pd.Series(fourth.value_counts())
# print(winner_count)

## Q3. 위 데이터들을 하나의 데이터 프레임으로 합침
ranks = pd.concat([winner_count, runners_up_count, third_count, fourth_count], axis=1, sort = True)

## Q4.데이터의 결측값을 0으로 채우고, dtype을 int64로 설정
ranks = ranks.fillna(0).astype('int64') # 기존 ranks의 경우 data type이 float형. astype을 통해 int64형으로 바꿔줌
# print(ranks)

## Q5.1위 횟수, 2위 횟수, 3위 횟수, 4위 횟수 순서대로 내림차순 정렬
ranks = ranks.sort_values(['Winner', 'Runners_Up', 'Third', 'Fourth'], ascending=False)
print(ranks)





