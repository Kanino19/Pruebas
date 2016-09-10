import math as mt
import numpy as np
import matplotlib.pyplot as plt



def Rotar(x,y,a): 
	return x*mt.cos(mt.radians(a))+y*np.sin(mt.radians(a)), -x*np.sin(mt.radians(a))+y*np.cos(mt.radians(a))

def RotarI(x,y):
	return -y,x

def RotarD(x,y):
	return y,x

def Tras(x,y,d1,d2):
	return x+d1, y+d2

def Escal(x,y,r):
	return r*x, r*y

def four(x,y,d):
	x,y = Escal(x,y,0.5)
	d = 0.25*d
	# Parte 1
	x1, y1 = RotarI(x,y)
	x1, y1 = Tras(x1,y1,-d,-d)
	x1, y1 = x1[::-1],y1[::-1]

	# Parte 2
	x2, y2 = Tras(x,y,-d,-3*d)

	# Parte 3
	x3, y3 = Tras(x,y,3*d,-3*d)

	# Parte 4
	x4, y4 = RotarD(x,y)
	x4, y4 = Tras(x4,y4,5*d,-d)

	x = np.concatenate((x1,x2,x3,x4),axis=0)
	y = np.concatenate((y1,y2,y3,y4),axis=0)
	return x,y



if __name__ == '__main__':
	d = float(input('d:?'))
	n = int(input('n:?'))
	x = np.array([0,0,d,d])
	y = np.array([0,-d,-d,0])

	fig = plt.figure(1)
	plt.axis([-d-0.5,d+0.5,-d-0.5,d+0.5])
	for i in range(n):
		x, y = four(x,y,d)
		#plt.plot(x,y)
	plt.plot(x,y)
	plt.show()