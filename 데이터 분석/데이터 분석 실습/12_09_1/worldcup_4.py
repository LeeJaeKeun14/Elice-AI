## 국가별 득점 수 구하기 ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
import preprocess
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''

## Q1. 이전에 전처리한 WorldCupMatches.csv파일이 주어집니다.
world_cups_matches = preprocess.world_cups_matches

## Q2.홈 팀 득점을 나타내는 home 데이터 프레임과, 어웨이 팀 득점을 나타내는 away 데이터 프레임을 각각 만들어보고자 합니다.
# print(world_cups_matches.columns) # world_cups_matches 컬럼 확인
# Home Team Name(홈 팀 국가 이름)으로 그룹을 묶어 Home Team Goals(홈 팀 득점 수)의 합계를 구하고 home에 저장
home = world_cups_matches.groupby(['Home Team Name'])['Home Team Goals'].sum() # 홈 팀별 홈 팀의 총 득점 수
# print(home)
# Away Team Name(원정 팀 국가 이름)을 그룹으로 묶어 Away Team Goals(원정 팀 득점 수)의 합계를 구하고 away 변수에 저장
away = world_cups_matches.groupby(['Away Team Name'])['Away Team Goals'].sum() # 원정 팀별 원정 팀의 총 득점 수
# print(away)

## Q3. home, away 데이터 프레임을 하나로 합치고, goal_per_country라는 새로운 데이터프레임에 저장
# 결측값을 제거하기 위해 fillna 함수를 적용. 이떄 결측값은 0으로 대체 (골을 넣지 못했다는 의미이므로)
goal_per_country = pd.concat([home,away],axis=,sort=True).fillna(0) # axis=1을 통해 열의 방향으로 합치고, index인 나라 이름을 기준으로 합쳐짐 
# sort =True 로 설정할 경우 index를 중심으로 내림차순으로 정렬. sort=False로 할 경우 NaN값이 아래로 몰림
# print(goal_per_country)

## Q4.새로운 칼럼 “Goals”를 만들기
# 각 나라별 홈 팀일 때의 총 득점 + 원정 팀일 때의 총 득점 = 각 나라별 총 득점 
goal_per_country['Goals'] = goal_per_country['Home Team Goals'] + goal_per_country['Away Team Goals'] # 시리즈 + 시리즈 = 시리즈

## Q5.Goals 칼럼만 추출하고, 내림차순으로 정렬
goal_per_country = goal_per_country.Goals.sort_values(ascending=False) # 총 득점 수가 많은 나라 순서대로 나열됨
# print(goal_per_country) # 기본이 float형 (dtype: float64)

## Q6.저장된 값의 dtype를 정수형으로 바꾸기
goal_per_country = goal_per_country.astype(int)
print(goal_per_country)




