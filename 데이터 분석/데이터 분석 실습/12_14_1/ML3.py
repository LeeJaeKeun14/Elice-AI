## R2 Score ##

from elice_utils import EliceUtils

elice_utils = EliceUtils()

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import sklearn # 추가
# from sklearn.metrics import r2_score

# 앞의 MSE & MAE 실습의 load_data 함수와 거의 똑같음 
# 선형성을 잘 따르는 데이터를 생성합니다.
def load_linear_data(num_samples=100):
    X = np.linspace(0, 10, num=num_samples) # X는 0에서 10 사이에서 일정한 간격으로 num_samples 만큼 생성하고,
    y = X + np.random.normal(scale=0.5, size=(num_samples,)) # y는 각 X 값에 Gaussian noise를 더한 값으로 생성합니다.

    # 선형 회귀 모델에 적용하기 위해 차원을 확장합니다.(1차원 -> 2차원)
    X = X[:, np.newaxis]
    y = y[:, np.newaxis]

    return X, y

# 선형성이 전혀 없는 데이터를 생성합니다.
def load_random_data(num_samples=100):
    X = np.linspace(0, 10, num=num_samples) # X는 0에서 10 사이에서 일정한 간격으로 num_samples 만큼 생성하고,
    y = np.random.normal(loc=5, scale=3, size=(num_samples,)) # y는 평균이 5이고 표준편차가 3인 정규 분포에서 샘플링하여 생성합니다.

    # 선형 회귀 모델에 적용하기 위해 차원을 확장합니다.
    X = X[:, np.newaxis]
    y = y[:, np.newaxis]

    return X, y

# 선형 회귀 모델을 학습합니다.
def fit_linear_regression(X, y):
    lr_model = LinearRegression().fit(X, y)
    
    return lr_model

# R2 Score를 구합니다.
def r2_score(y_true, y_pred):
    # TODO: SSR과 SST를 구하세요.
    # 학문에 따라 SSE(error)라고 하기도하고 SSR(residual)이라 하기도 함
    ssr = np.sum(np.square(y_true - y_pred))
    sst = np.sum(np.square(y_true - np.mean(y_true)))

    # TODO: R2 Score를 구하세요.
    r2 = 1 - ssr/sst
    
    # r2 = sklearn.metrics.r2_score(y_true, y_pred) # sklearn 사용 버전

    return ssr, sst, r2

# 데이터와 학습된 직선을 함께 그래프로 그립니다.
def plot_result(X, y, y_pred, r2, data_type="linear"):
    fig = plt.figure()
    plt.title("{} Data".format(data_type.title()))
    plt.scatter(X, y, color="deepskyblue", label="Data")
    plt.plot(X, y_pred, linewidth=3, color="lightcoral", label="Predicted Line")
    plt.plot([], [], ' ', label="R2 Score: {:.5f}".format(r2))

    handles, labels = plt.gca().get_legend_handles_labels()
    order = [2, 0, 1]
    plt.legend([handles[i] for i in order], [labels[i] for i in order], loc="lower right")

    plt.savefig("{}.png".format(data_type))
    elice_utils.send_image("{}.png".format(data_type))

def main():
    ## 데이터를 불러옵니다.
    X_linear, y_linear = load_linear_data() # 선형성을 잘 따르는 데이터
    X_random, y_random = load_random_data() # 선형성이 전혀 없는 데이터
    
    ## 선형 회귀 모델을 불러와 학습시킵니다.
    # 각 데이터별로(선형성 O & 선형성 X) 회귀모델 학습
    linear_model = fit_linear_regression(X_linear, y_linear)
    random_model = fit_linear_regression(X_random, y_random)

    ## 학습된 선형 회귀 모델의 예측값을 구합니다.-> predict 함수 사용
    y_linear_pred = linear_model.predict(X_linear)
    y_random_pred = random_model.predict(X_random)
    # 여기선 같은 X값을 이용해 모델을 훈련시키고 예측을 하였지만, 사실 실제 모델에서는 훈련용 X와 예측용 X 따로 존재하고 존재해야함.

    ## 각 모델의 R2 Score를 구합니다.
    # r2_score만 필요하므로 ssr, sst 부분은 _로 받는다.
    _, _, linear_r2_score = r2_score(y_linear, y_linear_pred)
    _, _, random_r2_score = r2_score(y_random, y_random_pred)

    print("Linear R2: {:.5f}".format(linear_r2_score))
    print("Random R2: {:.5f}".format(random_r2_score))
    # 선형성이 있는 데이터에서 R2 score가 훨씬 높게 나온 것을 확인 -> 모델의 설명력이 높다는 의미

    ## 결과를 그래프로 그립니다.
    plot_result(X_linear, y_linear, y_linear_pred, linear_r2_score, data_type="linear")
    plot_result(X_random, y_random, y_random_pred, random_r2_score, data_type="random")

if __name__ == "__main__":
    main()
