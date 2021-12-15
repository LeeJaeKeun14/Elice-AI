## 선형 회귀 과정 살펴보기 ##

from elice_utils import EliceUtils

elice_utils = EliceUtils()

import numpy as np
import matplotlib.pyplot as plt

## 정해진 X, y 데이터 로드
def load_data():
    X = np.array([[8.70153760], [3.90825773], [1.89362433], [3.28730045], [7.39333004], [2.98984649], [2.25757240], [9.84450732], [9.94589513], [5.48321616]])
    y = np.array([[5.64413093], [3.75876583], [3.87233310], [4.40990425], [6.43845020], [4.02827829], [2.26105955], [7.15768995], [6.29097441], [5.19692852]])
    
    return X, y

# 예측함수. 주어진 beta_0과 beta_1을 이용하여 X에 대한 y의 값 예측
def prediction(beta_0, beta_1, X):
    
    y_pred = beta_0 + beta_1 * X # 왼쪽 설명란에 있는 선형회귀식
    
    return y_pred

## beta_1와 beta_1 값을 업데이트 하는 규칙을 정의하는 함수입니다.
# 어느정도 업데이트할 것인지. MSE loss에 대한 gradient descent 이용
def update_beta(X, y, y_pred, lr):
    
    delta_0 = -(lr * (2 / len(X)) * np.sum(y - y_pred)) # beta_0은 모든 x에서 공유하므로
    
    delta_1 = -(lr * (2 / len(X)) * (np.dot(X.T, (y - y_pred)))) 
    
    return delta_0, delta_1


# 모델 훈련(학습) 및 최종 beta_0, beta_1 값 반환 
def gradient_descent(X, y, lr, iteration, plot_cycle):
    
    beta_0 = np.zeros((1, 1)) # shape? (1,1). 2차원
    beta_1 = np.zeros((1, 1)) # shape: (1,1). 2차원
    
    for i in range(iteration):
        
        y_pred = prediction(beta_0, beta_1, X)
        # 위에서 사용자가 설정한 prediction 함수를 이용하여 주어진 X값들에 대한 y의 값 예측
        # 바로 전 iteration(i-1)에서 업데이트하였던 beta_0, beta_1을 이용하여 y값 예측
        loss = np.mean(np.square(y - y_pred))
        # MSE(mean squared error)를 loss로 설정
        # np.square: 배열에있는 모든 요소의 제곱을 계산. cf. np.sqrt: 제곱근을 반환
        
        beta0_delta, beta1_delta = update_beta(X, y, y_pred, lr) 
        # 위에서 사용자가 설정한 update_beta 함수를 이용하여 beta_0, beta_1 값을 어느정도 업데이트 했는지 반환 (beta0_delta, beta1_delta)
        # 이들을 이용하여 beta_0과 beta_1 값 업데이트
        beta_0 -= beta0_delta
        beta_1 -= beta1_delta
        
        # plot_cycle번의 학습마다 그래프 출력하기 (저장)
        # 저장한 그래프들은 나중에 main 부분에서 gif 형태로 묶어줄거임
        if i % plot_cycle == 0:
            plotting_graph(X, y, beta_0, beta_1, i)
        
    return beta_0, beta_1 # 총 학습횟수(iteration)만큼 학습(beta 업데이트)가 진행된 후 최종적인 beta_0, beta_1 값

## 그래프를 시각화하는 함수입니다.
def plotting_graph(X, y, beta_0, beta_1, i):
    
    y_pred = beta_0 + beta_1[0,0] * X
    
    fig = plt.figure()
    
    plt.scatter(X, y)
    plt.title("Iteration: {}".format(i))
    plt.ylim(0, 8)
    plt.plot(X, y_pred,c='r')
    
    plt.savefig("test_{}.png".format(i))

## 회귀 알고리즘 구현 진행을 위한 main() 함수입니다.  
def main():
    
    ## 학습을 위해 필요한 파라미터와 데이터입니다. 
    lr = 1e-4 # learning rate
    iteration = 1000 # 총 학습 횟수입니다.
    plot_cycle = 100 # 그래프를 그릴 주기입니다.
    
    X, y = load_data() # X, y 데이터 로드
    
    beta_0, beta_1 = gradient_descent(X, y, lr, iteration, plot_cycle)
    # 위에서 사용자가 설정한 gradient_descent 함수를 이용하여 학습 진행 및 그래프 저장 & 최종 beta_0, beta_1 값 반환
    
    print("{}번의 학습 이후의 회귀 알고리즘 결과".format(iteration))
    print("beta_0: {}, beta_1: {}".format(beta_0[0], beta_1[0]))
    
    plotting_graph(X, y, beta_0, beta_1, iteration) # 최종 beta_0, beta_1를 이용하여 그래프를 그림

    ## 그린 그래프를 GIF로 변환합니다.
    graphs = []
    filenames = ["test_{}.png".format(iter) for iter in range(0, iteration + 1, plot_cycle)] # gradient_descent 함수에서 저장했던 그래프들
    for filename in filenames:
        graphs.append(imageio.imread(filename)) # 그래프(이미지)를 읽어서 graphs 모음집으로
    imageio.mimsave("test.gif", graphs, duration=0.2) # 그래프 모음집 graphs를 이용하여 gif 짤 만들기
    elice_utils.send_image("test.gif")
    
    return beta_0, beta_1

if __name__=="__main__":
    from utils import install_imageio
    install_imageio()
    
    import imageio
    main()