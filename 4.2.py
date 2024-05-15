import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np


def is_convex(p1, p2, p3):
    # Функция для проверки выпуклости треугольника
    det = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    return det >= 0


def divide_polygon(points):
    triangles = []
    # Триангуляция полигона
    for i in range(1, len(points) - 1):
        if is_convex(points[0], points[i], points[i+1]):
            triangles.append([points[0], points[i], points[i+1]])
        else:
            triangles.append([points[0], points[i+1], points[i]])

    return triangles


def plot_polygon(points, triangles):
    fig, ax = plt.subplots()
    patches = []

    # Отображение полигона
    polygon = Polygon(points, closed=True, edgecolor='black', facecolor='none')
    ax.add_patch(polygon)

    # Отображение треугольников
    for triangle in triangles:
        patches.append(Polygon(triangle, closed=True, edgecolor='blue', facecolor='lightblue'))

    p = PatchCollection(patches, match_original=True)
    ax.add_collection(p)

    ax.autoscale_view()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Заданные точки полигона
points = np.array([[0, 0], [-3, 2], [-1, 4], [0, 2], [3, 3], [1, 2], [12, 1], [15, 85]])

# Триангуляция полигона
triangles = divide_polygon(points)

# Визуализация
plot_polygon(points, triangles)
