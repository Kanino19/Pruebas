#! /usr/bin/env python
#! /usr/bin/env bash
#------------------Paquetes----------------
#------------------------------------------
from argparse import ArgumentParser
import os 
import sys 
import subprocess
#------------------------------------------

#-----------Lectura de parametros----------
#------------------------------------------
parser = ArgumentParser(prog = 'Descargas',
	description='Descargar de Mangas',	
	epilog = '''Copyright 2016
	Recomendaciones Iniciales:
	-> Configurar la obtencion de paquetes html con link
	-> Configurar la obtencion de link a descargar''',
	version = '2.0')

	# Carpeta
default_carpeta = "OP"
parser.add_argument("-c", "--carpeta", 
	action="store",
	dest="carpeta",
	default=default_carpeta,
	help="Carpeta en donde se guardara los archivos")

	# Fichero
default_link = "False"
parser.add_argument("-l", "--link", 
	action="store",
	dest="link",
	default=default_link,
	help="link de donde comenzar a descargar")

	# Cantidad de descargas
default_num = 0
parser.add_argument("-n", "--num", 
	action="store",
	dest="num",
	type = int,
	default=default_num,
	help="Numero de imagenes")

# Parsear los parametros
options = parser.parse_args()
#------------------------------------------

#-----------------Funciones----------------
#------------------------------------------
def ObtenerHtml(lineas):
	# Configuracion para encontrar el siguiente link en el html
	linea1 = lineas[14]
	linea1 = linea1.split('id="next"')[1]
	linea1 = linea1.split("href=")[1]
	linea1 = linea1.split('>')[0]
	options.link = linea1.split('"')[1]


def ObtenerLink(lineas):
	# Configuracion para encontrar el link de la imagen a descargar
	linea2 = lineas[14]
	linea2 = linea2.split('id="img"')[1]
	linea2 = linea2.split("src=")[1]
	linea2 = linea2.split(' ')[0]
	linea2 = linea2.split('"')[1]
	return linea2

def Link():
	# Verificar si se ingreso el link inicial para descargar
	if options.link == 'False':
		print "Ingrese el link inicial para comenzar la descarga"
		exit(0)

	else:
		print '-- Descargando link . . . Espere . . . --'
		contador = 0
		rango = range(0,options.num,options.num/5)
		urls = []
		for i in range(options.num):
			# Generar comando de descargar
			aux_url = "wget %s -o log.txt"%options.link

			# Extraer nombre del html
			name = options.link.split('/')[-1]

			# Descargar html
			subprocess.call(aux_url,shell=True)
			
			# Abrir y extraer aux_url y urls_img
			f = open(name,"r")
			lineas = f.readlines()
			f.close()

			# Extraer aux_url y urls_img
			ObtenerHtml(lineas)
			
			# Agregar urls_img	
			urls.append(ObtenerLink(lineas))
			
			# Eliminar archivo descargado
			os.remove(name)

		# Guargar los urls en el archivo link_manga.txt
		g = open('link_manga.txt','w')
		urls = '\n'.join(urls)
		g.write(urls)
		g.close()
		# Medida tomada en caso la descarga se cancele

def Descarga():
	Sedescarga = True
	# Posicionarse en el home
	if os.getcwd() != '/home/jkahn/':
		os.chdir("/home/jkahn/")

	# La carpeta existe
	if os.path.exists('/home/jkahn/'+options.carpeta) == False :
		# Creamos la carpeta
		os.mkdir(options.carpeta)
		# Ingresamos a la carpeta
		os.chdir('/home/jkahn/'+options.carpeta)
		# Corremos Link()
		Link()

	else :
		# Ingresamos a la carpeta
		os.chdir('/home/jkahn/'+options.carpeta)
		if os.path.exists('/home/jkahn/'+options.carpeta+'/link_manga.txt') == False:
			Link()

	if Sedescarga:
		# Comando de terminal
		comando = "wget -c -i %s"%'link_manga.txt'
		RunCommands(comando)
			

def RunCommands(commands):
	# Si es un solo comando
	if type(commands) == str:
		print "Running Command"
		subprocess.call(commands, shell=True)

	# Si es un array de comandos
	else :
		for cmd in commands:
			print "Running Command"
			subprocess.call(cmd, shell=True)
#------------------------------------------

if __name__ == '__main__':
	Descarga()
