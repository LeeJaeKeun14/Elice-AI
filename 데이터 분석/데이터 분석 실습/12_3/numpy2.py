import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
## 실습 전 Quiz
## 2번째 행은? [4,5,6]
## 1번째 열은? [1,4,7]
## array1의 3행 2열 값은? 8 

# array1 첫 번째 column 벡터와 두 번째 column 벡터를 더하여 봅시다.
array2 = array1[:,0] + array1[:,1]
print("1st column of array1 + 2nd column of array1:\n", array2)

# array1 첫 번째 row 벡터와 두 번째 row 벡터를 빼 봅시다.
array3 = array1[0,:] - array1[1,:]
## Quiz2. 
## 두 컬럼 벡터의 합인 array2의 차원은? 1
## array2의 shape는? (3,)
## 두 행 벡터의 빼기인 array3의 차원은? 1
## array3의 shape는? (3,)
# ※ 주의) np.array([1,2,3])와 같은 형태는 shape가 (1,3)이라고 생각할 수 있으나 1차원이므로 shape는 (3,)이 되어야한다.
# --> shape가 (1,3)이 되긴위해서는 np.array([[1,2,3]])와 같은 2차원의 형태이어야한다.
print("\n1st row of array1 - 2nd row of array1:\n", array3)

# array2과 array3을 곱하여 봅시다.
array4 = array2 * array3
print("\narray2 * array3:\n", array4)

array5 = np.c_[array2,array3,array4]
## Quiz3.
## array5의 shape는? (3,3)
## np.c_[array1,array3,array4]의 shape는? (3, 5)
## np.r_[array1,array3,array4]는? error 발생(all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)) => np.r_[array1,array3.reshape(1,3),array4.reshape(1,3)] 로 해줘야함

# array1을 array5로 나누어 봅시다.
array6 = array1 / array5
print("\narray1 / array5:\n", array6)
## 실제 행렬간 나눗셈은 존재하지 않음. 
## cf. 실제 행렬 곱(dot product): array1 @ array5, np.dot(array1, array5)
## Quiz4.
## np.c_[array1,array3,array4] @ array5 의 shape는? 
## np.c_[array1,array3,array4]의 shape는 (3,5)이고 array5의 shape는 (3,3)이기 떄문에 행렬곱 불가능
## array5 @ np.c_[array1,array3,array4]는 가능? 가능하며 이때의 shape는 (3,5)

