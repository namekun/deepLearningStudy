# x, y는 전의 linearRegression에서 사용했던 것들 사용
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
x = diabetes.data[:, 2]
y = diabetes.target

w = 1.0
b = 1.0

y_hat = x[0] * w + b
# print(y_hat)
# print(y[0])

# w값 조절해서 예측값 변경하기
w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b
# print(y_hat_inc)

# 예측값 증가 정도 확인
w_rate = (y_hat_inc - y_hat) / (w_inc - w)
# print(w_rate)

# 변화율로 가중치 업데이트
w_new =  w + w_rate
# print(w_new)

# 변화율로 절편 업데이트
b_inc = b + 0.1 # 0.1 만큼 증가
y_hat_inc = x[0] *  w + b_inc
# print(y_hat_inc)

b_rate = (y_hat_inc - y_hat) / (b_inc - b) # 변화율 계산
# print(b_rate)

b_new = b + 1
# print(b_new)