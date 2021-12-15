## 역대 월드컵의 관중 수 ##

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

world_cups = world_cups[['Year', 'Attendance']]
print(world_cups) # 뽑은 데이터 확인

# 역대 월드컵의 관중 수를 그래프로 출력
plt.plot(world_cups['Year'], world_cups['Attendance'], marker='o', color='black')
# Q) 그래프의 색깔 + 마커 모양 + 선 스타일을 한번에 나타내기
# plt.plot(world_cups.Year, world_cups.Attendance,'ko-')

plt.savefig("image.svg", format="svg")
elice_utils.send_image("image.svg")