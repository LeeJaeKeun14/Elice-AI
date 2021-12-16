## 다중 선형 회귀 ##

from elice_utils import EliceUtils

elice_utils = EliceUtils()

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score 

TARGET_FEATURE = "petal width (cm)"

def load_data():
    # sklearn의 내장 데이터셋 iris 로드
    X, _ = load_iris(return_X_y=True, as_frame=True)
    y = X[TARGET_FEATURE] # TARGET_FEATURE = "petal width (cm)"
    # print(type(X)) # <class 'pandas.core.frame.DataFrame'>

    # TODO: X에서 "petal width (cm)" 컬럼을 제거하세요.
    # X가 dataframe 형식이므로 drop을 통해 제거 가능
    X = X.drop(TARGET_FEATURE, axis=1) # 열 제거이므로 axis=1

    return X, y

def fit_multiple_regression(X, y):
    # TODO: 다중 선형 회귀 모델을 학습하세요.
    lr_model = LinearRegression().fit(X,y) # fit을 통해 학습
    
    return lr_model

# 데이터와 학습된 직선을 함께 그래프로 그립니다.
def plot_result(X, y, y_pred, r2, feature_name="sepal_length"):
    fig = plt.figure()
    plt.title("{} Result".format(feature_name.replace("_", " ").title()))
    plt.xlabel("{} (cm)".format(feature_name.replace("_", " ")))
    plt.ylabel("petal width (cm)")

    plt.scatter(X, y, color="deepskyblue", label="Data Point")
    plt.scatter(X, y_pred, color="lightcoral", label="Predicted Point")
    plt.plot([], [], ' ', label="R2 Score: {:.5f}".format(r2))

    handles, labels = plt.gca().get_legend_handles_labels()
    order = [1, 2, 0]
    plt.legend([handles[i] for i in order], [labels[i] for i in order], loc="lower right")

    plt.savefig("{}.png".format(feature_name))
    elice_utils.send_image("{}.png".format(feature_name))

def main():
    X, y = load_data()
    lr_model = fit_multiple_regression(X, y)

    # TODO: scikit-learn 함수를 통해 R2 Score와 예측값을 구하세요.
    ## (*) y_pred 먼저 구한 후 r2 구하는게 전개상 맞을 듯
    y_pred = lr_model.predict(X)
    r2 = lr_model.score() # .score()을 통해 R2값을 바로 얻을 수 있음 (회귀모델들)
    # r2 = r2_score(y, y_pred) # sklearn.metrics의 r2_score 이용버전. y_true, y_pred 순서

    feature_names = ["sepal_length", "sepal_width", "petal_length"]
    for i in range(len(feature_names)): # 각 피쳐(변수)별로 그래프 그리기
        plot_result(X.iloc[:, i], y, y_pred, r2, feature_name=feature_names[i])
        
    return lr_model

if __name__ == "__main__":
    main()