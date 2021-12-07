import numpy as np

x=[[1,2,3], [4,5,6], [7,8,9]]

def solution(data):
    #리스트 x를 Numpy 배열로 출력합니다.
    array1 = np.array(x)

    #모든 원소가 0인 3×3의 배열을 출력합니다.
    array2 = np.zeros((3,3))
    # cf) array2 = np.zeros(3,3) -> error 발생.

    #모든 원소가 1인 2×5의 배열을 출력합니다.
    array3 = np.ones((2,5))
    # cf) array3 = np.ones(3,3) -> 마찬가지로 error 발생.

    # 0 이상 1 미만의 랜덤 값을 갖는 5×3의 배열을 출력합니다.
    array4 = np.random.random((5,3))    

    # 0부터 9까지의 값을 원소로 하는 1×10 배열을 출력합니다.
    array5 = np.arange(10) # np.arange(0,10,1)
    # 다양한 정답이 존재하니 하나의 코드만 맞다고 생각하지 말 것!
    
    ## Quiz1: array1과 array5의 차원(dimension)은? 
    ## print(array2.ndim, array5.ndim) <- ndim을 쓰면 행렬의 차원을 알 수 있음
    ## [ ] 괄호의 개수로도 행렬의 차원을 알 수 있음
    
    
    return array1, array2, array3, array4, array5

def print_answer(**kwargs):
    for key in kwargs.keys():
        print(key,":", kwargs[key])

array1, array2, array3, array4, array5 = solution(x)

print_answer(array1=array1, array2=array2, array3=array3, array4=array4, array5=array5)