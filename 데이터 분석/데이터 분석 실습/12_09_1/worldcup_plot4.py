## 2014 월드컵 다득점 국가 순위 ##

import matplotlib.pyplot as plt
from elice_utils import EliceUtils
import preprocess
elice_utils = EliceUtils()
team_goal_2014 = preprocess.team_goal_2014 # 이전 실습에서 처리한 team_goal_2014 데이터 불러오기
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''
print(team_goal_2014) # team_goal_2014 데이터 확인
# plot 함수의 kind 속성으로 “bar”를 부여하여 막대그래프를 생성
team_goal_2014.plot(x=team_goal_2014.index, y=team_goal_2014.values, kind="bar", figsize=(12, 12), fontsize=14)
plt.tight_layout() # 여백 간격 설정. 나라의 이름들을 다 보이게 해줌

# fig, ax = plt.subplots()
# ax.bar(team_goal_2014.index, team_goal_2014.values)
# plt.xticks(rotation = 90)
# plt.tight_layout()

plt.savefig("image.svg", format="svg")
elice_utils.send_image("image.svg")
