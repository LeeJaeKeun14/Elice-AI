## 2014 월드컵 다득점 국가 순위 ##

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

world_cups_matches = preprocess.world_cups_matches

## Q1. Year가 2014인 것들을 추출
world_cups_matches = world_cups_matches[world_cups_matches.Year == 2014]

## Q2.2014년 월드컵 경기 데이터 중에서 홈 팀의 골 수와 원정 팀의 골 수를 각각 계산: 앞에서 했던 방식과 동일
# Home Team Name을 그룹으로 묶어 Home Team Goals의 합계를 구하고 home_team_goal 변수에 저장
home_team_goal = world_cups_matches.groupby(['Home Team Name'])['Home Team Goals'].sum()
# Away Team Name을 그룹으로 묶어 Away Team Goals의 합계를 구하고 away_team_goal 변수에 저장
away_team_goal = world_cups_matches.groupby(['Away Team Name'])['Away Team Goals'].sum()

## Q3.홈 득점 수와 원정 득점 수를 하나의 데이터로 합침
# home_team_goal과 away_team_goal을 열의 방향으로 합쳐서 team_goal_2014 변수에 저장
# 결측값이 존재한다는 것은, 골을 넣지 못했다는 의미이므로 0으로 대체
team_goal_2014 = pd.concat([home_team_goal, away_team_goal],axis=1).fillna(0)

## Q4.홈 팀 골과 원정 팀 골 수를 합한 새로운 칼럼 goals를 만들고, 기존 칼럼은 drop 함수를 이용해 삭제
# Home Team Goals와 Away Team Goals를 합쳐 goals라는 새로운 컬럼을 만듦
team_goal_2014['goals'] = team_goal_2014['Home Team Goals']+ team_goal_2014['Away Team Goals']
# 기존의 Home Team Goals와 Away Team Goals 컬럼은 drop 함수를 이용해 삭제
team_goal_2014 = team_goal_2014.drop(['Home Team Goals', 'Away Team Goals'], axis=1)
# == team_goal_2014.drop(['Home Team Goals', 'Away Team Goals'], axis=1, inplace=True)
# == team_goal_2014 = team_goal_2014.drop(columns=["Home Team Goals", "Away Team Goals"])

## Q5.저장된 값을 정수로 변환 - 근데 기본적인 값이 정수 값이어서 하나 안하나 같음
team_goal_2014 = team_goal_2014.astype('int') # 

## Q6.데이터 프레임을 내림차순으로 정렬
print(team_goal_2014.goals.sort_values(ascending=False))
