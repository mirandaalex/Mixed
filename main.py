from Tkinter import Tk
from libs.Frames.NFrame import *
#from libs.data_base.SaveDataJSON import *
from libs.data_base.servidor1 import *
from threading import Thread
from time import sleep
from datetime import datetime
apuntadorStatusFrame=[]
New=True
stop_threads = False
listaactual=[]


def InterfazThread():
	#Se crea ventana
	root = Tk()

	#Se crea instancia NFrame
	#initF=NFrame(root)

	#Se crea frame secundario que contiene los lavelx Modulo NFrame (\libs\Frames)
	LabelFrame=LabFrame(root)
	LabelFrame.ConfigureF(668,37,12,36,"#696969")#,"#D8D8D8"
	LabelFrame.addLabel("General ",12,2,1,1,"#4a4a4a")
	LabelFrame.addLabel("Banda",12,2,92,0,"#4a4a4a")
	LabelFrame.addLabel(" ",70,2,182,0,"#4a4a4a")

	#Se crea frame secundario que contiene los textbox Modulo NFrame (\libs\Frames)
	StatusFrame=TextFrame(root)
	StatusFrame.ConfigureF(668,480,12,73,"#4a4a4a")
	StatusFrame.addListBox(ax=93,ay=23,x=10,y=0,bg="#4a4a4a")
	StatusFrame.addText(0,"   Serial Number            Status                         Date",1)
	StatusFrame.clickEventListbox(0)
	apuntadorStatusFrame.append(StatusFrame)

	ButtonsFrame=TextureFrame(root)
	ButtonsFrame.ConfigureF(413,517,680,36,"#4a4a4a")	
	if ButtonsFrame.addButtonI((0,0,206,109),30,40,1)!=-1:
		ButtonsFrame.addButtonI((0,109,206,218),30,172,2)
		ButtonsFrame.addButtonI((0,218,206,327),30,305,3)
		ButtonsFrame.addButtonI((206,0,352,109),249,40,4)
		ButtonsFrame.addButtonI((206,109,352,218),249,172,5)
		ButtonsFrame.addButtonI((206,218,352,327),249,305,6)

	root.mainloop()


def servidorM():
	global listaactual
	#servidor([apuntadorStatusFrame,0])
	pass



try:
	today = datetime.now()
	print(1,today.strftime("%d/%m/%Y %H:%M:%S"))
	#T1=Thread(target=InterfazThread )
	InterfazThread()

	today = datetime.now()
	print(2,today.strftime("%d/%m/%Y %H:%M:%S"))
	#InterfazThread()
	T3=Thread(target=servidorM)
	
	#today = datetime.now()
	#print(3,today.strftime("%d/%m/%Y %H:%M:%S"))
	#T1.start()

	#today = datetime.now()
	#print(4,today.strftime("%d/%m/%Y %H:%M:%S"))
	#T1.join()
	#print(5,today.strftime("%d/%m/%Y %H:%M:%S"))
	sleep(1)

	today = datetime.now()
	print(5,today.strftime("%d/%m/%Y %H:%M:%S"))
	T3.start()

	#today = datetime.now()
	#print(6,today.strftime("%d/%m/%Y %H:%M:%S"))
	#T1.join()

	today = datetime.now()
	print(7,today.strftime("%d/%m/%Y %H:%M:%S"))
	T3.join()

	today = datetime.now()
	print(8,today.strftime("%d/%m/%Y %H:%M:%S"))
except Exception as e:
	print "Error: unable to start thread"	
	print e
#time.sleep(4)
try:
	pass
except Exception as e:
	raise e