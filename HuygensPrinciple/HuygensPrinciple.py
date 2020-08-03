import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimations as ans

t = np.linspace(0, 2*np.pi, 100)

half_circles = [np.linspace(3*(np.pi/2) + i*(np.pi/4), 5*(np.pi/2) + i*(np.pi/4), 100) for i in range(8)]

plt.style.use('dark_background')

fig, ax1 = plt.subplots()

ax1.set_aspect('equal')
ax1.set_xlim(-4, 4)
ax1.set_ylim(-4, 4)
ax1.axis('off')

tline1, = ax1.plot(t*0, t*0, linewidth=2, c='white', zorder=1, alpha=.5)
tdot1 = ax1.scatter(0, 0, color='white', s=0)

lines = [ax1.plot(t*0, t*0, linewidth=2, c='white', zorder=1, alpha=.5)[0] for i in range(9)]

dots = [ax1.scatter(np.cos(i*np.pi/4), np.sin(i*np.pi/4), color='white', s=0) for i in range(8)]

ts = [ans.Transitions() for i in range(29)]

r = 12
ttime = 11.5
ds = 20
dur = 12.7

def animate(i):

    ts[0].dot_transition(i, 1, 0, ds, tdot1, duration=17.5)
    ts[1].par_transition(i, 2, t*0, np.cos(t), t*0, np.sin(t), tline1, transition_type=ans.sine)
    
    for n in range(8):
        ts[2+n].dot_transition(i, 3+n/10, 0, ds, dots[n], duration=dur, transition_type=ans.sine)
    
    for n in range(8):
        ts[10+n].par_transition(i, 4.2, half_circles[n]*0+np.cos(n*np.pi/4), r*np.cos(half_circles[n])+np.cos(n*np.pi/4), half_circles[n]*0+np.sin(n*np.pi/4), r*np.sin(half_circles[n])+np.sin(n*np.pi/4), lines[n], transition_time=ttime, transition_type=ans.linear)
    
    ts[18].axis_transition(i, 5, [-4, 4], [-7.5, 7.5], [-4, 4], [-7.5, 7.5], ax1)
    ts[19].par_transition(i, 17.5, np.cos(t), t*0, np.sin(t), t*0, tline1, transition_type=ans.sine)
    
    for n in range(8):
        ts[20+n].color_transition(i, 4, plt.cm.binary, 0, 1, lines[n], transition_time=ttime, transition_type=ans.linear)
    
    
ani = animation.FuncAnimation(fig, animate, interval=20, frames=975, repeat=False)

plt.show()
