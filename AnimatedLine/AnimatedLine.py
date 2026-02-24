import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import random

plt.ion()
fig, ax = plt.subplots()
ax.set_ylim(-10, 10)

x, y = [], []
line, = ax.plot([], [])

i = 0
while True:
    x.append(i)
    y.append(random.randint(-9, 9))
    x, y = x[-50:], y[-50:]

    line.set_data(x, y)
    ax.set_xlim(max(0, i - 50), i + 1)

    plt.pause(0.1)
    i += 1
