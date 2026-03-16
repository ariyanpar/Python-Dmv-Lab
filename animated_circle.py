import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ---- User Input ----
y_pos = float(input("Enter Y position of circle (0–10): "))
speed = float(input("Enter animation speed in milliseconds (smaller = faster): "))

# ---- Plot Setup ----
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((0, y_pos), 0.5, color='blue')
ax.add_patch(circle)

# ---- Animation Function ----
def update(frame):
    circle.center = (frame, y_pos)
    return circle,

ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    interval=speed
)

plt.title("Animated Moving Circle")
plt.show()