## 데이터 시각화하는 방법 - bar() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()

test_data = pd.read_csv('testfile.csv')
# print(test_data.head()) : 데이터의 형태 확인. 앞에서 사용하였던 데이터와는 다른 데이터

# 지시사항 1번을 참고하여 코드를 작성하세요.
counts = test_data['class'].value_counts().sort_index() # 인덱스로 내림차순 (1반, 2반, 3반)
print(counts)
# print(test_data['class'].value_counts()) ; vaule_counts는 기본적으로 값을 기준으로 내림차순 


# 지시사항 2번을 참고하여 코드를 작성하세요.
fig, axes = plt.subplots(figsize = (10,10))
axes.bar(counts.index, counts.values) # index의 class 이름(x값), values의 값들(y값)을 가져옴 
# print(counts.index) ; print(counts.values)
axes.set_title("학급 별 학생 수", size= 30)
axes.set_xlabel("학급 구분", size= 20)
axes.set_ylabel("학생 수", size= 20)

# 아래 코드는 채점을 위한 코드입니다. 수정하지 마세요!
plt.savefig("img.svg", format="svg")
elice_utils.send_image("img.svg")