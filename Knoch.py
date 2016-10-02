import numpy as np
import matplotlib.pyplot as plt


def Rotar60(x,y):
	return .5*x - 0.5*(3**0.5)*y , 0.5*(3**0.5)*x + .5*y

def Rotar120(x,y):
	return -.5*x - 0.5*(3**0.5)*y , .5*(3**0.5)*x - 0.5*y

def Tras(x,y,d1,d2):
	return x+d1, y+d2

def Escal(x,y,r):
	return r*x, r*y

def four(x,y,d):
	x,y = Escal(x,y,1/3.)
	d = 0.25*d
	# Parte 1
	x1, y1 = RotarI(x,y)
	x1, y1 = Tras(x1,y1,-d,-d)
	x1, y1 = x1[::-1],y1[::-1]

	# Parte 2
	x2, y2 = Tras(x,y,-d,-3*d)

	# Parte 3
	x3, y3 = Tras(x,y,3*d,-3*d)

	x = np.concatenate((x1,x2,x3),axis=0)
	y = np.concatenate((y1,y2,y3),axis=0)
	return x,y

if __name__ == '__main__':
	d = 1.#float(input('d:?'))
	#n = int(input('n:?'))
	x = np.array([0,d])
	y = np.array([0,0])

	fig = plt.figure(1)
	plt.axis([-d-0.5,d+0.5,-d-0.5,d+0.5])
	#for i in range(n):
		#x, y = four(x,y,d)
		#plt.plot(x,y)
	plt.plot(x,y)
	plt.plot(x1,y1)
	plt.plot(x2,y2)
	plt.show()