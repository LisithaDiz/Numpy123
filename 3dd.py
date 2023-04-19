import numpy as np
import matplotlib.pyplot as plt


def z_func(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5


def cal_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), - np.sin(5 * x) * np.sin(5 * y)  # respect to x, respect to y


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_func(X, Y)

currnt_pos = (0.7, 0.4, z_func(0.7, 0.4))
currnt_pos1 = (0.5, 0.3, z_func(0.5, 0.3))
currnt_pos2 = (-0.7, -0.4, z_func(-0.7, -0.4))


L = 0.01

ax = plt.subplot(projection='3d')

for _ in range(1000):
    X_der, Y_der = cal_gradient(currnt_pos[0], currnt_pos[1])
    x_new, y_new = currnt_pos[0] - L * X_der, currnt_pos[1] - L*Y_der
    currnt_pos = (x_new, y_new, z_func(x_new, y_new))

    ax.plot_surface(X, Y, Z, cmap='viridis', zorder=0)
    ax.scatter(currnt_pos[0], currnt_pos[1], currnt_pos[2], color='magenta', zorder=1)
    plt.pause(0.001)
    ax.clear()
