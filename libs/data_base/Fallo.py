#clase Fallo
#Esta clase sirve para tener una manera de recivir informacion y oredenarla
#Metodos get sirven para obtener los argumentos(privados __@)
#Metodos get sirven para modificar los argumentos(privados __@)
#__init__ es como un constructor pero seria erroneo decir que es uno
#__init__ se ejecuta cuando creas una instancia de la clase
class Fallo(object):
	"""docstring for Fallo"""
	def __init__(self,typee,serial,status,date):
		self.__status = status
		self.__date=date
		self.__serial=serial
		self.__type=typee

	def getSerial(self):
		return self.__serial

	def setSerial(self,nserial):
	 	self.__serial=nserial
	 		
	def getDate(self):
		return self.__date

	def setDate(self,ndate):
		self.__date=ndate

	def getStatus(self):
		return self.__status

	def setStatus(self,nstatus):
		self.__status=nstatus

	def getType(self):
		return self.__type

	def setType(self,ntype):
	 	self.__type=ntype