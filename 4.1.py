import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Заданные значения
mx, my, mz = 2, 2, 1

# Вершины тетраэдра
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

# Функция для построения аксонометрической проекции осей
def plot_axes(ax):
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)
    ax.text(1.1, 0, 0, 'X', color='r')
    ax.text(0, 1.1, 0, 'Y', color='g')
    ax.text(0, 0, 1.1, 'Z', color='b')

# Функция для построения тетраэдра
def plot_tetrahedron(ax):
    edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    for edge in edges:
        ax.plot3D(*zip(vertices[edge[0]], vertices[edge[1]]), color='black')

# Создание графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение осей и тетраэдра
plot_axes(ax)
plot_tetrahedron(ax)

# Настройка графика
ax.set_xlim(0, 1.5)
ax.set_ylim(0, 1.5)
ax.set_zlim(0, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=20., azim=-45)  # Угол обзора

# Отображение графика
plt.show()
