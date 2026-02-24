import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

def update(frame):
    circle.center = (frame, 5)
    return circle,

ani = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 100),
    interval=50
)

plt.title("Animated Moving Circle")
plt.show()
