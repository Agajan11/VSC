import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Задаем координаты точек
points = np.array([[9, -9], [8, -4], [9, 5], [9, 10], [6, 5], [-4, 0], [1, 0]])

# Строим выпуклую оболочку
hull = ConvexHull(points)

# Строим график точек
plt.plot(points[:,0], points[:,1], 'o')

# Строим границы выпуклой оболочки
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.title('Выпуклая оболочка множества точек')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
