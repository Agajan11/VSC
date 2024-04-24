import numpy as np
import matplotlib.pyplot as plt

# Направляющий вектор проектирования
s = np.array([0, 1, 1])

# Построение профильной плоскости
profile_matrix = np.eye(3) - np.outer(s, s) / np.linalg.norm(s)
profile_axes = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
profile_projection = profile_axes @ profile_matrix

# Построение фронтальной плоскости
frontal_matrix = np.eye(3) - np.outer(s, s) / np.linalg.norm(s)
frontal_axes = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
frontal_projection = frontal_axes @ frontal_matrix

# Построение горизонтальной плоскости
horizontal_matrix = np.eye(3) - np.outer(s, s) / np.linalg.norm(s)
horizontal_axes = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
horizontal_projection = horizontal_axes @ horizontal_matrix

# Визуализация проекций
fig = plt.figure()

# Профильная плоскость
ax1 = fig.add_subplot(131, projection='3d')
ax1.quiver(0, 0, 0, *s, color='r', label='s')
ax1.quiver(0, 0, 0, *profile_projection[:, 0], color='g', label='x')
ax1.quiver(0, 0, 0, *profile_projection[:, 1], color='b', label='y')
ax1.set_xlabel('Oy\'')
ax1.set_ylabel('Oz\'')
ax1.set_zlabel('Ox\'')
ax1.legend()

# Фронтальная плоскость
ax2 = fig.add_subplot(132, projection='3d')
ax2.quiver(0, 0, 0, *s, color='r', label='s')
ax2.quiver(0, 0, 0, *frontal_projection[:, 0], color='g', label='x')
ax2.quiver(0, 0, 0, *frontal_projection[:, 1], color='b', label='y')
ax2.set_xlabel('Ox\'')
ax2.set_ylabel('Oy\'')
ax2.set_zlabel('Oz\'')
ax2.legend()

# Горизонтальная плоскость
ax3 = fig.add_subplot(133, projection='3d')
ax3.quiver(0, 0, 0, *s, color='r', label='s')
ax3.quiver(0, 0, 0, *horizontal_projection[:, 0], color='g', label='x')
ax3.quiver(0, 0, 0, *horizontal_projection[:, 1], color='b', label='y')
ax3.set_xlabel('Oz\'')
ax3.set_ylabel('Ox\'')
ax3.set_zlabel('Oy\'')
ax3.legend()

plt.show()
