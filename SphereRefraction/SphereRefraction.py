import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import mplanimations

# Refractive indices
ni=1
nt=1.5

# Many functions are defined to avoid having big long equations.

def theta(var):
    return np.arccos(-var)

def thetai(var):
    return np.arctan(np.cos(theta(var))/np.sin(theta(var)))

def thetat(var):
    return np.arcsin((ni/nt)*np.sin(thetai(var)))

def L(var):
    return np.sin(np.pi-2*thetat(var))/(np.sin(thetat(var)))


def l1xcoord2(var): # Coordinate for l1x[1] and l2x[0]
    return -np.sin(theta(var))
def l1ycoord(var): # Coordinate for l2y[0] and l1y[1]
    return var


def l2xcoord2(var): # Coordinate for l2x[1] and l3x[0]
    return -np.sin(theta(var))+L(var)*np.cos(np.pi/2-theta(var)-thetat(var))
def l2ycoord2(var): # Coordinate for l2y[1] and l3y[0]
    return var+L(var)*np.sin(np.pi/2-theta(var)-thetat(var))


def thetaf(var):
    return (-np.arcsin((nt/ni)*np.sin(np.arctan(l2ycoord2(var)/l2xcoord2(var))+np.arctan((-(l2ycoord2(var)-l1ycoord(var)))/(l2xcoord2(var)-l1xcoord2(var)))))+np.arctan(l2ycoord2(var)/l2xcoord2(var)))


def l3xcoord2(var): # Coordinate for l3x[1]
    return 5*np.cos(thetaf(var))
def l3ycoord2(var): # Coordinate for l3y[1]
    return 5*np.sin(thetaf(var))+l2ycoord2(var)



fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

t = np.linspace(0, 2*np.pi)

ax.plot(np.cos(t), np.sin(t), c='black', linewidth=1)

ax.fill_between(np.cos(t), np.sin(t))

y = [.85-i/10 for i in range(18)]
x = [-2.2 for i in range(len(y))]
slopes_midline = [(l2ycoord2(item)-l1ycoord(item))/(l2xcoord2(item)-l1xcoord2(item)) for item in y]
slopes_endline = [(l3ycoord2(item)-l2ycoord2(item))/(l3xcoord2(item)-l2xcoord2(item)) for item in y]
l1xend = [l1xcoord2(item) for item in y]
l2xend = [l2xcoord2(item) for item in y]

rays = ax.scatter(x, y, s=5)

es = [mplanimations.Effects() for i in range(1)]

def animate(i):
    
    for j in range(len(x)):
        
        if x[j] < l1xend[j]:
            x[j] += .01

        if l1xend[j] <= x[j] <= l2xend[j]:
            x[j] += np.absolute(.01/(nt*np.sqrt(1+slopes_midline[j]**2)))
            y[j] += (slopes_midline[j]/np.absolute(slopes_midline[j]))*.01/(nt*np.sqrt(1+1/((slopes_midline[j])**2)))

        if x[j] > l2xend[j]:
                x[j] += np.absolute(.01/np.sqrt(1+slopes_endline[j]**2))
                y[j] += (slopes_midline[j]/np.absolute(slopes_midline[j]))*.01/np.sqrt(1+1/((slopes_endline[j])**2))


    es[0].tail(x, y, rays, 'red', 50*len(x))


ani = animation.FuncAnimation(fig, animate, interval=20, frames=650, repeat=False)

plt.show()
    














