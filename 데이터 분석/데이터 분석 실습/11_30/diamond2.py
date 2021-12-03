## 고품질 다이아몬드 가격 인상하기

from elice_utils import EliceUtils

elice_utils = EliceUtils()

from read_data import read_above_3000
from itertools import repeat
                
# TODO: 지시사항 3번의 map에서 활용할 가격 증가 함수를 완성하세요.
## 여기서 d는 high_quality_diamonds 리스트에 들어있는 각각의 딕셔너리들
def increase_price(d, n):
    d['price'] = d['price'] * n ## 다이아몬드의 가격(price)를 n배로 증가
    ## d['price'] *= n
    return d

def main():
    ## 'price' key가 3000이상인 딕셔너리들의 모음(list)
    above_3000 = read_above_3000() 
    
    # TODO: above_3000에서 cut, color, clarity의 최대값을 구하세요.
    max_cut = max([d['cut'] for d in above_3000]) ## max(list(map(lambda d : d['cut'], above_3000)))
    max_color = max([d['color'] for d in above_3000])
    max_clarity = max([d['clarity'] for d in above_3000])
    
    # TODO: cut, color, clarity가 모두 최대값인 다이아몬드들만 골라내세요.
    ## above_3000 list에 들어있는 각각의 딕셔너리들에 대해 딕셔너리의 'cut' key가 max_cut, 'color' key가 max_color, 'clarity' key가 max_clarity인 딕셔너리들만 통과시킴
    high_quality_diamonds = list(filter(lambda d: (d['cut']==max_cut) & (d['color']==max_color) & (d['clarity']==max_clarity), above_3000))
    ## list(filter(lambda d:d["cut"]==max_cut and d["color"]==max_color and d["clarity"]==max_clarity, above_3000))
    
    # TODO: 고품질 다이아몬드들의 가격을 10배로 인상하세요.
    ## == list(map(increase_price, high_quality_diamonds, [10]*20))
    high_quality_diamonds_10_times = list(map(increase_price, high_quality_diamonds, repeat(10)))
    ## == list(map(increase_price, high_quality_diamonds, [10]*20)) 
    ## [increase_price(d, 10) for d in high_quality_diamonds]
    
    return max_cut, max_color, max_clarity, high_quality_diamonds, high_quality_diamonds_10_times

if __name__ == "__main__":
    main()