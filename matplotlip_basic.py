import numpy as np
import matplotlib.pyplot as plt

# 1. 선그리기
# plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
# plt.show()

# 2. 산점도 그리기
# plt.scatter([1, 2, 3, 4, 5], [1,4,9,16,25])
# plt.show()

# 3. 넘파일 배열로 산점도 그리기
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y)
plt.show()