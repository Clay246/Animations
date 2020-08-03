import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimations as ans

t = np.linspace(0, 2*np.pi, 100)

half_circles = [np.linspace(3*(np.pi/2) + i*(np.pi/4), 5*(np.pi/2) + i*(np.pi/4), 100) for i in range(8)]

plt.style.use('dark_background')

fig, ax1 = plt.subplots()

ax1.set_aspect('equal')
ax1.set_xlim(-6, 6)
ax1.set_ylim(-6, 6)
ax1.axis('off')

tline1, = ax1.plot(t*0, t*0, linewidth=2, c='white', zorder=1, alpha=.5)
tdot1 = ax1.scatter(0, 0, color='white', s=0)

lines = [ax1.plot(t*0, t*0, linewidth=2, c='white', zorder=1, alpha=.5)[0] for i in range(9)]

ts = [ans.Transitions() for i in range(21)]

r = 6
ttime = 6
ds = 20

def animate(i):

    ts[1].par_transition(i, 0, t*0, np.cos(t), t*0, np.sin(t), tline1, transition_type=ans.linear)
    ts[2].par_transition(i, 1, np.cos(t), (r+1)*np.cos(t), np.sin(t), (r+1)*np.sin(t), tline1, transition_time=ttime, transition_type=ans.linear)
    ts[3].color_transition(i, 0, plt.cm.binary, 0, .25, tline1, transition_time=1, transition_type=ans.linear)
    ts[4].color_transition(i, 0, plt.cm.binary, .25, 1, tline1, transition_time=ttime, transition_type=ans.linear)

    for n in range(8):
        ts[5+n].par_transition(i, 1, np.cos(n*np.pi/4), r*np.cos(half_circles[n])+np.cos(n*np.pi/4), half_circles[n]*0+np.sin(n*np.pi/4), r*np.sin(half_circles[n])+np.sin(n*np.pi/4), lines[n], transition_time=ttime, transition_type=ans.linear)
        
    for n in range(8):
        ts[13+n].color_transition(i, 1, plt.cm.binary, .25, 1, lines[n], transition_time=ttime, transition_type=ans.linear)
    
    
ani = animation.FuncAnimation(fig, animate, interval=20, frames=350, repeat=False)

plt.show()
