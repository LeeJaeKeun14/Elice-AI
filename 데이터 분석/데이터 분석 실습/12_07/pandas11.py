## 데이터 시각화하는 방법 - boxplot() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
fig, axes = plt.subplots(figsize = (20,20))
axes.boxplot(test_data['math'])
axes.set_title("엘리스 학교 수학 성적", size=30)
axes.set_xlabel("과목", size=30)
axes.set_ylabel("점수", size=30)

# Tips) 수학과 국어에 대한 상자 그림
# axes.boxplot((test_data['math'], test_data['korean']))
# axes.set_xticklabels(["수학","국어"], size=30) : xticklabels를 통해 과목 이름 설정 가능

# 아래 코드는 이미지 출력을 위한 코드입니다. 수정하지 마세요!
plt.savefig("img.svg", format="svg")
elice_utils.send_image("img.svg")