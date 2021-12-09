## 데이터 구조를 확인하는 함수 - info() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import pandas as pd
import numpy as np

# 지시사항 1번을 참고하여 코드를 작성하세요.
test_data = pd.read_csv('testfile.csv')


# 지시사항 2번을 참고하여 코드를 작성하세요.
print(test_data.info())

# Quiz. test_data의 요약통계량 확인하려면?
# test_data.describe()
## include 인자를 통해 원하는 요약통계량을 볼 수 있음