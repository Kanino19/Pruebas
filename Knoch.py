import numpy as np
import matplotlib.pyplot as plt


def Rotar60(x,y):
	return .5*x - 0.5*(3**0.5)*y , 0.5*(3**0.5)*x + .5*y

def Rotar_60(x,y):
	return .5*x + 0.5*(3**0.5)*y , -.5*(3**0.5)*x + 0.5*y

def Tras(x,y,d1,d2):
	return x+d1, y+d2

def Escal(x,y,r):
	return r*x, r*y

def four(x,y,d):
	x,y = Escal(x,y,1/3.)
	d = d/6.
	# Parte 1
	x1, y1 = Rotar60(x,y)
	x1, y1 = Tras(x1,y1,2*d,0)

	# Parte 2
	x2, y2 = Rotar_60(x,y)
	#print x2,y2
	x2, y2 = Tras(x2,y2,3*d,(3**.5)*d)
	#print x2,y2

	# Parte 3
	x3, y3 = Tras(x,y,4*d,0)

	x = np.concatenate((x,x1,x2,x3),axis=0)
	y = np.concatenate((y,y1,y2,y3),axis=0)
	return x,y

if __name__ == '__main__':
	d = float(input('d:?'))
	n = int(input('n:?'))
	x = np.array([0,d])
	y = np.array([0,0])

	fig = plt.figure(1)
	plt.axis([-.05*d,1.05*d,-0.5,0.5*d])
	for i in range(n):
		x, y = four(x,y,d)
		plt.plot(x,y)
	plt.plot(x,y)
	plt.show()