# 오차 역전파
# 이름에서 알 수 있듯 오차가 연이어 전파되는 모습으로 수행된다.

from src import gradient_descent as g
import matplotlib.pyplot as plt

# 1. 오차의 변화율을 곱하여 가중치 업데이트하기
err = g.y[0] - g.y_hat
w_new = g.w + g.w_rate * err
b_new = g.b + 1 * err
# print(w_new, b_new)

# 2. 두번째 샘플을 사용해서 오차를 구하고, 새로운 w와 b 구하기
y_hat = g.x[1] * w_new + b_new
err = g.y[1] - y_hat
w_rate = g.x[1]
w_new = w_new + w_rate * err
b_new = b_new + 1 * err
# print(w_new, b_new)

# 3. 전체 샘플 반복
for x_i, y_i in zip(g.x, g.y):
    y_hat = x_i * g.w + g.b
    err = y_i - y_hat
    w_rate = x_i
    g.w = g.w + w_rate * err
    g.b = g.b + 1 * err
# print(g.w, g.b)

# visualization
plt.scatter(g.x, g.y)
pt1 = (-0.1, -0.1* g.w + g.b)
pt2 = (0.15, 0.15 * g.w + g.b)
plt.plot([pt1[0], pt2[0]],[pt1[1], pt2[1]])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# repeat EPOKE
for i in range(1, 100):
    for x_i, y_i in zip(g.x, g.y):
        y_hat = x_i * g.w + g.b
        err = y_i - y_hat
        w_rate = x_i
        g.w = g.w + w_rate * err
        g.b = g.b + 1 * err

print(g.w, g.b) # 방정식의 기울기와 절편

# one more visualization
plt.scatter(g.x, g.y)
pt1 = (-0.1, -0.1* g.w + g.b)
pt2 = (0.15, 0.15 * g.w + g.b)
plt.plot([pt1[0], pt2[0]],[pt1[1], pt2[1]])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# predict by model
x_new = 0.18
y_pred = x_new * g.w + g.b
print(y_pred)

# visualization
plt.scatter(g.x, g.y)
plt.scatter(x_new, y_pred)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

