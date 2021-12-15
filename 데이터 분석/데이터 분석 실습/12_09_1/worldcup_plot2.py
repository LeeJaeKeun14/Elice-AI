## 역대 월드컵의 경기당 득점 수 ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
world_cups = pd.read_csv("WorldCups.csv")
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''

# world_cups 데이터에서 'Year', 'GoalsScored'(총 득점 수), 'MatchesPlayed'(총 경기 수)만 추출
world_cups = world_cups[['Year', 'GoalsScored', 'MatchesPlayed']]
# 앞의 문제에서 했던 것처럼 새로운 칼럼 GoalsPerMatch(경기당 골 수)를 추가 ("GoalsScored"/"MatchesPlayed")
world_cups["GoalsPerMatch"] = world_cups["GoalsScored"] / world_cups["MatchesPlayed"]


# 첫 번째 그래프 출력 (axes[0])
fig, axes = plt.subplots(2, 1, figsize=(4,8)) # 2개의 행과 1개의 열
# bar 그래프를 그리고 다음에 plot 그래프(선 그래프)를 그림
axes[0].bar(x=world_cups['Year'], height=world_cups['GoalsScored'], color='grey', label='goals') # 총 득점 수는 bar 그래프호
axes[0].plot(world_cups['Year'], world_cups['MatchesPlayed'], marker='o', color='blue', label='matches') # 총 경기 수는 선 그래프로
axes[0].legend(loc='upper left')


# 두 번째 그래프 출력 (axes[1])
axes[1].grid(True) # 배경에 grid 표시
axes[1].plot(world_cups['Year'], world_cups['GoalsPerMatch'], marker='o', color='red', label='goals_per_matches') # 경기당 골 수는 빨간색 그래프로
axes[1].legend(loc='lower left')

plt.savefig("image.svg", format="svg")
elice_utils.send_image("image.svg")