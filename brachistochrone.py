import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation showing the path of minimum time for an object accelerating due to gravity (Brachistochrone problem) using the solutions which were solved as part of the graded tutorial in the Mathematical Physics class.

# constants and parametric equations
g = 9.81
A = 1/(2*g)
t = np.linspace(0, 5, 1000)
linex = A * (t - 0.5*np.sin(2*t))
liney = -A * (0.5 - 0.5*np.cos(2*t))

# for loop to stop the animation once y reaches it's minimum point
counter = 0
for i in range(1, len(linex)):
    if abs(liney[i]) - abs(liney[i-1]) > 0:
        counter += 1
    else:
        break

ymin = liney[0:counter].min()
xmax = linex[0:counter].max()


def position(t):
    x = A * (t - 0.5*np.sin(2*t))
    y = -A * (0.5 - 0.5*np.cos(2*t))
    return x, y


fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Curve of minimum time (Brachistochrone)')
ax.plot(linex, liney)
ax.axis([0, xmax, ymin, 0])
point, = ax.plot(0, 1, marker='o')


def update(t):
    x, y = position(t)

    if x <= xmax and y >= ymin:
        point.set_data([x], [y])
    else:
        pass

    return point,


animate = FuncAnimation(fig, update, interval=10, blit=True, repeat=True, frames=np.linspace(0, 2*np.pi, 360, endpoint=False))
plt.show()
