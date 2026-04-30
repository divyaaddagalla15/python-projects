import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cube vertices
vertices = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

# Cube faces
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[4], vertices[7], vertices[3], vertices[0]]
]

# Add 3D shading
ax.add_collection3d(Poly3DCollection(
    faces,
    facecolors='skyblue',
    linewidths=1,
    edgecolors='black',
    alpha=0.8
))

# Auto scale
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title("3D Shaded Cube in Python")

plt.show()
