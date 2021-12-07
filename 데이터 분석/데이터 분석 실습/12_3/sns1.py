##### [실습9] Seaborn regplot 그리기 #####

# Seaborn 라이브러리 import 하기 
import seaborn as sns 
import matplotlib.pyplot as plt 

from elice_utils import EliceUtils
elice_utils = EliceUtils()

# seaborn의 load_dataset을 사용하여 tips (팁 가격) 데이터 불러오기
df = sns.load_dataset('tips') # seaborn 내장데이터

# 전체 데이터에서 처음 5개의 row 데이터 표시 (내용 확인)
# 데이터에 대한 정보를 알고 싶은 경우, 주석을 풀어 확인
print(df.head())
# 기본 설정은 5개의 row를 보여줌. 안에 숫자를 넣어 원하는 수만큼의 row를 볼 수 있음. ex. df.head(2)
# df.head를 통해 컬럼들 종류 확인

# x축에 해당되는 데이터로 total_bill series를 x_data으로 저장 
x_data = df['total_bill']
# y축에 해당되는 데이터로 tip series를 y_data으로 저장 
y_data = df['tip']

# regplot함수의 출력물을 sns_plot으로 저장
# line의 색은 red로 설정
sns_plot = sns.regplot(x_data, y_data, line_kws={'color': 'red'})
# cf) scatter의 색을 빨간색으로: sns_plot = sns.regplot(x_data, y_data, scatter_kws={'color': 'red'})
# cf) 전체적으로 빨간색으로: sns_plot = sns.regplot(x_data, y_data, color='red')

# 엘리스 플랫폼 내의 출력을 위한 함수
fig = sns_plot.get_figure()
fig.savefig("plot.png")
elice_utils.send_image("plot.png")