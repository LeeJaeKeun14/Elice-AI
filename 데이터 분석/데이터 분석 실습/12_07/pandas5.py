## 데이터를 정리하는 방법 - astype() ##

# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
import numpy as np
import pandas as pd
test_data = pd.read_csv('testfile.csv')

# 지시사항 1번을 참고하여 코드를 작성하세요.
print(test_data.info())


# 지시사항 2번을 참고하여 코드를 작성하세요.
test_data = test_data.astype({'class':'category'})
# == test_data['class'] = test_data['class']astype('category')
# cf. test_data.class = test_data.class.astype('category') 는 불가. class가 이미 python의 내장함수이기 때문에 사용하면 안됨
# 저의 경우 여러개의 데이터의 type을 바꿔야할 때는 위에 방식, 하나의 데이터만 바꿀 경우 아래의 방식을 사용. 편하신거 사용하세요!
# test_data = test_data.astype({'class':'category', 'name':'category'}) : 여러 열의 데이터 타입을 변경할 때

# 지시사항 3번을 참고하여 코드를 작성하세요.
print(test_data.info())