from json import load, dump
import sys
from datetime import datetime
#obasd=ManagementJson()
#obasd.wri
#Clase ManagementJson hija de object
#Esta clase nos permite crear pseudo base de datos a traves de documentos JSON
class ManagementJson(object):

	"""docstring for ClassName"""
	#Modifica una instacia justo despues de ser creada
	#@[in] name es el nombre del archivo "nombre.json" de tipo candena
	def __init__(self,name):
		root=self.sysPlatforms(name)
		self.root=root
		self.loadFile(root)

	#Busca la ruta de un archivo dependiendo el S.O.
	def sysPlatforms(self,name):	
		if sys.platform.startswith('win32'):
			root="docs\\"+str(name)
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin') :
			root="docs/"+str(name)
		return root

	#Verifica que el archivo exista de lo contrario lo creara 
	def loadFile(self,root):
		try:
			data_file=open(root,"r") 
			data=load(data_file)
			self.synchronizeSize(len(data["serial"]))
			data_file.close
		except Exception as e:
			with open(root,"w") as data_file:
				dump={"serial":[] ,"status":[],"date":[],"pos":[]}
				json.dump(dump,data_file) 
				self.synchronizeSize(0)

	#Add un nuevo elemento a el archivo
	def addError(self,status,pos=0):
		today = datetime.now()
		data_file=open(self.root,"r")
		data=load(data_file)
		self.plusSize()
		#Si esta vacio incia la serializacion en 000000
		if int(len(data["serial"]))==0:
			data={"serial":[] ,"status":[],"date":[],"pos":[]}
			data["serial"].append("000000")
			data["status"].append(status)
			data["date"].append(str(today.strftime("%d/%m/%Y %H:%M:%S")))
			data["pos"].append(pos)

		#Si no esta vacia continua con la serializacion
		else:
			serial=str(int(len(data["serial"])))
			if len(serial)<6:
				a=len(serial)
				for x in range(0,6-a):
					serial="0"+serial

			data["serial"].append(serial)
			data["status"].append(status)
			data["date"].append(str(today.strftime("%d/%m/%Y %H:%M:%S")))
			data["pos"].append(pos)
		data_file.close
		data_file=open(self.root,"w")
		json.dump(data,data_file)

	#elimina un elemento determinado por su serial, si falla regresa 0
	def delError(self,serial):
		data_file=open(self.root,"r")
		data=load(data_file)
		if int(len(data["serial"]))!=0:
			cont=0
			for temp in data["serial"]:
				if temp==serial:
					break
				cont+=1
			if cont<len(data["serial"]):
				data["serial"].pop(cont)
				data["status"].pop(cont)
				data["date"].pop(cont)
				data["pos"].pop(cont)
				data_file.close
				data_file=open(self.root,"w")
				json.dump(data,data_file)
				return 1
		data_file.close
		return 0

	#Carga todos los elementos de un documento y los regresa como un diccionario{"elemento":[lista],"elemento2":[],....}
	def loadList(self):
		data_file=open(self.root,"r")
		data=load(data_file)
		data_file.close
		return data

	#Busca un elemento en especifico y si lo encuentra los regresa como lista [dato 1, dato 2, ....], si falla regresa 0
	def searchError(self,serial):
		data_file=open(self.root,"r")
		data=load(data_file)
		if int(len(data["serial"]))!=0:
			cont=0
			for temp in data["serial"]:
				if temp==serial:
					break
				cont+=1
			if cont<len(data["serial"]):
				return [data["serial"][cont],data["status"][cont],data["date"][cont],data["pos"][cont]]
		return 0

	#Busca los ultimos N elementos de un archivo y lo regresa como un diccionario{"elemento":[lista],"elemento2":[],....}, si falla regresa 0
	def ultimosN(self,N):
		data_file=open(self.root,"r")
		data=load(data_file)
		A=len(data["serial"])-N
		if A<0:
			A=0
		if int(len(data["serial"]))!=0:
			temp={"serial":[] ,"status":[],"date":[],"pos":[]}
			for cont in range(A,len(data["serial"])):
				temp["serial"].append(data["serial"][cont])
				temp["status"].append(data["status"][cont])
				temp["date"].append(data["date"][cont])
				temp["pos"].append(data["pos"][cont])
			#print("---->",temp)
			return temp
		return 0

	#Busca un intervalo con inicio I y final F y lo regresa como un diccionario{"elemento":[lista],"elemento2":[],....}, si falla regresa 0
	def intervaloIF(self,I,F):
		data_file=open(self.root,"r")
		data=load(data_file)
		F+=1
		if F<I:
			local=I
			I=F
			F=local
		if I<0:
			I=0
		if F>len(data["serial"]):
			F=len(data["serial"])

		if int(len(data["serial"]))!=0:
			temp={"serial":[] ,"status":[],"date":[],"pos":[]}
			for cont in range(I,F):
				temp["serial"].append(data["serial"][cont])
				temp["status"].append(data["status"][cont])
				temp["date"].append(data["date"][cont])
				temp["pos"].append(data["pos"][cont])
			return temp
		return 0
	
	def plusSize(self):
		fa=open("config.txt","r+")
		fa.seek(7)
		maxi=fa.readline()
		fa.seek(7)
		fa.write(str(int(maxi)+1)+"\n")
		fa.close()

	def synchronizeSize(self,number):
		fa=open("config.txt","r+")
		fa.seek(7)
		fa.write(str(number)+"\n")
		fa.close()