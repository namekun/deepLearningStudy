# slope = 기울기 , intercept = 절편
# 선형회귀는 x,y가 주어졌을때, 기울기와 절편을 찾아 내는 것입니다
#
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

# data 크기 확인
print(diabetes.data.shape, diabetes.target.shape)

# data slicing
print(diabetes.data[0:3])
print(diabetes.target[:3])

# data visualization
import matplotlib.pyplot as plt

plt.scatter(diabetes.data[:,2], diabetes.target) # [:} 은 데이터의 전체를 사용한다는 의미
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# data 변수에 save
x = diabetes.data[:, 2]
y = diabetes.target