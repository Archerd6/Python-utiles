import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constantes
k = 8.99 * 10**9 # N * m^2 / C^2
q1 = 2 * 10**-9 # C
q2 = 3 * 10**-9 # C
x1, y1 = 0, 0
x2, y2 = 2, 0
dt = 0.01 # s
t_max = 10 # s

def update(frame):
    global x1, y1, x2, y2
    r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    F = k * q1 * q2 / r**2
    Fx = F * (x1 - x2) / r
    Fy = F * (y1 - y2) / r
    ax1 = Fx / q1
    ay1 = Fy / q1
    ax2 = -Fx / q2
    ay2 = -Fy / q2
    x1 = x1 + ax1 * dt
    y1 = y1 + ay1 * dt
    x2 = x2 + ax2 * dt
    y2 = y2 + ay2 * dt
    colors = ['red' if q >= 0 else 'blue' for q in [q1, q2]]
    scat.set_offsets([[x1, y1], [x2, y2]])
    scat.set_facecolors(colors)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

scat = ax.scatter([x1, x2], [y1, y2], s=500, edgecolor='k')
ani = animation.FuncAnimation(fig, update, frames=int(t_max / dt), interval=10)

plt.show()
