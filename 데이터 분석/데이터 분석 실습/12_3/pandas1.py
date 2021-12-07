import pandas as pd

### 1.1차원 데이터를 선언하여 Series형 데이터를 생성하세요.
# 5개의 age 데이터와 이름을 age로 선언해보세요.
## # 5개 데이터의 경우 자유롭게 설정!
age = pd.Series([12,54,23,10,3], name= 'age')
print(age)

### 2. Python Dictionary형 데이터 class_name을 Series형 데이터로 생성하세요.
class_name = {'국어' : 90,'영어' : 70,'수학' : 100,'과학' : 80}
class_series = pd.Series(class_name)
print(class_series,'\n')

### 3. 2차원 데이터를 선언하여 DataFrame형 데이터를 생성하세요.
# index와 columns 값을 직접 설정해보세요.
## 마찬가지로 원하는 대로 dataframe 만들기! 밑에는 단순 예시
scores = [[45,34,54],
          [34,5,6],
          [34,56,99]]
df = pd.DataFrame(scores, index =['A','B','C'], columns = ['국어','수학','영어'])
print(df,'\n')
## Quiz1. dictionary를 이용해서 위의 df와 똑같은 DataFrame을 만드세요 (여러분의 데이터에 맞게!)
## scores = {'국어':[45,34,34],'수학':[34,5,56],'영어':[54,6,99]} ; pd.DataFrame(scores, index=['A','B','C'])

