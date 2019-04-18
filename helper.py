import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter, FormatStrFormatter
#ax.view_init(30, 190)
def initOneSoliton(off, v, L, N, S):
	psi = np.zeros(N, dtype=np.complex_)
	t = 0
	h = L/N
	a = np.sqrt(2)
	B = 3/2 - 2 * S
	for i in range(N):
		x = i * h - off
		f = (2 * a * exp(a * x)) / (1 + B * \
			exp(2 * a * x))
		psi[i] = f * exp(I * t + I * v * x)
	return psi 
	plt.show()
def initTwoSoliton(x1off, v1, x2off, v2, L,
	N, S):
	psi = np.zeros(N, dtype=np.complex_)
	t = 0
	h = L/N
	a = np.sqrt(2)
	B = 3/2 - 2 * S
	for i in range(N):
		x1 = i * h - x1off
		f1 = (2 * a * exp(a * x1)) / (1 + B * \
			exp(2 * a * x1))
		x2 = i * h - x2off
		f2 = (2 * a * exp(a * x2)) / (1 + B * \
			exp(2 * a * x2))
		psi[i] = f1 * exp(I * t + I * v1 * x1) \
			+ f2 * exp(I * t + I * v2 * x2)
	return psi
def computeN(psi1, psi2, L, N):
	N1 = np.trapz(abs(psi1), dx=L/N)
	N2 = np.trapz(abs(psi2), dx=L/N)
	return np.abs(N1 - N2)
def plot2D(y, L, N):
	plt.plot(np.linspace(0, L, num=N), abs(y))
	plt.show()
def plot3D(psiEv, L, N, T, tau):
	fig = plt.figure(figsize=(20,10))
	ax = fig.gca(projection='3d')
	# Make data.
	X = np.arange(0, L, L/N)
	Y = np.arange(0, T, tau)
	X, Y = np.meshgrid(X, Y)
	# Plot the surface.
	surf = ax.plot_surface(X, Y, psiEv,
	cmap=cm.jet, linewidth=10,
	antialiased=True, rstride=1,
	cstride=1)
	# Customize the z axis.
	ax.set_zlim(0, 2)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
	#ax.view_init(30, 190)
	# Add a color bar which maps values to
	fig.colorbar(surf, shrink=0.5, aspect=10)
	plt.show()