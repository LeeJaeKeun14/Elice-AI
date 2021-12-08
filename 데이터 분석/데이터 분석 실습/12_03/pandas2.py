import pandas as pd
import numpy as np

a = pd.Series([20, 15, 30, 25, 35], name='age')
b = pd.Series([68.5, 60.3, 53.4, 74.1, 80.7], name='weight')
c = pd.Series([180, 165, 155, 178, 185], name ='height')

## 1. human DataFrame 만들기
human = pd.DataFrame([a,b,c])
print(human,'\n')
# series들을 행방향으로 붙여 dataframe을 만든건데 사실 series의 경우 열 방향으로 보통 붙여줌
# -> 보통 데이터들의 경우, 열에 feature(변수) 행은 단순 index를 나타내기 때문
# print(pd.concat([a,b,c], axis=1))

def main():
    ### 2. loc(), iloc() 함수를 이용하여 `age`를 추출
    # loc의 경우 column이나 row index의 '명칭'을 통해, iloc의 경우 index의 '위치'를 통해 인덱싱/슬라이싱 진행
    print(human.loc['age'],'\n')
    print(human.iloc[0],'\n')
    
    ### 3. loc(), iloc() 함수를 이용하여 `weight`와 `height`만 추출
    # Quiz1. human.loc['weight','height'] 가능? -> error 발생
    # --> 해당 코드의 의미는 행의 'weight' index에, 열의 'height' index에 해당하는 데이터를 뽑겠다는 의미. 
    # --> 하지만 열에는 'height' index가 존재하지도 않으며, 우리가 원하는 것도 이런 것이 아님.
    # 행의 'weight','height' index에 해당하는 데이터를 뽑기 위해서는 human.loc[['weight','height'],:]와 같이 작성해야함
    # --> 해당 코드의 뜻은 행의 ['weight','height'] index에 해당하는 데이터를 모든 열에서 대하여 뽑겠다는 의미 
    # --> == human.loc[['weight','height']]로도 나타낼 수 있음
    print(human.loc[['weight','height']],'\n') # == human.loc[['weight','height'],:]
    
    # Quiz2. human.iloc[1,2]는? -> 53.4  
    # --> 해당 코드의 의미는 행에서는 1th 위치에, 열에서는 2nd 위치에 해당하는 데이터를 뽑겠다는 의미. 따라서 해당하는 값인 53.4가 결과로 나옴
    # 행의 1th, 2nd 위치에 해당하는 데이터를 뽑기 위해서는? human.iloc[[1,2],:]와 같이 작성해야함
    # --> == human.iloc[[1,2]] 로도 나타낼 수 있음
    # print(human.iloc[[1,2]],'\n') # == human.iloc[[1,2],:]

     
    sex = ['F','M','F','M','F']
    ### 4.새로운 데이터 `sex`를 `human`에 추가 (행에 추가)
    human.loc['sex',:] = sex # human.loc['sex'] = sex 도 가능 
    print(human,'\n')
    # Quiz3. 새로운 데이터인 [45,56.7,190,'M']를 'new'라는 명칭으로 열에 추가
    # new = [45,56.7,190,'M']
    # human.loc[:,'new'] = new
    # print(human,'\n')

    ### 5. `human`에서 `height`를 삭제
    tmp = human.drop(['height']) 
    # 위의 코드는 tmp = human.drop(['height'], axis=0)과 같음 (axis=0: 행 삭제 / axis=1: 열 삭제)
    # cf) tmp = human.drop(['height'],axis=1) ? -> error 발생
    # --> 'height'을 index로 가진 column을 삭제하겠다는 의미. 하지만 human dataframe의 경우 column에 'height' index가 없으므로 error 발생 
    # cf2) tmp = human.drop([1],axis=1) ? -> 1 index를 가진 열 삭제
    # cf3) tmp = human.drop(['height','weight'])와 같은 형식으로 여러개의 row 또는 column 삭제 가능
    print(tmp,'\n')

if __name__ == "__main__":
    main()

