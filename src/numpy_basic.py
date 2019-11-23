import numpy as np
print(np.__version__)

# 넘파이로 배열만들기

my_arr = np.array([[10, 20, 30],[1, 3, 4]])
print(my_arr)
print(my_arr[0][2])

# type 확인
print(type(my_arr))

# numpy sum
np.sum(my_arr)