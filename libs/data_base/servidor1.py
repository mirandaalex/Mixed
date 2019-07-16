#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:44:13 2019

@author: Del Valle
"""
import numpy as np
import socket,cv2
import sys,pickle
import matplotlib.pyplot as plt
from PIL import Image
from libs.data_base.SaveDataJSON import *
from threading import Thread
from libs.AWS.smsaws import *
#from libs.data_base.firebaseadd import *
def servidor(listatemp):
	
	# Creando el socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	# Enlace de socket y puerto
	server_address = ('192.168.0.5', 10002)
	print(sys.stderr, 'empezando a levantar %s puerto %s' % server_address)
	sock.bind(server_address)

	# Escuchando conexiones entrantes
	sock.listen(50)
	array_area=np.zeros((1,100))
	text="OK "
	#connection, client_address = sock.accept()
	while True:
		# Esperando conexion
		print (sys.stderr, 'Esperando para conectarse')
		connection, client_address = sock.accept()
		try:
			print(sys.stderr, 'conexion desde', client_address)
		
			buf = ''
			while True:
				c=connection.recv(1)
				if c:
					break
			c=c.decode("utf-8")
			while c != ' ':
				buf += c
				c=connection.recv(1)
				c=c.decode("utf-8")
			pos=int(buf)
			#print(sys.stderr, 'Posicion: "%d"' % pos)
			buf = ''
			c=connection.recv(1)
			c=c.decode("utf-8")
			while c != ' ':
				buf += c
				c=connection.recv(1)
				c=c.decode("utf-8")
			area=float(buf) 
			
			array_area[0][pos]=area
			#print(sys.stderr, 'Area: "%d"' % area)
			data = []
			while True:
				packet = connection.recv(4096)
				if not packet: 
					break
				data.append(packet)
			severity=""
			asca=ManagementJson("Helloword.json")
			if area<1500:	
				asca.addError("Riesgo Bajo")
				severity="Riesgo Bajo"
			elif area>1500 and area<3500:
				asca.addError("Riesgo Medio")
				severity="Riesgo Medio"
			else:
				asca.addError("Riesgo Alto")
				severity="Riesgo Alto"
				#Cadena a enviar por mensaje de texto
				AWS("High damage")
			
			lista=asca.ultimosN(1)
			#FireBase
			# try:
			# 	newFailure(lista["serial"][0],0,severity,False)
			# except Exception as e:
			# 	raise e	

			print("area...........",area, "serial................. ",lista["serial"][0])
			
			data_arr = pickle.loads(b"".join(data))
			if sys.platform.startswith('win32'):
				name = "image\\"+lista["serial"][0]+".jpg"
			elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
				name = "image/"+lista["serial"][0]+".jpg"
		
			
			cv2.imwrite(name,data_arr)	
			#print('Se envió la confirmación ',text)
			
			
			if listatemp[0].isAlive()==False:
				return 0
			#print("----------------------------->>>>",listatemp[1])
			if lista["status"][0]=="Riesgo Medio":
				listatemp[1][0].addText(0,"   "+lista["serial"][0]+"        "+lista["status"][0]+"      "+lista["date"][0])
			else:
				listatemp[1][0].addText(0,"   "+lista["serial"][0]+"        "+lista["status"][0]+"          "+lista["date"][0])
			
			#listatemp[1][0].addText(1,lista["status"][0])
			#listatemp[1][0].addText(2,lista["date"][0])		
		finally:
			# Cerrando conexion
			print("End")
			connection.close()
			