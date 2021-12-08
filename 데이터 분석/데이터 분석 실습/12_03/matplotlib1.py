##### [실습7] Matplotlib으로 기본 그래프 그리기 #####

import numpy as np
import pandas as pd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def main():
    
    x = np.arange(10)
    
    # 초기 figure와 축을 설정합니다.
    fig, ax = plt.subplots() # default: plt.subplots(1,1)
    
    # y = x 그래프를 그립니다. 따라서 x 데이터는 x, y 데이터도 x로 설정합니다.
    # label은 'y=x'로 설정하고, 마커는 'o', 마커 색깔은 'blue', 그래프의 선 스타일은 ':'로 설정합니다.
    ax.plot(
        x, x,
        label = 'y=x',
        marker = 'o',
        color = 'blue', # color='b'로도 나타낼 수 있음
        linestyle = ':'
    )
    # cf) 선의 색깔, 마커, 선의 스타일을 한번에 나타내는 법
    # ax.plot(
    #     x, x,'bo:', # 색깔 마커 선스타일 순서대로 작성
    #     label = 'y=x',
    # )
    # ※) color, marker, linestyle은 입력할 수 있는 값들이 정해져있음. 모든 입력대로 그려주는 것이 아님.
    
    # y = x^2 그래프를 그립니다. 따라서 x 데이터는 x, y 데이터는 x**2으로 설정합니다.
    # label은 'y=x^2'로 설정하고, 마커는 '^', 마커 색깔은 'red', 그래프의 선 스타일은 '--'로 설정합니다.
    ax.plot(
        x, x**2,
        label = 'x**2',
        marker = '^',
        color = 'red', # color='r'로도 나타낼 수 있음
        linestyle = '--'
    )
    # Quiz1. 선의 색깔, 마커, 선의 스타일을 한번에 나타내기
    # ax.plot(x, x**2, 'r^--', label='x**2') 
    # Quiz2. y=x+5 그래프를 그립시다. 따라서 x 데이터는 x, y 데이터는 x+3으로 설정합시다.
    # label은 'y=x+5'로 설정하고, 마커는 '*', 마커 색깔은 'green', 그래프의 선 스타일은 '-.'로 설정합니다.
    # ax.plot(x,x+3,'g*-.',label='y=x+3')
    
    # 그래프 제목을 'Graph'로 설정합니다.
    ax.set_title('Graph') # cf) plt의 경우 plt.title()
    # 같은 상황에서도 plt일 때와 ax일 때의 사용 함수들이 다르니 이 점 생각하면서 코드 작성.
    
    # x label은 'x', y label은 'y'로 설정합니다.
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # x 범위는 0부터 10까지, y 범위는 0부터 100까지로 설정합니다.
    ax.set_xlim(0,10) # xlimit
    ax.set_ylim(0,100) # ylimit
    # cf) ax.set_xlim(0,5) ; ax.set_ylim(0,50)으로 설정하면 그래프가 잘린 채로 나타남
    
    # 범례의 위치는 'upper left'로 하고, 그림자 효과는 넣고, 테두리는 둥글게 합니다.
    ax.legend(
        loc = 'upper left', # 'best', 'upper right', 'center' ... 다양하게 설정 가능
        shadow = True,
        fancybox = True
    )
    
    # figure를 "plot.png"라는 이름으로 저장하세요.
    fig.savefig('plot.png')
    
    # 엘리스 플랫폼에서 그래프를 출력하기 위한 코드입니다.
    elice_utils.send_image("plot.png")

if __name__ == "__main__":
    main()
