## 데이터 시각화하는 방법 - barh() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
test_data = pd.read_csv('testfile.csv')
# print(test_data.head()): 해당 데이터셋은 앞의 데이터셋과 달리 class가 ~반으로 되어있음

# 지시사항 1번을 참고하여 코드를 작성하세요.
fig, axes = plt.subplots(figsize = (10,7))
# axes.bar(test_data['class'], test_data['math']) 
axes.barh(test_data['class'], test_data['math'], height = 0.7) # height을 통해 바의 얇기 설정
# bar는 일반적인 세로 바 그래프, barh는 가로 바 그래프
axes.set_title("엘리스 학교 학급 당 평균 수학점수", size= 20)
axes.set_xlabel("평균 점수", size= 10)
axes.set_ylabel("학급 별", size= 10)
plt.margins(y= 0.3) # 마진을 줘서 바 그래프를 더 여유있게 그려줌


# 아래 코드는 이미지 출력을 위한 코드입니다. 수정하지 마세요!
plt.savefig("img.svg", format="svg")
elice_utils.send_image("img.svg")