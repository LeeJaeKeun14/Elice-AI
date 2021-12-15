## 월드컵 매치 데이터 전처리 ##

import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
'''
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
'''
world_cups_matches = pd.read_csv('WorldCupMatches.csv')
# WorldCupMatches.csv 파일의 경우 앞의 WorldCup.csv와는 다른 데이터!

print("전처리 이전:")
print("Germany FR: {}".format(world_cups_matches.isin(["Germany FR"]).sum().sum()))
print("C�te d'Ivoire: {}".format(world_cups_matches.isin(["C�te d'Ivoire"]).sum().sum()))
print("rn\">Bosnia and Herzegovina: {}".format(world_cups_matches.isin(["rn\">Bosnia and Herzegovina"]).sum().sum()))
print("rn\">Serbia and Montenegro: {}".format(world_cups_matches.isin(["rn\">Serbia and Montenegro"]).sum().sum()))
print("rn\">Trinidad and Tobago: {}".format(world_cups_matches.isin(["rn\">Trinidad and Tobago"]).sum().sum()))
print("rn\">United Arab Emirates".format(world_cups_matches.isin(["rn\">United Arab Emirates"]).sum().sum()))
print("Soviet Union: {}".format(world_cups_matches.isin(["Soviet Union"]).sum().sum()))


## Q1. 데이터 프레임의 일부 값을 replace 함수를 사용해 교체
# world_cups_matches = world_cups_matches.replace('Germany FR', 'Germany') # 한개만 바꿀 경우
world_cups_matches = world_cups_matches.replace({'Germany FR':'Germany',"C�te d'Ivoire":"Côte d'Ivoire",
                                                 'rn”>Bosnia and Herzegovina':'Bosnia and Herzegovina',
                                                 'rn”>Serbia and Montenegro':'Serbia and Montenegro',
                                                 'rn”>Trinidad and Tobago':'Trinidad and Tobago',
                                                 'rn”>United Arab Emirates':'United Arab Emirates',
                                                 'Soviet Union':'Russia'}) # 여러개를 동시에 바꿀 경우
                                                 # inplace = True를 통해 바로 replace 가능

print("\n전처리 이후:")
print("Germany FR: {}".format(world_cups_matches.isin(["Germany FR"]).sum().sum()))
print("C�te d'Ivoire: {}".format(world_cups_matches.isin(["C�te d'Ivoire"]).sum().sum()))
print("rn\">Bosnia and Herzegovina: {}".format(world_cups_matches.isin(["rn\">Bosnia and Herzegovina"]).sum().sum()))
print("rn\">Serbia and Montenegro: {}".format(world_cups_matches.isin(["rn\">Serbia and Montenegro"]).sum().sum()))
print("rn\">Trinidad and Tobago: {}".format(world_cups_matches.isin(["rn\">Trinidad and Tobago"]).sum().sum()))
print("rn\">United Arab Emirates".format(world_cups_matches.isin(["rn\">United Arab Emirates"]).sum().sum()))
print("Soviet Union: {}".format(world_cups_matches.isin(["Soviet Union"]).sum().sum()))

## Q2. 데이터 프레임에 중복된 데이터가 얼마나 있는지 확인 & 중복값을 제거
# print(world_cups_matches.duplicated()) # 중복된 데이터일 경우 True, unique한 데이터일 경우 False
# -> 기본적으로 중복값이 있으면 첫번째 값을 duplicated 여부를 False로 반환하고, 나머지 중복값에 대해 True를 반환. keep='first'가 deafault이기 때문
# keep='last'로 설정하면 맨 마지막값만 True로 반환하고, keep=False로 설정하면 중복값은 무조건 False로 반환
dupli = world_cups_matches.duplicated() # flag 
print("\n중복된 값 개수: {}".format(len(dupli[dupli == True]))) # 중복된 데이터의 개수 확인: 16
# print(dupli[dupli == True].shape[0]) # 행의 개수를 통해서도 중복된 데이터의 개수를 확인할 수 있음 (보다 직관적이서 개인적으론 이렇게 더 많이 씀)

# 중복된 데이터 제거
world_cups_matches = world_cups_matches.drop_duplicates()
# world_cups_matches.drop_duplicates(inplace=True) # inplace=True를 통해 바로 중복된 데이터 제거 가능
print(world_cups_matches.shape) # 중복된 데이터를 제거한 후 행과 열 크기 확인 (836, 20)
