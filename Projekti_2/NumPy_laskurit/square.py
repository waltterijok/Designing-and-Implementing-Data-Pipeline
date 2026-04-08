import numpy as np
import matplotlib.pyplot as plt

square = np.array([
    [-1, -1, 0],
    [1, -1, 0],
    [1, 1, 0],
    [-1, 1, 0]
])

def x_rotation(theta):
    return np.array([
        [1, 1, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def y_rotation(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def z_rotation(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

theta = np.radians(45)

R = z_rotation(theta)

rotated_square = square @ R.T

'''def plot_square(points, title):
    pts = np.vstack([points, points[0]])
    plt.plot(pts[:, 0], pts[:, 1], '0-')

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plot_square(square, "Original")

plt.subplot(1,2,2)
plot_square(rotated_square, "Rotated")

plt.show()'''