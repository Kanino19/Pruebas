#! /usr/bin/env python
#! /usr/bin/env bash
from argparse import ArgumentParser
import os 
import sys 
import subprocess

#lectura de parametros

parser = ArgumentParser(prog = 'Descargas',
	description='Descargar de Mangas',	
	epilog = 'Copyright 2016',
	version = '2.0')

#Carpeta
default_carpeta = "OP"
parser.add_argument("-c", "--carpeta", 
	action="store",
	dest="carpeta",
	default=default_carpeta,
	help="Carpeta en donde se guardara los archivos")

#Fichero
default_link = "False"
parser.add_argument("-l", "--link", 
	action="store",
	dest="link",
	default=default_link,
	help="link de donde comenzar a descargar")

#Cantidad de descargas
default_num = 0
parser.add_argument("-n", "--num", 
	action="store",
	dest="num",
	type = int,
	default=default_num,
	help="Numero de imagenes")

#parsear los parametros
options = parser.parse_args()

# funciones
#------------------------------------------
def Link():
	if options.link == 'False':
		print "Ingrese el link inicial para comenzar la descarga"
		return 0
	else:
		urls = []
		for i in range(options.num):
			#Extraer comando y nombre
			aux_url = "wget %s"%options.link
			
			name = options.link.split('/')[-1]
			print aux_url
			print name
			#Descargar
			subprocess.call(aux_url,shell=True)
			
			#Abrir y extraer aux_url y urls_img
			f = open(name,"r")
			lineas = f.readlines()
				#urls
			linea1 = lineas[14]
			linea1 = linea1.split('id="next"')[1]
			linea1 = linea1.split("href=")[1]
			linea1 = linea1.split('>')[0]
			options.link = linea1.split('"')[1]
				#urls_img
			linea2 = lineas[14]
			linea2 = linea2.split('id="img"')[1]
			linea2 = linea2.split("src=")[1]
			linea2 = linea2.split(' ')[0]
			urls.append(linea2.split('"')[1])

			#Cerrar archivo
			f.close()

			#Eliminar archivo descargado
			os.remove(name)
		return urls

def Descarga():

	

def RunCommands(commands):
	for cmd in commands:
		print "Running Command"
		subprocess.call(cmd, shell=True)

def main():
		os.chdir("/home/jkahn/")
		downland = []
		urls = Link()
		if urls!=0:
			for url in urls:
				comando = "wget -c %s"%url
				downland.append(comando)
			try :
				os.mkdir(options.carpeta)
				os.chdir("/home/jkahn/"+options.carpeta)
			except :
				os.chdir("/home/jkahn/"+options.carpeta)
			RunCommands(downland)
#------------------------------------------

if __name__ == '__main__':
	main()
