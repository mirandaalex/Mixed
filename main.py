from Tkinter import *
from libs.Frames.NFrame import *
from libs.data_base.Fallo import *
from libs.data_base.SaveDataJSON import *
from libs.data_base.servidor1 import *
from libs.AWS.smsaws import *
from threading import Thread
import time
apuntadorStatusFrame=[]
New=True
stop_threads = False

listaactual=[]
def InterfazThread():
	#Se crea ventana
	root = Tk()

	#Se crea instancia NFrame
	initF=NFrame(root)

	#Se crea frame secundario que contiene los lavelx Modulo NFrame (\libs\Frames)
	LabelFrame=NFrame(root,False)
	LabelFrame.ConfigureF(668,37,12,36,"#696969")#,"#D8D8D8"
	LabelFrame.addLabel("General ",12,2,1,1,"#4a4a4a")
	LabelFrame.addLabel("Banda",12,2,92,0,"#4a4a4a")
	LabelFrame.addLabel(" ",70,2,182,0,"#4a4a4a")

	#Se crea frame secundario que contiene los textbox Modulo NFrame (\libs\Frames)
	StatusFrame=NFrame(root,False)
	StatusFrame.ConfigureF(668,480,12,73,"#4a4a4a")
	StatusFrame.addListBox(ax=93,ay=23,x=10,y=0,bg="#4a4a4a")
	StatusFrame.addText(0,"   Serial Number            Status                         Date",1)
	StatusFrame.clickEventListbox(0)
	apuntadorStatusFrame.append(StatusFrame)

	ButtonsFrame=NFrame(root,False,True)
	ButtonsFrame.ConfigureF(413,517,680,36,"#4a4a4a")	
	if ButtonsFrame.addButtonI((0,0,206,109),30,40,1)!=-1:
		ButtonsFrame.addButtonI((0,109,206,218),30,172,2)
		ButtonsFrame.addButtonI((0,218,206,327),30,305,3)
		ButtonsFrame.addButtonI((206,0,352,109),249,40,4)
		ButtonsFrame.addButtonI((206,109,352,218),249,172,5)
		ButtonsFrame.addButtonI((206,218,352,327),249,305,6)

	root.mainloop()


def servidorM():
	global T1,listaactual
	servidor([T1,apuntadorStatusFrame,0])



try:
	T1=Thread(target=InterfazThread )
	
	T3=Thread(target=servidorM)
	T1.start()
	
	time.sleep(2)
	
	
	T3.start()
	
	T1.join()
	
	T3.join()
except:
	print "Error: unable to start thread"	

#time.sleep(4)