## Mean Squared Error와 Mean Absolute Error ##

from elice_utils import EliceUtils

elice_utils = EliceUtils()

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import sklearn
# from sklearn.metrics import mean_squared_error, mean_absolute_error

## 선형 회귀 모델을 훈련할 데이터를 생성합니다.
def load_data(num_samples=100):
    X = np.linspace(0, 10, num=num_samples) # X는 0에서 10 사이에서 일정한 간격으로 num_samples 만큼 생성
    y = X + np.random.normal(scale=1.5, size=(num_samples,)) # y는 각 X 값에 Gaussian noise를 더한 값으로 생성
    # print(X.shape, y.shape) # (100,) (100,)

    # 선형 회귀 모델에 적용하기 위해 차원을 확장합니다. (1차원 -> 2차원으로. 내용 구성물들은 같음)
    # sklearn의 LinearRegression이 1차원의 형태로 안 받기 때문에 차원 조작
    X = X[:, np.newaxis]
    y = y[:, np.newaxis]
    # print(X.shape, y.shape) # (100,1) (100,1)

    return X, y
    
## 선형 회귀 모델을 학습합니다.
# sklearn의 LinearRegression 함수를 이용 & fit 함수를 통해 훈련 진행
def fit_linear_regression(X, y):
    lr_model = LinearRegression().fit(X, y)
    
    return lr_model # 주어진 X,y로 훈련시킨 선형 회귀 모델

## MSE를 구합니다.
# MSE의 식을 보면, MAE보다 큰 오류에 대해서 더 민감하게 반응할 것을 알 수 있음(제곱때문)
# -> 큰 오류에 대해선 더 크게, 작은 오류에 대해선 더 작게 반응하게 만듦
# -> 그만큼 특이치에 더 민감하게 반응
def mean_squared_error(y_true, y_pred):
    num_data = len(y_true)

    # TODO: MSE를 구현하세요.
    mse = np.sum(np.square(y_true - y_pred)) / num_data # 왼쪽 공식을 그대로 코드화시킨 경우
    # np.sum 대신 그냥 sum을 이용하면 mse가 숫자형태가 아니라 array안에 숫자가 들어있는 형태([mse])를 띤다.(2차원 형태이기 때문에) 따라서 한번 더 꺼낼거아니면 np.sum을 사용
    # mse = np.mean(np.square(y_true - y_pred)) # 보다 더 간단히 나타낸 경우
    # mse = sklearn.metrics.mean_squared_error(y_true, y_pred) # sklearn 사용 버전. from sklearn.metrics import mean_squared_error
    # print(mse)

    return mse

## MAE를 구합니다.
# MSE에 비해 특이치에 민감하게 반응하지 않음
def mean_absolute_error(y_true, y_pred):
    num_data = len(y_true)

    # TODO: MAE를 구현하세요.
    mae = np.sum(np.abs(y_true - y_pred)) / num_data # 왼쪽 공식을 그대로 코드화시킨 경우
    # mae = np.mean(np.abs(y_true - y_pred)) # 보다 더 간단히 나타낸 경우
    # mae = sklearn.metrics.mean_absolute_error(y_true, y_pred) # sklearn 사용 버전. from sklearn.metrics import mean_absolute_error
    # print(mae)

    return mae

## 데이터와 학습된 직선을 함께 그래프로 그립니다.
def plot_result(X, y, y_pred, mse, mae):
    plt.title("Result")
    plt.scatter(X, y, color="deepskyblue", label="Data")
    plt.plot(X, y_pred, linewidth=3, color="lightcoral", label="Predicted Line")
    plt.plot([], [], ' ', label="MSE: {:.5f}".format(mse))
    plt.plot([], [], ' ', label="MAE: {:.5f}".format(mae))

    handles, labels = plt.gca().get_legend_handles_labels()
    order = [3, 0, 1, 2]
    plt.legend([handles[i] for i in order], [labels[i] for i in order], loc="lower right")

    plt.savefig("result.png")
    elice_utils.send_image("result.png")

def main():
    ## 데이터를 불러옵니다.
    X, y = load_data() # 위에서 설정한 load_data 함수
    
    ## 선형 회귀 모델을 불러와 학습시킵니다.
    lr_model = fit_linear_regression(X, y) # 위에서 설정한 fit_linear_regression 함수. X,y 데이터를 이용해 훈련시킨 선형회귀 모형 반환(lr_model)

    ## 학습된 선형 회귀 모델의 예측값을 구합니다.
    y_pred = lr_model.predict(X) # predict 함수를 통해 X에 대한 y의 값들을 예측

    ## MSE와 MAE를 구합니다.(실제값과 예측한 값들을 이용하여 오차 계산)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    # 실제로는 mse에 root를 씌운 RMSE를 많이 사용 -> robust한 특징때문

    print("Mean Squared Error : {:.5f}".format(mse))
    print("Mean Absolute Error: {:.5f}".format(mae))

    ## 결과를 그래프로 그립니다.
    plot_result(X, y, y_pred, mse, mae)

    return lr_model

if __name__ == "__main__":
    main()