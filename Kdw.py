# import packages
import numpy as np
import matplotlib.pyplot as plt
# Korteweg-deVries Numerical Solution
# initial condition
k = 1*10**(-7) # temporal step
n = 1000 #  spatial number
h = 1/n # spatial step
delta = 0.022 # who the fuck knows
t = np.arange(0,.0001,k)
x = np.arange(0,2, h)

#
u = np.zeros([len(x),len(t)])  # generate empty position array
for i in range(0,len(x)):       
    u[i,0] = np.cos(np.pi*x[i])
for j in range(1,len(t)-1):
    for i in range(len(x)):
        i = i % 2000
        u[i,j+1] = u[i,j-1] - 1/3*(k/h)*(u[ (i+1 )% 2000,j]+u[i,j]+u[i-1,j])*(u[( i+1 )% 2000,j]-u[i-1,j]) \
       - (delta**2*(k/h)**3)*(u[ (i+2 ) % 2000,j]-2*u[ ( i+1 ) % 2000,j]+2*u[i-1,j]-u[i-2,j])


# plotting

from pylab import clf, plot, xlim, ylim, show, pause
for i in range(100):
	clf() # clear the plot
	plt.plot(u[:,i])
	plt.draw()
	plt.title('Velocity Time Evolution', fontsize = 12)
	plt.xlabel('Position (m)', fontsize = 10)
	plt.ylabel('Velocity (m/s)',  fontsize = 10)
	pause(0.1)