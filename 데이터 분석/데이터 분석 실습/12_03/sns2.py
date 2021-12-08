##### [실습10] Seaborn countplot, jointplot 그리기 #####

# Seaborn 라이브러리 import 하기 
import seaborn as sns 
import matplotlib.pyplot as plt 

from elice_utils import EliceUtils
elice_utils = EliceUtils()

# seaborn의 load_dataset을 사용하여 tips (팁 가격) 데이터 불러오기
df = sns.load_dataset('tips') 
# print(df.columns)

# countplot함수의 출력물을 sns_plot_size으로 저장
# "size" 데이터에 해당하는 자료를 x축으로 출력
sns_plot_size = sns.countplot(x='size', data=df)
# sns_plot_size = sns.countplot(df['size']) 와 같은 형식도 가능
# Quiz1. sns.countplot(x='size', data=df) ? <- error 발생.Cannot pass values for both `x` and `y`
# countplot의 경우, 해당 데이터의 unique value들의 개수를 세어 그래프로 보여주는 함수이므로 한 종류의 데이터만 들어가야함
# Quiz2. 가로 버전으로 나타내려면? sns_plot_size = sns.countplot(y='size', data=df) 
# -> x,y의 의미는 어떤 방향으로 데이터를 보여주려는지임

# jointplot함수의 출력물을 g로 저장
# "total_bill"을 x축, "tip"을 y축, "resid" 형태 그래프로 설정 
g = sns.jointplot(df['total_bill'], df['tip'], kind='resid')
# == sns.jointplot(x='total_bill', y='tip', data=df, kind='resid')
# kind='resid'의 경우 잔차그래프를 그리는건데, 이건 후에 머신러닝 파트에서 배울겁니다.(아마..?)

# 엘리스 플랫폼 내의 출력을 위한 함수
fig = sns_plot_size.get_figure()
fig.savefig("plot_siz.png")
elice_utils.send_image("plot_siz.png")

g.savefig("plot.png")
elice_utils.send_image("plot.png")