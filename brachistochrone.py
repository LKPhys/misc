import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
rcParams['animation.convert_path'] = r'/lewis/bin/convert'

# Animation showing the path of minimum time for an object accelerating due to gravity (Brachistochrone problem) using the solutions which were solved as part of the graded tutorial in the Mathematical Physics class.

# constants and parametric equations
g = 9.81
A = 1/(2*g)
t1 = np.linspace(0, 2, 1000)
linex = A * (t1 - 0.5*np.sin(2*t1))
liney = -A * (0.5 - 0.5*np.cos(2*t1))

# for loop to stop the animation once y reaches it's minimum point
counter = 0
for i in range(1, len(linex)):
    if abs(liney[i]) - abs(liney[i-1]) > 0:
        counter += 1
    else:
        break

ymin = liney[0:counter+40].min()
xmax = linex[0:counter+40].max()
m = ymin/xmax
x0 = A*t1
y0 = m*x0


def position(t):
    '''
    Parametric equation for the curve of minimum time found using Euler-Lagrange
    '''
    x1 = A * (t - 0.5*np.sin(2*t))
    y1 = -A * (0.5 - 0.5*np.cos(2*t))

    return x1, y1


def linear(t):
    '''
    Linear path
    '''
    x2 = A*t
    y2 = m*x2
    return x2, y2


fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Curve of minimum time (Brachistochrone)')
ax.plot(linex[0:counter+40], liney[0:counter+40], 'b')
ax.plot(x0, y0, 'b')
ax.axis([0, xmax, ymin, 0])


points = []
for i in range(2):
    point = ax.plot([], [], marker='o', markersize=10)[0]
    points.append(point)


def init():
    for i in points:
        i.set_data([],[])
    return points


def update(t):
    x1, y1 = position(t)
    x2, y2 = linear(t)
    legend = plt.legend()

    x = [x1, x2]
    y = [y1, y2]

    for i, point in enumerate(points):
        if x[i] <= xmax and y[i] >= ymin:
            point.set_data(x[i], y[i])
            if i == 1:
                point.set_label('Linear = {:.3f}s'.format(t))
            else:
                point.set_label('Brachistochrone = {:.3f}s'.format(t))

    legend.remove()
    legend=plt.legend()

    return points + [legend]


animate = FuncAnimation(fig, update, interval=20, blit=True, repeat=True, frames=np.linspace(0, 2*np.pi, 360, endpoint=False))
animate.save('curveanimation.gif', writer='imagemagick', fps=30)
plt.show()
