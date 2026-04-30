import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots()

# Square
square = patches.Rectangle((1, 1), 2, 2, edgecolor='blue', facecolor='lightblue')

# Circle
circle = patches.Circle((6, 2), 1, edgecolor='green', facecolor='lightgreen')

# Rectangle
rectangle = patches.Rectangle((1, 5), 3, 1.5, edgecolor='red', facecolor='salmon')

# Triangle
triangle = patches.Polygon([[6, 5], [5, 7], [7, 7]], edgecolor='purple', facecolor='violet')

# Add shapes to plot
ax.add_patch(square)
ax.add_patch(circle)
ax.add_patch(rectangle)
ax.add_patch(triangle)

# Set limits and title
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("2D Shapes in Python (Simple Visualization)")

# Hide axes for clean look
ax.set_xticks([])
ax.set_yticks([])

plt.show()
