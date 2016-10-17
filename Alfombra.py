import numpy as np
import pygame
import os

# Funciones
def four(x,y,a,b):
	x,y = Escal(x,y,1/3)
	a = a/3
	b = b/3
	aux = x
	auy = y
	puntos = [[1,0],[2,0],[0,1],[2,1],[0,2],[1,2],[2,2]]
	for i,j in puntos:
		x1, y1 = Tras(x,y,i*a,j*b)
		aux = np.concatenate((aux,x1),axis=0)
		auy = np.concatenate((auy,y1),axis=0)
	return aux, auy

def Tras(x,y,d1,d2):
	return x+d1, y+d2

def Escal(x,y,r):
	return r*x, r*y

# Iniciar pygame
pygame.init()
Finish = False
width = 800 # ancho
height = 334 # alto
screen = pygame.display.set_mode((width,height)) # ventana

white = (255,255,255) # Color blanco


# Imagen
Img = pygame.image.load('ojo.jpg') 
WH = Img.get_size()
# Parametros
sw = 799
sh = sw*WH[1]/WH[0]
rect = pygame.Rect(0,0,sw,sh)

# Generar puntos
pX = np.array([0])
pY = np.array([0])
pX, pY = four(pX,pY,sw,sh)

# Escalar
Img0 = pygame.transform.scale(Img,(sw/3,sh/3))



# Bucle

for j in range(6):
	screen.fill(white)
	for i in range(8):
		screen.blit(Img0,(pX[i],pY[i]))
	Img0 = screen.subsurface(rect).copy()
	Img0 = pygame.transform.scale(Img0,(sw/3,sh/3))
	pygame.display.update()

while not Finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Finish = True