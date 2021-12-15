## 월드컵 4강 이상 성적 집계하기 ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from elice_utils import EliceUtils
elice_utils = EliceUtils()
import preprocess
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
ranks = preprocess.ranks
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''

# x축에 그려질 막대그래프들의 위치입니다.
x = np.array(list(range(0, len(ranks)))) # len(ranks) == ranks.shape[0] 
# print(ranks.shape, len(ranks))

# 그래프를 그립니다.
fig, ax = plt.subplots()

# x 위치에, 항목 이름으로 ranks.index(국가명)을 붙입니다.
plt.xticks(x, ranks.index, rotation=90)
plt.tight_layout() # figure의 모서리와 서브플롯의 모서리 사이의 여백을 설정. 해당 설정이 없을 경우 국가이름이 잘림

## Tips
# ranks.plot(y=["Winner", "Runners_Up", "Third", "Fourth"],
#     kind="bar", 
#     color=['gold', 'silver', 'brown', 'black'], 
#     figsize=(15,12),
#     fontsize=10, 
#     width=0.8,
#     align='center')

# 4개의 막대를 차례대로 그립니다.: 이를 위해 x을 위와 같이 설정
ax.bar(x - 0.3, ranks['Winner'],     color = 'gold',   width = 0.2, label = 'Winner')
ax.bar(x - 0.1, ranks['Runners_Up'], color = 'silver', width = 0.2, label = 'Runners_Up')
ax.bar(x + 0.1, ranks['Third'],      color = 'brown',  width = 0.2, label = 'Third')
ax.bar(x + 0.3, ranks['Fourth'],     color = 'black',  width = 0.2, label = 'Fourth')

plt.savefig("image.svg", format="svg")
elice_utils.send_image("image.svg")