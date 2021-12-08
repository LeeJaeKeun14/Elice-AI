##### [실습8] Matplotlib으로 다양한 그래프 그리기 #####

import numpy as np
import matplotlib.pyplot as plt
import csv

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def main():
    
    data_x = []
    data_y = []
    
    with open('./data/data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_x.append(float(row[0]))
            data_y.append(float(row[1]))
    
    # 2x2개의 그래프를 그릴 수 있는 초기 figure와 축을 설정합니다.
    fig, axes = plt.subplots(2,2) # 2개의 행 & 2개의 열로 구성된 subplots
    
    """
    Scatter 그래프 그리기
    """
    
    colors = np.random.randint(0,100,500)
    # figure의 (0,0) 위치에 scatter 그래프를 그립니다.
    # x 데이터는 data_x, y 데이터는 data_y, 데이터 포인트의 색깔은 colors, 사이즈는 2, 투명도는 0.7로 설정합니다.
    axes[0,0].scatter(
        data_x, data_y,
        c = colors, # color로 설정할 경우 For a sequence of values to be color-mapped, use the 'c' argument instead.라는 에러 발생
        s = 2, 
        alpha = 0.7
    )
    # 위의 경우는 각 점별로 색깔을 다르게 하기 위해 c라는 인자를 주었지만, 하나의 색으로 나타내고자 한다면 color 쓰면 됨
    # axes[0,0].scatter(
    #     data_x, data_y,
    #     color = 'red',
    #     s = 2, 
    #     alpha = 0.7
    # )
    
    
    """
    Bar 그래프 그리기
    """
    
    bar_x = np.arange(10)
    
    # figure의 (0,1) 위치에 Bar 그래프를 그립니다.
    # x 데이터는 bar_x, y 데이터는 bar_x**2로 설정합니다.
    axes[0,1].bar(
        bar_x, bar_x**2 # color='green'와 인자를 추가하여 bar 전체의 색깔을 바꿀 수 있음
    )
    # bar_x에 존재하는 x들의 위치에 corresponding한 y값들(bar_x**2)을 그려주는 것임
    
    """
    Multi-Bar 그래프 그리기
    """
    ## 누적 막대 차트 그리기 (bottom) 라는 것을 미리 알려주기
    
    x = np.array([3,2,1])
    y = np.array([2,3,2])
    z = np.array([1,3,4])
    data1 =  [x, y, z]

    x_ax =  np.arange(3) # x들의 위치 겸 stack할 값(x,y,z)들의 개수
    
    # 누적 막대 그래프 -> 막대를 여러번 쌓는 것. for문을 통해 bar 그래프를 여러번 쌓음
    for i in x_ax:
        # figure의 (1,0) 위치에 Bar 그래프를 그립니다.
        # x 데이터는 x_ax, y 데이터는 각각 x,y,z로 설정합니다.
        axes[1,0].bar(
            x_ax, data1[i],
            bottom=np.sum(data1[:i], axis=0) # bottom: 해당 barplot을 어느정도 높이에서 그릴지 설정 가능
            # 해당 데이터 전까지 해당 위치에서 stacked된 값을 bottom값으로 사용 
        ) # axes[1,0]에 해당하는 plot에 bar plot 3개를 그린 것임
        
        
    # figure의 (1,0) 위치에서 x축 데이터를 병렬적으로 설정합니다.
    axes[1,0].set_xticks(x_ax)
    
    # figure의 (1,0) 위치에서 x축 label을 'A', 'B', 'C'로 설정합니다.
    # 설정하지 않을 경우 기본 값인 0, 1, 2로 label이 설정됨
    # ※주의) x-label을 설정(set_xticklabels)하기 전에 먼저 x-ticks을 설정(set_xticks)해야 함. 왜냐하면 막대 당 하나의 눈금이 붙는 게 기본 값이 아니기 때문
    # x-label 앞에 x-ticks을 설정하는 것을 건너 뛰면 잘못된 위치에 눈금이 생길 수도 있음! (보여주기)
    axes[1,0].set_xticklabels(['A','B','C'])
    
    """
    Histogram 그래프 그리기
    """
    
    data = np.array(data_x)
    
    # figure의 (1,1) 위치에 Histogram 그래프를 그립니다.
    # 입력될 데이터는 data, Histogram 표현시 분할되는 개수는 50으로 설정합니다.
    axes[1,1].hist(data, bins=50) # cf) bar 그래프의 경우 두쌍의 데이터가 필요하나 hist는 하나의 데이터만 필요
    
    # figure를 저장하고 엘리스 플랫폼에서 그래프를 출력합니다.
    fig.savefig("plot.png")
    elice_utils.send_image("plot.png")

if __name__ == '__main__':
    main()