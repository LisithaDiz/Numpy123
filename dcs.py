import numpy as np
import matplotlib.pyplot as plt


def y_fun(x):
    return x ** 2


def y_der(x):
    return 2 * x


current_pos = (80, y_fun(80))
learning_rate = 0.001
x = np.arange(-100, 100, 0.1)
y = y_fun(x)

for _ in range(1000):   # 1000 = epochs
    new_x = current_pos[0] - learning_rate * y_der(current_pos[0])

    new_y = y_fun(new_x)
    current_pos = (new_x, new_y)
    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color='red')
    plt.pause(1)
    plt.clf()

