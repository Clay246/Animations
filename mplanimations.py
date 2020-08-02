import matplotlib.pyplot as plt
import numpy as np

interval = 20
n = 1000/interval

def time(counter):
    return (interval*counter)/1000

def sine(initial, final, counter):
    return (initial*(n-n*(.5*np.sin((np.pi/n)*counter-(np.pi/2))+.5))+final*(n*(.5*np.sin((np.pi/n)*counter-(np.pi/2))+.5)))/n
    
def linear(initial, final, counter):
    return (initial*(n-counter)+final*(counter))/n



class Transitions:
    
    def __init__(self):
        """
        Initiates the counters for each transition instance.
        """
        
        self.alpha_transition_c = 0
        self.axis_transition_c = 0
        self.color_transition_c = 0
        self.dot_transition_c = 0
        self.line_transition_c = 0
        self.par_transition_c = 0
        self.var_transition_c = 0
        
        
        
    def alpha_transition(self, i, starttime, alpha1, alpha2, transitionline, transition_time=1, transition_type='sine'):
        """
        Creates a transition between two different alpha values.
        """

        t = time(i)
        
        if transition_type == 'sine':
            if t >= starttime and t < starttime + transition_time:
                self.alpha_transition_c += 1/transition_time
                transitionline.set_alpha(sine(alpha1, alpha2, self.alpha_transition_c))
            elif t == starttime + transition_time:
                self.alpha_transition_c = 0
        
            
            
    def axis_transition(self, i, starttime, xlim1, xlim2, ylim1, ylim2, axis, transition_time=1, transition_type='sine'):
        """
        Creates a transition between axis limits.
        """

        t = time(i)
        
        if transition_type == 'sine':
            if t >= starttime and t < starttime + transition_time:
                self.axis_transition_c += 1/transition_time
                axis.set_xlim(sine(xlim1[0], xlim2[0], self.axis_transition_c), sine(xlim1[1], xlim2[1], self.axis_transition_c))
                axis.set_ylim(sine(ylim1[0], ylim2[0], self.axis_transition_c), sine(ylim1[1], ylim2[1], self.axis_transition_c))
            elif t == starttime + transition_time:
                    self.axis_transition_c = 0
                    
        if transition_type == 'linear':
            if t >= starttime and t < starttime + transition_time:
                self.axis_transition_c += 1/transition_time
                axis.set_xlim(linear(xlim1[0], xlim2[0], self.axis_transition_c), sine(xlim1[1], xlim2[1], self.axis_transition_c))
                axis.set_ylim(linear(ylim1[0], ylim2[0], self.axis_transition_c), sine(xlim1[1], xlim2[1], self.axis_transition_c))
            elif t == starttime + transition_time:
                    self.axis_transition_c = 0
                    
                    
                    
    def color_transition(self, i, starttime, cmap, c1, c2, transitionline, transition_time=1, transition_type='sine'):
        """
        Creates a color transition for using the specified color map and the initial and final colors.
        """

        t = time(i)
    
        if transition_type == 'sine':
            if t >= starttime and t < starttime + transition_time:
                self.color_transition_c += 1/transition_time
                transitionline.set_color(cmap(sine(c1, c2, self.color_transition_c)))
            elif t == starttime + transition_time:
                self.color_transition_c = 0
                
        if transition_type == 'linear':
            if t >= starttime and t < starttime + transition_time:
                self.color_transition_c += 1/transition_time
                transitionline.set_color(cmap(linear(c1, c2, self.color_transition_c)))
            elif t == starttime + transition_time:
                self.color_transition_c = 0
                    
                    
                    
    def dot_transition(self, i, starttime, size1, size2, dot, transition_time=1, duration='inf', transition_type='sine'):
        """
        Creates a transition between dot sizes for all dots in a scatter plot.
        """

        t = time(i)
        
        if transition_type == 'sine':
            if duration == 'inf':
                if t >= starttime and t < starttime + transition_time:
                    self.dot_transition_c += 1/transition_time
                    dot.set_sizes([sine(size1, size2, self.dot_transition_c)])
                elif t == starttime + transition_time:
                    self.add_dot_c = 0
            else:
                if t >= starttime and t < starttime + transition_time:
                    self.dot_transition_c += 1/transition_time
                    dot.set_sizes([sine(size1, size2, self.dot_transition_c)])
                elif t >= starttime + duration and t < starttime + duration + transition_time:
                    self.dot_transition_c += 1/transition_time
                    dot.set_sizes([sine(size1, size2, self.dot_transition_c)])
                    
        if transition_type == 'linear':
            if duration == 'inf':
                if t >= starttime and t < starttime + transition_time:
                    self.dot_transition_c += 1/transition_time
                    dot.set_sizes([linear(size1, size2, self.dot_transition_c)])
                elif t == starttime + transition_time:
                    self.add_dot_c = 0
            else:
                if t >= starttime and t < starttime + transition_time:
                    self.dot_transition_c += 1/transition_time
                    dot.set_sizes([linear(size1, size2, self.dot_transition_c)])
                elif t == starttime + transition_time:
                    # This is required for the linear function because it is not periodic and the dot transition will occur again at the end.
                    self.dot_transition_c=0
                elif t >= starttime + duration and t < starttime + duration + transition_time:
                    self.dot_transition_c += 1/transition_time
                    dot.set_sizes([linear(size2, size1, self.dot_transition_c)])
            
                
            
    def line_transition(self, i, starttime, yvals1, yvals2, transitionline, transition_time=1, transition_type='sine'):
        """
        Creates a transition between two functions of x
        """

        t= time(i)
        
        if transition_type == 'sine':
            if t >= starttime and t < starttime + transition_time:
                self.line_transition_c += 1/transition_time
                transitionline.set_ydata(sine(yvals1, yvals2, self.line_transition_c))
            elif t == starttime + transition_time:
                line_transition_c = 0
                
        if transition_type == 'linear':
            if t >= starttime and t < starttime + transition_time:
                self.par_transition_c += 1/transition_time
                transitionline.set_ydata(linear(yvals1, yvals2, self.line_transition_c))
            elif t == starttime + transition_time:
                self.par_transition_c = 0
                
                
            
    def par_transition(self, i, starttime, xvals1, xvals2, yvals1, yvals2, transitionline, transition_time=1, transition_type='sine'):
        """
        Creates a transition between two sets of parametric equations.
        This function is capable of doing the same thing as line_transition(), but requires two extra arguments.
        """

        t = time(i)
        
        if transition_type == 'sine':
            if t >= starttime and t < starttime + transition_time:
                self.par_transition_c += 1/transition_time
                transitionline.set_data(sine(xvals1, xvals2, self.par_transition_c), sine(yvals1, yvals2, self.par_transition_c))
            elif t == starttime + transition_time:
                self.par_transition_c = 0
                
        if transition_type == 'linear':
            if t >= starttime and t < starttime + transition_time:
                self.par_transition_c += 1/transition_time
                transitionline.set_data(linear(xvals1, xvals2, self.par_transition_c), linear(yvals1, yvals2, self.par_transition_c))
            elif t == starttime + transition_time:
                self.par_transition_c = 0



    def var_transition(self, i, starttime, initial, final, transitionline, func, transition_time=1, transition_type='sine'):
        """
        Creates a variable that transitions between two values.
        """

        t = time(i)
        self.var = initial
        
        if transition_type == 'sine':
            if t >= starttime and t < starttime + transition_time:
                self.var_transition_c += 1/transition_time
                self.var = sine(initial, final, self.var_transition_c)
                transitionline.set_ydata(func(self.var))
            elif t == starttime + transition_time:
                self.par_transition_c = 0

        if transition_type == 'linear':
            if t >= starttime and t < starttime + transition_time:
                self.var_transition_c += 1/transition_time
                self.var = linear(initial, final, self.var_transition_c)
                transitionline.set_ydata(func(self.var))
            elif t == starttime + transition_time:
                self.par_transition_c = 0
