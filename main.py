import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 0
v0 = 20
theta = np.pi/4
m = 1
k = 0.1
g = 9.8

def vx(t):
    return v0 * np.cos(theta) * np.exp(-k/m*t)

def x(t):
    return x0 + (m/k) * v0 * np.cos(theta) * (1 - np.exp(-k/m*t))

def y(t):
    return y0 + (v0 * np.sin(theta) * t) - (0.5 * g * t**2)

t_max = (2 * v0 * np.sin(theta))/g

y_max = y0 + ((v0**2) * (np.sin(theta)**2))/(2*g)

# Вывод результатов
print("Время полета:", t_max, "секунд")
print("Максимальная высота:", y_max, "метров")

t = np.linspace(0, t_max, 1000)
x_vals = [x(i) for i in t]
y_vals = [y(i) for i in t]
plt.plot(x_vals, y_vals)
plt.xlabel("x, м")
plt.ylabel("y, м")
plt.title("Траектория движения тела")
plt.show()