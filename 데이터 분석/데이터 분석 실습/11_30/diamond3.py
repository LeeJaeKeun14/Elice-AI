## 캐럿 상위 20% 다이아몬드의 가격 통계

from elice_utils import EliceUtils

elice_utils = EliceUtils()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from read_data import read_diamonds

def plot_price_histogram(top_20_percent_carat, mean_carat, stdv_carat):
    bins = np.linspace(0.5, 3.5, num=100)
    sns.histplot(top_20_percent_carat, bins=bins)
    plt.plot([], [], ' ', label="Mean: {:.5f}".format(mean_carat))
    plt.plot([], [], ' ', label="Stdv: {:.5f}".format(stdv_carat))
    plt.legend(loc="upper right")
    plt.savefig("price.png")
    elice_utils.send_image("price.png")

def main():
    diamonds = read_diamonds() ## 전체 다이아몬드 딕셔너리들의 모음(list)
    
    # TODO: 다이아몬드들을 가격이 높은 순으로 정렬하세요.
    ## 정렬해야하므로 sorted 함수 이용
    ## 가격이 높은 순으로 정렬하기 때문에 reverse 이용
    diamonds = sorted(diamonds, key=lambda d: d['price'], reverse=True)
    ## == sorted(diamonds, key=lambda d: -d["price"])
    
    # TODO: 가격 상위 20% 다이아몬드들의 캐럿을 가져오세요.
    num_20_percent = int(len(diamonds) * 0.2)
    top_20_percent = diamonds[:num_20_percent]
    top_20_percent_carat = [d['carat'] for d in top_20_percent]
    
    # TODO: 가격 상위 20% 다이아몬드들 캐럿의 평균과 표준편차를 구하세요.
    # ※ 루트의 경우 math.sqrt 이용
    mean_carat = sum(top_20_percent_carat)/len(top_20_percent_carat) # np.mean(top_20_percent_carat)
    stdv_carat = math.sqrt(sum([(c-mean_carat)**2 for c in top_20_percent_carat])/len(top_20_percent_carat)) # np.std(top_20_percent_carat)
    
    # 히스토그램으로 캐럿 분포를 그립니다.
    ## 가격 상위 20%인 다이아몬드들의 캐럿 분포. mean이랑 std는 legend로 설정
    plot_price_histogram(top_20_percent_carat, mean_carat, stdv_carat)
    
    return diamonds, top_20_percent_carat, mean_carat, stdv_carat

if __name__ == "__main__":
    main()