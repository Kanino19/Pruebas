# --------------- Package ---------------
import numpy as np
import matplotlib.pyplot as plt
# ----------------------------------------


# --------------- Class RSA---------------
class KeyRsa():
	# p and q must be prime
	def __init__(self, p, q):
		self.n = p*q
		self.phi = (p-1)*(q-1) #Function Euler
		self.Coprime() #Public key
		self.Inve() #Secret key
		print 'Datos'
		print 'n: '+str(self.n)
		print 'e: '+ str(self.e), 'd:'+str(self.d)

	def Coprime(self):
		auxe = 2
		cop = self.Eucli(self.phi, auxe)
		while cop != 1:
			auxe += 1
			cop = self.Eucli(self.phi, auxe)
		self.e = auxe

	def Inve(self):
		x = self.EucliEx(self.phi, self.e)
		if x[0] != 1:
			print '%i no es invertible modulo %i'%(self.e,self.phi)
			exit()
		else:
			if x[2] < 0:
				self.d = self.phi + x[2]
			else :
				self.d = x[2]

	def Eucli(self, a, b):
		resto = np.min([a,b])
		if a < b:
			c = b
			b = a
			a = c
		while a%b != 0:
			resto = a%b
			a = b
			b = resto
		return resto

	def EucliEx(self, a, b):
		resto = np.min([a,b])
		x1, y1 = 1, 0
		x0, y0 = 0, 1
		r1 = a
		r0 = b
		while a%b != 0:
			q = a/b
			resto = a%b
			a = b
			b = resto
			x = x1 - q*x0
			y = y1 - q*y0
			
			x1, y1 = x0, y0
			x0, y0 = x, y
			r1 = r0
			r0 = resto
		return [resto,x0,y0]
# ----------------------------------------


# --------------- Functions ---------------
# Mejorar sin utilizar division sino exponenciacion
def ST(n):
	num = 0
	a = n
	while a >= 256:
		num += 1
		a = a/256
	return num

def Base10(m):
	lm = len(m)
	mb = sum(m[i]*(256**(lm-i-1)) for i in range(lm))
	return mb

def Base59(m,s):
	mb = []
	while m != 0:
		mb.append(m%256)
		m = m/256
	mb = mb[::-1]
	if len(mb)<s:
		mb = (s-len(mb))*[0] + mb
	return mb

def Expo(a,m,n):
	m = bin(m)[2:]
	e = 1
	k = a
	for i in range(len(m)-1,-1,-1):
		if int(m[i]) == 1:
			e = (e*k)%n
		k = (k**2)%n
	return e

def AaS(m):
	auxm = ''
	for i in range(len(m)):
		auxm += m[i]
	return auxm

# need: md e n s t 
# return: me
# Encriptar letra por letra
def Encriptar(n,e,m,s):
	l = len(m)
	# Combierte cada letra en su valor ASCII
	m = [ord(m[j]) for j in range(l)]
	# Calcula las posiciones de las columnas
	bl = range(0,l,s)+[l]
	# Cambio de base para cada bloque de s letras
	m = [Base10(m[bl[r]:bl[r+1]]) for r in range(len(bl)-1)]
	# Encriptando
	me = []
	k = len(m)
	for i in range(k):
		aux = Expo(m[i],e,n)
		aux = Base59(aux,s+1)
		me += aux
	# Texto Codificado
	#print self.me
	me = [chr(me[k]) for k in range(len(me))]
	me = AaS(me)
	return me

# need: me d n s t 
# return: md
# Desencriptar letra por letra
def Desencriptar(n,d,m,s):
	l = len(m)
	m = [ord(m[j]) for j in range(l)]
	bl = range(0,l,s+1)+[l]
	m = [Base10(m[bl[r]:bl[r+1]]) for r in range(len(bl)-1)]
	md = []
	k = len(m)
	for i in range(k):
		aux = Expo(m[i],d,n)
		aux = Base59(aux, s)
		md += aux
	l = len(md)
	md = [chr(md[j]) for j in range(l)]
	md = AaS(md)
	return md
# ----------------------------------------

# Mejorar la eleccion de la clave publica
# ingresar 2 primos o importarlos de un archivos
# para mejorar la seguridad se olvida de p, q y phi
p = 2**17 - 1 # p = 131071
q = 2**19 - 1 # q = 524287
# Generate public and secret keys
r = KeyRsa(p,q)

# save n, e, d, s
n = r.n
e = r.e
d = r.d
s = ST(n)
m = 'Joseph Luis Kahn Casapia Kanino19 Overlord19'
print m
print 'Encriptando por bloques el mensaje'
me = Encriptar(n,e,m,s)
print me
print '\n-------------------\n'
print 'Desencriptando por bloques el mensaje'
md = Desencriptar(n,d,me,s)
print md
