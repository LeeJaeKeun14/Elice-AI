import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
## Quiz1
## x의 차원과 shape는? 1차원, (9,)

# 배열 x를 reshape를 사용하여 (3,3) 배열로 변환해봅시다.
array1 = x.reshape(3,3) # np.reshape(x,(3,3))
print("(3x3) 배열 x:\n", array1)
## Quiz. x.reshape(-1,3)의 shape는? (3,3)

# 변환된 배열 array1의 2번째 column을 구해봅니다. 
# (3, 1) 형태로 array2에 저장합니다.

array2 = array1[:,1].reshape(3,1)
print("\narray1의 2번째 column :\n", array2)
## array1[:,1]는 1 dimension & shape:(3,)
## array2는 2 dimension & shape:(3,1)

# array1에 column 방향으로 array2를 붙여봅니다.
array3 = np.c_[array1,array2]
print("\narray1에 column 방향으로 array2 붙이기:\n", array3)
## Quiz2
## np.concatenate를 이용하면? np.concatenate([array1,array2], axis=1)
## np.concatenate([array1,array2], axis=0) 가능하나? 불가능
## --> array1.shape:(3,3), array2.shape:(3,1) => 두 array의 경우 행의 크기는 같아서 열의 방향으로는 데이터를 붙일 수 있으나, 열의 크기는 달라서 행의 방향으로는 데이터를 붙일 수는 없음
## 행의 방향으로 두 array를 붙이기 위해서는 np.concatenate((array1,array2.reshape(1,3)),axis=0)에서와 같이 array2의 shape를 (1,3)으로 reshape시켜야함 (np.r_에서도 마찬가지)

# array3을 reshape를 사용하여 (3,2,2) 배열로 변환해봅시다.
array4 = array3.reshape(3,2,2)
print("\n(3,2,2) array4:\n", array4)

# array4의 3개의 (2,2)행렬 중 첫 번째 행렬을 구합니다.
array5 = array4[0] # array4[0,:,:]
print("\narray4의 3개의 (2,2)행렬 중 첫 번째 행렬:\n", array5)
## Quiz3
## array4의 3개의 (2,2)행렬 중 2번째 행렬의 2번쨰 열을 구하면?
## array4[1,:,1]
## array4의 3개의 (2,2)행렬 중 전체 행렬들의 1번쨰 행을 구하면?
## array4[:,0,:]

