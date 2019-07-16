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
	def Server():
	# Creando el socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	# Enlace de socket y puerto
	server_address = ('192.168.0.103', 10002)
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
		#connection.setblocking(0)
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
			print(sys.stderr, 'Posicion: "%d"' % pos)
			buf = ''
			c=connection.recv(1)
			c=c.decode("utf-8")
			while c != ' ':
				buf += c
				c=connection.recv(1)
				c=c.decode("utf-8")
			area=float(buf) 
			array_area[0][pos]=area
			print(sys.stderr, 'Area: "%d"' % area)
			data = []
			while True:
				packet = connection.recv(4096)
				if not packet: 
					break
				data.append(packet)

		#connection, client_address = sock.accept()
			#arr.astype('U13')

			tempb=b"".join(data)

			print("------->",data[0:100])
			data_arr = pickle.loads(tempb)
			name = "img"+str(pos)+".png"
			cv2.imwrite(name,data_arr)	
			print('Se envió la confirmación ',text)		
		finally:
			# Cerrando conexion
			print("End")
			connection.close()
