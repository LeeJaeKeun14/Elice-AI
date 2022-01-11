import pandas as pd
import numpy as np

def recommendations(titles):

    ## 제목, 가중치평점만 있는 데이터
    df = pd.read_csv("./data/title_evaluation.csv")

    ## title 의 id(index) 를 찾는 코드
    indexes = []
    for title in titles:
        indexes.append(df[df.제목 == title].index[0])

    ## 특징 유사도 매트릭스
    similar_indexes = pd.read_csv(f"./data/genre_sim_matrix.csv")
    similar_indexes = np.array(similar_indexes)[indexes,:]
    similar_indexes = similar_indexes.reshape(-1)
    similar_indexes = set(similar_indexes)
    similar_indexes = np.array(list(similar_indexes))
    for i in indexes:
        similar_indexes = similar_indexes[similar_indexes != i]  # 타이틀 기준 제거

    return df.iloc[similar_indexes].sort_values("가중치평점", ascending=False)[:20][["제목", "가중치평점"]]
