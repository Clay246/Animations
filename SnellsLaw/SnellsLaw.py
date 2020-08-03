import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimations as ans

ni = 1
nt = 2
s = -6

def line1(m):
    return [-m*3, 0]

def line2(m):
    return [0, 4*np.tan(np.arcsin((ni/nt)*np.sin(np.arctan(m))))]

def line3(m):
    return [4*np.tan(np.arcsin((ni/nt)*np.sin(np.arctan(m)))), 4*np.tan(np.arcsin((ni/nt)*np.sin(np.arctan(m))))-line1(m)[0]]

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

ax.fill_between([3,7], -4, 4, alpha=.75)
ax.plot([3,3], [-4,4], c='black')
ax.plot([7,7], [-4,4], c='black')
ax.plot([3,7], [4,4], c='black')
ax.plot([3,7], [-4,-4], c='black')

l1, = ax.plot([0,3], line1(s), c='red', linewidth=3)
l2, = ax.plot([3,7], line2(s), c='red', linewidth=3)
l3, = ax.plot([7,10], line3(s), c='red', linewidth=3)

ts = [ans.Transitions() for i in range(6)]

def animate(i):
    ts[0].var_transition(i, 1, s, -s, l1, line1, transition_time=4)
    ts[1].var_transition(i, 1, s, -s, l2, line2, transition_time=4)
    ts[2].var_transition(i, 1, s, -s, l3, line3, transition_time=4)
    ts[3].var_transition(i, 6, -s, s, l1, line1, transition_time=4)
    ts[4].var_transition(i, 6, -s, s, l2, line2, transition_time=4)
    ts[5].var_transition(i, 6, -s, s, l3, line3, transition_time=4)

ani = animation.FuncAnimation(fig, animate, interval=20, frames=550, repeat=False)

plt.show()
