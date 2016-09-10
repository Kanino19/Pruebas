import math as mt
import numpy as np
import matplotlib.pyplot as plt



def Tras(x,y,d1,d2):
	return x+d1, y+d2

def Escal(x,y,r):
	return r*x, r*y

def Refle(x,y):
	return x,-y

def Nine(x,y,d,m,p):
	c = (m-2)/3
	x,y = Escal(x,y,(m-2.)/(3.*m))
	d = d/(1.*m)
	p = 3*p+1

	# Parte 1
	x1, y1 = x, y

	# Parte 2
	x2, y2 = Refle(x,y)
	x2, y2 = x2[::-1],y2[::-1]
	x2, y2 = Tras(x2,y2,0.,(m-c-1)*d)

	# Parte 3
	x3, y3 = Tras(x,y,0.,(m-c)*d)



	# Parte 4
	x4, y4 = x2[::-1],y2[::-1]
	x4, y4 = Tras(x4,y4,(m-2*c-1)*d,(m-2*c-1)*d)

	# Parte 5
	x5, y5 = x[::-1],y[::-1]
	x5, y5 = Tras(x5,y5,(m-2*c-1)*d,(m-2*c-1)*d)

	# Parte 6
	x6, y6 = x2[::-1],y2[::-1]
	x6, y6 = Tras(x6,y6,(m-2*c-1)*d,-(m-2*c-1)*d)



	# Parte 7
	x7, y7 = x,y
	x7, y7 = Tras(x7,y7,(m-c)*d,0)
	
	# Parte 8
	x8, y8 = x2,y2
	x8, y8 = Tras(x8,y8,(m-c)*d,0)
	
	# Parte 9
	x9, y9 = x,y
	x9, y9 = Tras(x9,y9,(m-c)*d,(m-c)*d)

	x = np.concatenate((x1,x2,x3,x4,x5,x6,x7,x8,x9),axis=0)
	y = np.concatenate((y1,y2,y3,y4,y5,y6,y7,y8,y9),axis=0)

	m = 3*m+2
	return x,y,m,p



if __name__ == '__main__':
	d = float(input('d:?'))
	n = int(input('n:?'))
	m= 8
	p= 1
	x = np.array([0,0,0.5*d,0.5*d,d,d])
	y = np.array([0,d,d,0,0,d])

	plt.figure(1)
	#x,y = Nine(x,y,d)
	plt.axis([-d-0.5,d+0.5,-d-0.5,d+0.5])
	if n==1:
		plt.plot(x,y)
	else:
		for i in range(n-1):
			x, y, m, p = Nine(x,y,d,m,p)
	plt.plot(x,y)
	plt.show()