## 다항 회귀 ##

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 앞의 load_data() 함수들과 비슷
def load_data():
    X = np.linspace(0, 10, num=200) # X는 0에서 10 사이에서 일정한 간격으로 200개를 생성하고,
    y = np.sin(X) + np.random.normal(scale=0.3, size=X.shape) # y는 각 X 값에 sin 함수를 취한 후 Gaussian noise를 더한 값으로 생성합니다.

    X = X[:, np.newaxis] # 차원 1->2차원으로

    return X, y

## X에 있는 각 값들을 n차 다항식으로 바꿔주는 함수입니다.
# 하나의 x값을 [x^0, x^1, ..., x^n]으로 바꿔주는 역할
def to_polynomial(X, n=4):
    X = X.flatten() # 2차원인 X를 다시 1차원으로 바꿔줌
    poly_X = np.empty([0, n + 1])
    # print(poly_X.shape) : (0,5)
    # empty, unlike zeros, does not set the array values to zero, and may therefore be marginally faster
    for x in X: # X는 총 200개
        # TODO: x의 값을 x^0부터 x^n까지 계산한 결과의 배열로 바꾸세요.
        x = np.array([x**m for m in range(n+1)])
        
        x = x[np.newaxis, :] # (1,n)
        poly_X = np.append(poly_X, x, axis=0) # numpy 배열들을 append
    # print(poly_X.shape) : (200,5)
    return poly_X 

## 선형 회귀 모델을 학습합니다.
def run_linear_regression(X, y):
    lr_model = LinearRegression().fit(X, y) # 선형모델 학습

    linear_r2 = lr_model.score(X, y) # R2 값 
    linear_y_pred = lr_model.predict(X) # 예측값
    
    return lr_model, linear_y_pred, linear_r2

## 다항 회귀 모델을 학습합니다..
def run_polynomial_regression(X, y):
    # X의 각 값들을 N차 다항식으로 바꿔줍니다.
    X = to_polynomial(X)
    pr_model = LinearRegression().fit(X, y) # 다항 회귀모델 학습

    poly_r2 = pr_model.score(X, y) # R2 값 
    poly_y_pred = pr_model.predict(X) # 예측값
    
    return pr_model, poly_y_pred, poly_r2

# 데이터와 학습된 다항식을 함께 그래프로 그립니다.
def plot_result(X, y, y_pred, r2, regression_type="linear"):
    fig = plt.figure()
    plt.title("{} Regression Result".format(regression_type.title()))

    plt.scatter(X, y, color="deepskyblue", label="Data Point") # 실제 데이터를 scatter로
    plt.plot(X, y_pred, linewidth=3, color="lightcoral", label="Predicted Line") # 예측값을 실선으로
    plt.plot([], [], ' ', label="R2 Score: {:.5f}".format(r2))

    handles, labels = plt.gca().get_legend_handles_labels()
    order = [2, 0, 1]
    plt.legend([handles[i] for i in order], [labels[i] for i in order], loc="lower right")

    plt.savefig("{}.png".format(regression_type))

def main():
    X, y = load_data() # 데이터 로드
    lr_model, linear_y_pred, linear_r2 = run_linear_regression(X, y) # 선형회귀 모델의 결과
    pr_model, poly_y_pred, poly_r2 = run_polynomial_regression(X, y) # 다항회귀 모델의 결과

    # 위의 결과들로 그림그리기
    plot_result(X, y, linear_y_pred, linear_r2, regression_type="linear")
    plot_result(X, y, poly_y_pred, poly_r2, regression_type="polynomial")

    return lr_model, pr_model

if __name__ == "__main__":
    main()