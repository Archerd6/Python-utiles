import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

k = 8.987552e9 # N * m^2 / C^2
q1, q2, q0 = -2e-9, -3e-9, 2e-9
x1, y1, x2, y2, x0, y0 = 0, 0, 2, 0, 2, 2
v1, v2, v0 = np.array([0, 0]), np.array([0, 0]), np.array([0, 0])
m1, m2, m0 = 1, 1, 1
dt = 0.01

def update(frame):
    global x0, y0, v0
    
    ax0 = k * q0 * (x2 - x0) / (((x2 - x0)**2 + (y2 - y0)**2)**(3/2)) + k * q0 * (x1 - x0) / (((x1 - x0)**2 + (y1 - y0)**2)**(3/2))
    ay0 = k * q0 * (y2 - y0) / (((x2 - x0)**2 + (y2 - y0)**2)**(3/2)) + k * q0 * (y1 - y0) / (((x1 - x0)**2 + (y1 - y0)**2)**(3/2))

    
    a0 = np.array([ax0, ay0])
    v0 = v0 + a0 * dt
    x0, y0 = x0 + v0[0] * dt, y0 + v0[1] * dt
    
    colors = ['red' if q > 0 else 'blue' for q in [q1, q2, q0]]

    scat.set_offsets(np.c_[x1, y1, x2, y2, x0, y0].reshape(-1, 2))
    scat.set_facecolors(colors)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)


x = np.array([x1, x2, x0])
y = np.array([y1, y2, y0])
scat = ax.scatter(x, y)

ani = animation.FuncAnimation(fig, update, frames=1000, interval=10)

plt.show()
