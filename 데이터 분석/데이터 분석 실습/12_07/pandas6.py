## 데이터를 정리하는 방법 - rename() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
print(test_data.columns)


# 지시사항 2번을 참고하여 코드를 작성하세요.
test_data.rename(columns = {'name' : '이름', 'class' : '학급명', 'math' : '수학', 'english' : '영어', 'korean' : '국어'}, inplace = True)
print(test_data.columns)
# inplace=True를 통해 test_data자체를 바꿔버림. 
