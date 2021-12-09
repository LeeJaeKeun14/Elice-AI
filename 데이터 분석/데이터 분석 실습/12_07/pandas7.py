## 데이터를 분석하는 방법 - index, isin() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
print(test_data.index)
# cf. test_data.columns : 컬럼 이름 추출


# 지시사항 2번을 참고하여 코드를 작성하세요.
print(test_data.isin([99,100]))
# 99점과 100점인 값들은 True, 아닌 값들은 False로 나타남
# Quiz. 90점이상 95점 이하인 값들을 확인하려면? print(test_data.isin(range(90,96)))

# Tips) 국어 성적 중에서 99점과 100점이 있는지 확인
# print(test_data[['korean']].isin([99,100]))
# Tips의 경우 데이터프레임 형식으로 국어 성적을 뽑은 다음 isin 적용
# test_data['korean'].isin([99,100])의 경우 시리즈 형식으로 국어 성적을 뽑은 다음 isin 적용
# 시리즈 형식으로 뽑는게 더 활용성이 높기 때문에 아래의 방식 추천