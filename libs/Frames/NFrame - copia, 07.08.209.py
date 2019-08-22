from Tkinter import *
from cv2 import imread,imshow
from PIL import Image, ImageTk
from libs.data_base.SaveDataJSON import *

	
#Clase NFrame hija de Frame de tkinter
#Esta clase crea permite crear frames y configurarlos, asi como agregarle widgets
#__init__ es como un constructor pero seria erroneo decir que es uno
#__init__ se ejecuta cuando creas una instancia de la clase

class NFrame(Frame):

	"""docstring for ClassName"""
	#Crea el Frame principal y coloca imagenes
	#parametros
	#@[in] master es la ventana padre donde se colocara el frame
	#@[in] inicial es un boolean que es True si es el primer frame creado
	#@[in] img es un boolean que indica si debe de pregargar texturas para un frame
	#si no le proporcionamos ningun dato a incial tendra por defecto True
	def __init__(self, master,inicial=True,img=False):
		Frame.__init__(self,master)
		self.master = master
		self.__list_label=[]
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		self.__texture=[]
		if inicial==True:
			self.init_window(master)
		if img==True:
			self.__loadIMG()

	#add imagenes dependiendo del tipo de sistema sobre el que opera el programa
	#Modifica las caracteristicas de la ventana principal
	def init_window(self,master):
		self.master.title("MOTVIAL")
		if sys.platform.startswith('win32'):
			self.master.iconbitmap("image\\cod.ico")
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			#self.master.iconbitmap("image/cod.ico")
			pass
		
		self.master.geometry("1114x608")
		self.master.configure(bg="#353535")
		self.master.resizable(1,1)
		self.configure(height=300,width=10 ,background="#353535")
		self.pack(side=RIGHT,ipadx=0, ipady=0)

	#Precarga las texturas para despuer ser recortadas
	def __loadIMG(self):
		try:
			if sys.platform.startswith('win32'):
				ruta="image\\texture.png"
			elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
				ruta="image/texture.png"
			self.__texture.append(Image.open(ruta))
		except Exception as e:
			pass			

	#Permite configurar un frame creado
	def ConfigureF(self,ax=600,ay=52,x=0,y=0,bg="#353535"):
		self.configure(height=ay, width=ax ,background=bg)
		self.place(x=x,y=y)

	#Crea un Label
	def addLabel(self,textvar="NONE",ax=4,ay=10,x=0,y=0,bg="#353535",fontcolor="#FFFFFF"):
		label=Label(self,height=ay, width=ax,background=bg,text=textvar,fg=fontcolor)
		label.place(x=x,y=y)
		self.__list_label.append(label)
		return label

	#Crea un TextBox
	def addListBox(self,ax=600,ay=52,x=0,y=0,bg="#B4045F"):
	
		scrolly=Scrollbar(self,activebackground="#171212",bg="#171212",orient=VERTICAL,troughcolor="#171212")
		
		listbox=Listbox(self,height=ay, width=ax ,background=bg,borderwidth=0,highlightcolor="#4d86a1",selectbackground="#4d86a1",activestyle=NONE,highlightbackground="#4a4a4a",yscrollcommand=scrolly.set)
		listbox.config(font=("", 10),fg="#FFFFFF")
		listbox.place(x=0,y=0)
		scrolly.place(x=651,y=0,height=387)	
		self.__list_listbox.append(listbox)
		self.__list_scrollbar.append(scrolly)
		for x in self.__list_listbox:
			x.configure(yscrollcommand=scrolly.set)
		scrolly.configure(command=self.__yview)
		
	#metodo privado add scrollbar a los textbox
	def __yview(self, *args):
		for x in self.__list_listbox:
			x.yview(*args)

	def clickEventListbox(self,index):
		self.__list_listbox[index].configure(selectmode=SINGLE)
		self.__list_listbox[index].bind('<Double-1>',self.__openImage)

	def Error(self,error="Se produjo un error"):
		Ventana2 = Toplevel(self.master)
		Ventana2.configure(height=100,width=260,bg="#4a4a4a")
		Ventana2.title("Error")
		Error=Label(Ventana2,text=error,bg="#4a4a4a",fg="#FFFFFF")
		Error.place(x=40,y=15)
		Error.config(font=("", 12))
		Salir=Button(Ventana2,width=10,text="Salir",command=Ventana2.destroy)
		Salir.place(x=85,y=55)

	def __openImage(self,event):
		try:		
			index=self.__list_listbox[0].get(self.__list_listbox[0].curselection())
			#print(index[3:16])
			if str(index[3:16])!="Serial Number":
				if sys.platform.startswith('win32'):
					root="image\\"+str(index[3:9])+".jpg"
				elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
					root="image/"+str(index[3:9])+".jpg"
				#print(root)	
				im=imread(root)
				imshow("image",im)
		except Exception as e:
			self.Error("Error al cargar la imagen")

	

	#add texto en pantalla		
	def addText(self,x,text,n):
		self.__list_listbox[x].insert(END,text)
		if (n+2)%2==0:
			self.__list_listbox[x].itemconfigure(n,bg="#696969")
	def retTextBox(self,x):
		return self.__list_listbox[x]
	#add button
	def addButtonI(self,dim=(0,0,206,109),x=0,y=0,command=0):
		try:
			crop=self.__texture[0].crop(dim)
			render=ImageTk.PhotoImage(crop)
			nbutton=Button(self,image=render,bg="#4a4a4a",borderwidth=0,activebackground="#4d86a1")
			nbutton.image=render
			nbutton.place(x=x,y=y)
			self.__list_button.append(nbutton)
			if command==1:
				nbutton.configure(command=self.showOne)
			elif command == 2:
				nbutton.configure(command=self.showAll)
			elif command==3:
				pass
			elif command ==4:
				nbutton.configure(command=self.master.destroy)
			
			return nbutton
		except Exception as e:
			self.Error("Error al cargar Texturas")
			return -1
	
		

	def showAll(self):
		Ventana2 = Toplevel(self.master)
		try:
			Poss=[0,50]
			maxi=self.buscMax()
			if int(maxi)<Poss[1]:
				Poss[1]=int(maxi)
			Ventana2.configure(height=45,width=25,bg="#4a4a4a")
			Ventana2.resizable(0,0)
			frameAux=Frame(Ventana2,bg="#4a4a4a",borderwidth=0)
			frameAux.pack(fill=BOTH)
			scrolly=Scrollbar(frameAux,orient=VERTICAL)	
			self.listbox1=Listbox(frameAux, width=90 ,background="#4a4a4a",borderwidth=0,fg="#FFFFFF",highlightcolor="#4d86a1",highlightbackground="#4d86a1",yscrollcommand=scrolly.set)
			self.listbox1.config(font=("", 11))
			self.listbox1.pack(side=LEFT)
			scrolly.pack(side=RIGHT,fill=Y)
			scrolly.configure(command=self.yview)
			self.load50(Poss)
			if sys.platform.startswith('win32'):
				ruta="image\\GoBack.png"
				ruta2="image\\GoOn.png"
			elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
				ruta="image/GoBack.png"
				ruta2="image/GoOn.png"
			load=Image.open(ruta)
			render=ImageTk.PhotoImage(load)
			load2=Image.open(ruta2)
			render2=ImageTk.PhotoImage(load2)
			backbutton1=Button(Ventana2, image=render,bg="#4a4a4a",borderwidth=0,activebackground="#4d86a1",highlightcolor="#4d86a1",highlightbackground="#4a4a4a",command=lambda:self.load50(Poss,"-"))
			backbutton1.image=render
			backbutton1.pack(side=LEFT)
			backbutton2=Button(Ventana2, image=render2,bg="#4a4a4a",borderwidth=0,activebackground="#4d86a1",highlightcolor="#4d86a1",highlightbackground="#4a4a4a",command=lambda:self.load50(Poss,"+"))
			backbutton2.image=render2
			backbutton2.pack(side=LEFT)
			backbutton3=Button(Ventana2,height=2, width=10, text="Back",command=lambda:self.Switch(self.master,Ventana2))
			backbutton3.pack(side=RIGHT)
		except Exception as e:
			Ventana2.destroy()
			self.Error("Se produjo un error al cargar")

	def yview(self, *args):
			self.listbox1.yview(*args)

			


	def showOne(self):

		
		Ventana2 = Toplevel(self.master)
		try:
			Ventana2.configure(height=210,width=428,bg="#FFFFFF")
			Ventana2.resizable(1,1)
			Ventana2.title("Buscar")
			
			frameAux=Frame(Ventana2,height=210,width=428,bg="#4a4a4a")
			frameAux.place(x=0,y=0)

			if sys.platform.startswith('win32'):
				r="image\\BuscarBosch.png"
				ruta="image\\Back.png"
				ruta2="image\\SearchOne.png"
				
			elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
				r="image/BuscarBosch.png"
				ruta="image/Back.png"
				ruta2="image/SearchOne.png"

			l=Image.open(r)
			re=ImageTk.PhotoImage(l)
			labelFont=Label(frameAux,image=re,borderwidth=0) 
			labelFont.image=re
			labelFont.place(x=0,y=0)
			
			labelText1=Label(frameAux,height=1,width=24,bg="#4a4a4a",text="Serie",fg="#FFFFFF",anchor=W) 
			labelText1.config(font=("Tahoma", 11))
			labelText1.place(x=15,y=25)
			labelText11=Label(frameAux,height=1,width=24,bg="#4a4a4a",fg="#FFFFFF",anchor=W) 
			labelText11.config(font=("Tahoma", 11))
			labelText11.place(x=210,y=25)

			labelText2=Label(frameAux,height=1,width=24,bg="#696969",text="Gravedad",fg="#FFFFFF",anchor=W)
			labelText2.config(font=("Tahoma", 11))
			labelText2.place(x=15,y=50)
			labelText22=Label(frameAux,height=1,width=24,bg="#696969",fg="#FFFFFF",anchor=W)
			labelText22.config(font=("Tahoma", 11))
			labelText22.place(x=210,y=50)

			labelText3=Label(frameAux,height=1,width=24,bg="#4a4a4a",text="Fecha",fg="#FFFFFF",anchor=W)
			labelText3.config(font=("Tahoma", 11))
			labelText3.place(x=15,y=75)
			labelText33=Label(frameAux,height=1,width=24,bg="#4a4a4a",fg="#FFFFFF",anchor=W)
			labelText33.config(font=("Tahoma", 11))
			labelText33.place(x=210,y=75)
			
			labell=Label(frameAux,height=1,width=25,bg="#4a4a4a",text="Ingresa el numero de serie",fg="#FFFFFF",anchor=W)
			#labell.place(x=15,y=135)
			labell.config(font=("Tahoma", 11))

			listbox3=Entry(frameAux,width=24, justify=RIGHT,bg="#696969",fg="#FFFFFF",borderwidth=0)
			listbox3.place(x=210,y=125)
			listbox3.config(font=("Tahoma", 11))

				
			load=Image.open(ruta)
			render=ImageTk.PhotoImage(load)
			backbutton=Button(frameAux,image=render,bg="#8d8e8c",borderwidth=0,activebackground="#696969",command=lambda:self.Switch(self.master,Ventana2))
			backbutton.image=render
			backbutton.place(x=245,y=155)
			load2=Image.open(ruta2)
			render2=ImageTk.PhotoImage(load2)
			searchButton=Button(frameAux,image=render2,bg="#8d8e8c",borderwidth=0,activebackground="#c4c4c4",command=lambda:self.load1(listbox3,labelText11,labelText22,labelText33))
			searchButton.image=render2
			searchButton.place(x=324,y=155)
		except Exception as e:
			Ventana2.destroy()
			self.Error("Se produjo un error al cargar")
		
		



	def Switch(self,root,Ventana2):
		root.deiconify()
		Ventana2.destroy()

	def load50(self,Poss,mode="a"):
		maxi=self.buscMax()
		I=Poss[0]
		F=Poss[1]
		if mode=="+":
			Poss[1]=Poss[1]+50
			if Poss[1]>int(maxi):
				Poss[1]=int(maxi)
			Poss[0]=Poss[1]-50
			if Poss[0]<0:
				Poss[0]=0
		elif mode=="-" and Poss[0]!=0:
			Poss[0]=Poss[0]-50
			if Poss[0]<0:
				Poss[0]=0
			Poss[1]=Poss[0]+50
			if Poss[1]>int(maxi):
				Poss[1]=int(maxi)
		if mode=="a" or Poss[0]!=I or Poss[1]!=F:
			asca=ManagementJson("Helloword.json")
			lista=asca.intervaloIF(Poss[0],Poss[1])
			#cargando texto
			self.listbox1.delete(0,self.listbox1.size())
			
			for x in range(0,len(lista["serial"])):
				if lista["status"][x]=="Riesgo Medio":
					self.listbox1.insert(END,lista["serial"][x]+"        "+lista["status"][x]+"      "+lista["date"][x])
				else:
					self.listbox1.insert(END,lista["serial"][x]+"        "+lista["status"][x]+"         "+lista["date"][x])
	


	def buscMax(self):
		f=open("config.txt","r")
		f.seek(7)
		maxi=f.readline()
		f.close()
		return maxi

	def load1(self,listbox3,label1,label2,label3):
		asca=ManagementJson("Helloword.json")
		lista=asca.searchError(listbox3.get())
		try:
			if lista==0:
				label1.configure(text="No se encontro")
				label2.configure(text="No se encontro")
				label3.configure(text="No se encontro")
				return 0
		except Exception as e:
			raise e
		label1.configure(text=lista[0])
		label2.configure(text=lista[1])
		label3.configure(text=lista[2])