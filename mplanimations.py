import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb, to_rgba
import numpy as np

interval = 20
n = 1000/interval

def time(counter):
    return (interval*counter)/1000

def normalize(array):
    return (array - array.min())/(array.max()-array.min())

def sine(initial, final, counter):
    return (initial*(n-n*(.5*np.sin((np.pi/n)*counter-(np.pi/2))+.5))+final*(n*(.5*np.sin((np.pi/n)*counter-(np.pi/2))+.5)))/n
    
def linear(initial, final, counter):
    return (initial*(n-counter)+final*(counter))/n



class Transitions:
    
    def __init__(self):
        """
        Initiates the counters for each transition instance.
        """
        
        self.counter = 0
        
        
        
    def alpha_transition(self, i, starttime, alpha1, alpha2, transitionline, transition_time=1, transition_type=sine):
        """
        Creates a transition between two different alpha values.
        """

        t = time(i)

        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            transitionline.set_alpha(transition_type(alpha1, alpha2, self.counter))
        elif t == starttime + transition_time:
            self.counter = 0
        
            
            
    def axis_transition(self, i, starttime, xlim1, xlim2, ylim1, ylim2, axis, transition_time=1, transition_type=sine):
        """
        Creates a transition between axis limits.
        """

        t = time(i)
        
        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            axis.set_xlim(transition_type(xlim1[0], xlim2[0], self.counter), transition_type(xlim1[1], xlim2[1], self.counter))
            axis.set_ylim(transition_type(ylim1[0], ylim2[0], self.counter), transition_type(ylim1[1], ylim2[1], self.counter))
        elif t == starttime + transition_time:
                self.counter = 0
                    
                    
                    
    def color_transition(self, i, starttime, cmap, c1, c2, transitionline, transition_time=1, transition_type=sine):
        """
        Creates a color transition for using the specified color map and the initial and final colors.
        """

        t = time(i)

        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            transitionline.set_color(cmap(transition_type(c1, c2, self.counter)))
        elif t == starttime + transition_time:
            self.counter = 0
                    
                    
                    
    def dot_transition(self, i, starttime, size1, size2, dot, transition_time=1, duration='inf', transition_type=sine):
        """
        Creates a transition between dot sizes for all dots in a scatter plot.
        """

        t = time(i)
                    
        if duration == 'inf':
            if t >= starttime and t < starttime + transition_time:
                self.counter += 1/transition_time
                dot.set_sizes([transition_type(size1, size2, self.counter)])
            elif t == starttime + transition_time:
                self.counter = 0
        else:
            if t >= starttime and t < starttime + transition_time:
                self.counter += 1/transition_time
                dot.set_sizes([transition_type(size1, size2, self.counter)])
            elif t == starttime + transition_time:
                self.counter=0
            elif t >= starttime + duration and t < starttime + duration + transition_time:
                self.counter += 1/transition_time
                dot.set_sizes([transition_type(size2, size1, self.counter)])
            
                
            
    def line_transition(self, i, starttime, yvals1, yvals2, transitionline, transition_time=1, transition_type=sine):
        """
        Creates a transition between two functions of x
        """

        t= time(i)
        
        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            transitionline.set_ydata(transition_type(yvals1, yvals2, self.counter))
        elif t == starttime + transition_time:
            self.counter = 0

                
                
            
    def par_transition(self, i, starttime, xvals1, xvals2, yvals1, yvals2, transitionline, transition_time=1, transition_type=sine):
        """
        Creates a transition between two sets of parametric equations.
        This function is capable of doing the same thing as line_transition(), but requires two extra arguments.
        """

        t = time(i)
        
        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            transitionline.set_data(transition_type(xvals1, xvals2, self.counter), transition_type(yvals1, yvals2, self.counter))
        elif t == starttime + transition_time:
            self.counter = 0
            
            
            
    def scatter_transition(self, i, starttime, xvals1, xvals2, yvals1, yvals2, scatterplot, carray1, carray2, transition_time=1, transition_type=sine):
        """
        Creates a transition between two scatter plots with different points
        """

        t = time(i)

        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            scatterplot.set_offsets(np.column_stack((transition_type(xvals1, xvals2, self.counter), transition_type(yvals1, yvals2, self.counter))))
            scatterplot.set_array(transition_type(carray1, carray2, self.counter))
            # The mathematical precision of the line above needs to be investigated.
        elif t == starttime + transition_time:
            self.counter = 0



    def var_transition(self, i, starttime, initial, final, transitionline, func, transition_time=1, transition_type=sine):
        """
        Creates a variable that transitions between two values.
        """

        t = time(i)
        self.var = initial

        if t >= starttime and t < starttime + transition_time:
            self.counter += 1/transition_time
            self.var = transition_type(initial, final, self.counter)
            transitionline.set_ydata(func(self.var))
        elif t == starttime + transition_time:
            self.counter = 0

    # A simpler and more versatile version that will eventually replace the var_transition function above.
    def var_transition2(self, i, starttime, initial, final, transition_time=1, transition_type=sine):
            """
            Creates a variable that transitions between two values.
            """

            t = time(i)
            self.var = initial

            if t >= starttime and t < starttime + transition_time:
                self.counter += 1/transition_time
                self.var = transition_type(initial, final, self.counter)
            elif t == starttime + transition_time:
                self.counter = 0                
                
                
                
class Effects:

    def __init__(self):
        
        self.xlist = []
        self.ylist = []

    # n must be divisible by number of elements in x and y lists
    def tail(self, xcoord, ycoord, ax, color, n):

        if len(self.xlist) < n:
            for item in xcoord:
                self.xlist.insert(0, item)
            for item in ycoord:
                self.ylist.insert(0, item)

        if len(self.xlist) == n:
            for item in xcoord:
                del self.xlist[-1]
                self.xlist.insert(0, item)
            for item in ycoord:
                del self.ylist[-1]
                self.ylist.insert(0, item)

        offsets = np.column_stack((self.xlist, self.ylist))
        ax.set_offsets(offsets)
        
        color=color
        alpha_array = [(1/(n**2))*((i-n)**2) for i in range(n)]
        r, g, b = to_rgb(color)
        color = [(r, g, b, alpha) for alpha in alpha_array]
        ax.set_color(color)



class Creations:

    def __init__(self):

        self.counter = 0

    
    # A function for creating lines entirely within the animation function
    def create_line(self, i, starttime, name, x, y, ax, color, alpha):

        t = time(i)
        if t == 0:
            self.graph = ax.plot(x,y, c=color, alpha=alpha)

