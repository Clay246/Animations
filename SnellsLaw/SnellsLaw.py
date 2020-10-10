import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mplanimations

ni = 1 # Index of refraction of beam outside material
nt = 2 # Index of refraction of the material
s = -6

# Incident Beam
def line0(m):
    return [-m*3, 0]

# Reflected Beam
def line1(m):
    return [m*3, 0]

# Transmitted beam in material
def line2(m):
    return [0, 4*np.tan(np.arcsin((ni/nt)*np.sin(np.arctan(m))))]

#Transmitted beam outside of material
def line3(m):
    return [4*np.tan(np.arcsin((ni/nt)*np.sin(np.arctan(m)))), 4*np.tan(np.arcsin((ni/nt)*np.sin(np.arctan(m))))-line0(m)[0]]

# Reflectivity for polarization parallel to the plane of incidence
# Note that for clarity, the true value of reflectivity is multiplied by 2 here
def ref(m):
    alphar = 2*((ni*np.sqrt(1-((ni/nt)*np.sin(np.arctan(m)))**2)-nt*np.cos(np.arctan(m)))/(ni*np.sqrt(1-((ni/nt)*np.sin(np.arctan(m)))**2)+nt*np.cos(np.arctan(m))))**2
    l1.set_alpha(alphar)

# Transmitissity for polarization parallel to the plane of incidence
def trans(m):
    alphat = (4*ni*nt*np.cos(np.arctan(m))*np.sqrt(1-((ni/nt)*np.sin(np.arctan(m)))**2))/((ni*np.sqrt(1-((ni/nt)*np.sin(np.arctan(m)))**2)+nt*np.cos(np.arctan(m)))**2)
    l2.set_alpha(alphat)
    l3.set_alpha(alphat)

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# The blue box
ax.fill_between([3,7], -4, 4, alpha=.75)
ax.plot([3,3], [-4,4], c='black')
ax.plot([7,7], [-4,4], c='black')
ax.plot([3,7], [4,4], c='black')
ax.plot([3,7], [-4,-4], c='black')

# The lines for the beam
l1, = ax.plot([0,3], line1(s), c='red', linewidth=3)
l0, = ax.plot([0,3], line0(s), c='red', linewidth=3)
l2, = ax.plot([3,7], line2(s), c='red', linewidth=3)
l3, = ax.plot([7,10], line3(s), c='red', linewidth=3)

ts = []
for i in range(8):
    ts.append(mplanimations.Transitions())

def animate(i):
    ts[0].var_transition(i, 1, s, -s, l0, line0, transition_time=6)
    ts[1].var_transition(i, 1, s, -s, l1, line1, transition_time=6)
    ts[2].var_transition(i, 1, s, -s, l2, line2, transition_time=6)
    ts[3].var_transition(i, 1, s, -s, l3, line3, transition_time=6)
    ts[4].var_transition(i, 8, -s, s, l0, line0, transition_time=6)
    ts[5].var_transition(i, 8, -s, s, l1, line1, transition_time=6)
    ts[6].var_transition(i, 8, -s, s, l2, line2, transition_time=6)
    ts[7].var_transition(i, 8, -s, s, l3, line3, transition_time=6)
    
    if mplanimations.time(i) <= 7:
        ref(ts[0].var)
        trans(ts[0].var)
    if mplanimations.time(i) > 7:
        ref(ts[4].var)
        trans(ts[4].var)

ani = animation.FuncAnimation(fig, animate, interval=20, frames=700, repeat=False)

plt.show()
