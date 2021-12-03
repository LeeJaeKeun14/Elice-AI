## 비싼 다이아몬드만 골라내기

from elice_utils import EliceUtils

elice_utils = EliceUtils()

# Feature들은 아래 index 순서대로 저장되어 있습니다.
feature_list = {
    "CARAT"   : 0,
    "CUT"     : 1,
    "COLOR"   : 2,
    "CLARITY" : 3,
    "DEPTH"   : 4,
    "TABLE"   : 5,
    "PRICE"   : 6,
    "X_LENGTH": 7,
    "Y_WIDTH" : 8,
    "Z_DEPTH" : 9,
}

# String으로 이루어진 변수 "cut", "color", "clarity"를 정수로 바꾸기 위한 딕셔너리입니다.
# 좋은 정도가 높을수록 큰 숫자를 가집니다.
cut_list = {
    "Ideal"    : 5,
    "Premium"  : 4,
    "Very Good": 3,
    "Good"     : 2,
    "Fair"     : 1,
}
color_list = {"D": 7, "E": 6, "F": 5, "G": 4, "H": 3, "I": 2, "J": 1}
clarity_list = {"FL": 11, "IF": 10, "VVS1": 9, "VVS2": 8, "VS1": 7, "VS2": 6,
                "SI1": 5, "SI2": 4, "I1": 3, "I2": 2, "I3": 1}

# CSV 파일을 그대로 읽어오면 각 줄이 모두 string으로 읽히므로
# 숫자 데이터는 숫자로 바꾸고, 문자열 데이터는 불필요한 따옴표를 제거합니다.

## input(diamond) 형식 ex: ['"0.23"', '"Ideal"', '"E"', '"SI2"', '61.5', '55', '326', '3.95', '3.98', '2.43'] 
def preprocess_data(diamond):
    for i, data in enumerate(diamond):
        # cut, color, clarity는 string feature입니다.
        ## ex. CUT: '"Ideal"' / COLOR: '"E"' / CLARITY: '"SI2"'
        if i == feature_list["CUT"] or i == feature_list["COLOR"] or i == feature_list["CLARITY"]:
            diamond[i] = data.replace('\"','') ## 내부에 불필요한 쌍따옴표를 제거

        # price는 int feature입니다.
        ## ex. PRICE: '326'
        elif i == feature_list["PRICE"]:
            diamond[i] = int(data)

        # 나머지는 float feature입니다.
        else:
            diamond[i] = float(data)
    ## 처리한 diamond 형식 ex.[0.23, 'Ideal', 'E', 'SI2', 61.5, 55, 326, 3.95, 3.98, 2.43] 

# CSV 파일을 읽어와 딕셔너리의 리스트로 저장합니다.
def read_data():
    diamonds = []
    
    with open("./diamonds.csv", "r") as f:
        # TODO: CSV 파일의 첫줄은 feature들의 이름입니다. 이를 리스트로 저장하세요.
        # 첫번째 항목은 빈 항목이므로 이를 제거해야 합니다.
        
        ## ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']
        features = f.readline().replace('\"','').strip().split(',')[1:]
        for line in f:
            # TODO: 각 다이아몬드 데이터를 읽어옵니다.
            # 마찬가지로 첫번째 항목은 인덱스이므로 제거해야 합니다.
            diamond_str = line.strip().split(',')[1:]
            
            preprocess_data(diamond_str)

            # TODO: 각 다이아몬드 데이터를 딕셔너리로 저장하세요.
            diamond = dict()
            for key, value in zip(features, diamond_str):
                diamond[key] = value
            # ex. {'carat': 0.23,'clarity': 'SI2','color': 'E','cut': 'Ideal','depth': 61.5,'price': 326,'table': 55.0,'x': 3.95,'y': 3.98,'z': 2.43}

            diamonds.append(diamond) ## 위의 diamonds list에 각 다이아몬드 데이터 딕셔너리를 저장
            
    return diamonds 

# TODO: 3번 지시사항에서 map 함수의 내부 함수로 사용할 함수입니다.
## cut_list = {"Ideal": 5,"Premium": 4,"Very Good": 3,"Good": 2,"Fair": 1,}
## color_list = {"D": 7, "E": 6, "F": 5, "G": 4, "H": 3, "I": 2, "J": 1}
## clarity_list = {"FL": 11, "IF": 10, "VVS1": 9, "VVS2": 8, "VS1": 7, "VS2": 6,
##                 "SI1": 5, "SI2": 4, "I1": 3, "I2": 2, "I3": 1}
## 여기서 input인 d는 diamonds list에 들어있는 각각의 딕셔너리를 의미. ex. {'carat': 0.23,'clarity': 'SI2','color': 'E','cut': 'Ideal','depth': 61.5,'price': 326,'table': 55.0,'x': 3.95,'y': 3.98,'z': 2.43}
def string_to_int(d):
    d["color"] = color_list[d["color"]] ## ex.'color': 'E' -> 6
    d["clarity"] = clarity_list[d["clarity"]] ## ex. 'clarity': 'SI2' -> 4
    d["cut"] = cut_list[d["cut"]] ## ex. 'cut': 'Ideal' -> 5

    return d ## ex. {'carat': 0.23,'clarity': 4,'color': 6,'cut': 5,'depth': 61.5,'price': 326,'table': 55.0,'x': 3.95,'y': 3.98,'z': 2.43}

def main():
    diamonds = read_data() # list안에 다이아몬드 데이터 딕셔너리들이 들어있는 상태
    
    # TODO: String으로 이루어진 feature들을 정수로 바꿔주세요.
    ## 위의 cut_list, color_list, clarity_list를 이용해 해당하는 문자를 숫자값으로 교체
    ## diamonds list에 들어있는 각각의 딕셔너리들에 string_to_int 함수를 적용
    diamonds = list(map(string_to_int, diamonds))
    
    # TODO: 가격이 3000달러 이상인 다이아몬드만 골라내세요.
    ## diamonds list에 들어있는 각각의 딕셔너리들에 대해 딕셔너리의 'price' key가 3000이상인 딕셔너리들만 통과시킴
    above_3000 = list(filter(lambda d: d["price"] >= 3000, diamonds)) ## 'price' key가 3000이상인 딕셔너리들의 모음(list)
    
    return diamonds, above_3000

if __name__ == "__main__":
    main()
