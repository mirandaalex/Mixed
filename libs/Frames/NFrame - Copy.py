from tkinter import *
from PIL import Image, ImageTk
	
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
	#si no le proporcionamos ningun dato a incial tendra por defecto True
	def __init__(self, master,inicial=True):
		Frame.__init__(self,master)
		self.master = master
		self.__list_label=[]
		self.__list_listbox=[]
		self.__list_scrollbar=[]
		self.__list_button=[]
		if inicial==True:
			self.init_window(master)

	#add imagenes dependiendo del tipo de sistema sobre el que opera el programa
	#Modifica las caracteristicas de la ventana principal
	def init_window(self,master):
		self.master.title("MAIN Window")
		if sys.platform.startswith('win32'):
			self.master.iconbitmap("image\\cod.ico")
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			self.master.iconbitmap("image/cod.ico")
		
		self.master.geometry("600x315")
		self.master.configure(bg="#D8D8D8")
		self.master.resizable(1,1)
		self.configure(height=300, width=10 ,background="#D8D8D8")
		self.pack(side=RIGHT,ipadx=0, ipady=0)
		

		if sys.platform.startswith('win32'):
			load=Image.open("image\\color.png")
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			load=Image.open("image/color.png")
		
		render=ImageTk.PhotoImage(load)
		img=Label(self,image=render)
		img.image=render
		img.pack()
		self.initUI()


	#add menu bar
	def initUI(self):	
		menubarra = Menu(self.master)
		fileMenu= Menu(menubarra,tearoff=0)
		busMenu= Menu(fileMenu,tearoff=0)
		busMenu.add_command(label="Buscar elemeto")
		busMenu.add_command(label="Mostrar todos los registros")
		fileMenu.add_cascade(label="Buscar",menu=busMenu)
		fileMenu.add_command(label="Ayuda")
		fileMenu.add_command(label="Exit", command=self.onExit)
		self.master.configure(menu=menubarra)
		menubarra.add_cascade(label="Opciones", menu=fileMenu)
		


	def onExit(self):

		self.quit()

	#Permite configurar un frame creado
	def ConfigureF(self,ax=600,ay=52,x=0,y=0,bg="#F9EFEF"):
		self.configure(height=ay, width=ax ,background=bg)
		self.place(x=x,y=y)

	#Crea un Label
	def addLabel(self,textvar="NONE",ax=4,ay=10,x=0,y=0):
		label=Label(self,height=ay, width=ax,background="#F9EFEF",text=textvar)
		label.place(x=x,y=y)
		self.__list_label.append(label)
		return label

	#Crea un TextBox
	def addTextBox(self,ax=600,ay=52,x=0,y=0,bg="#B4045F",final=True):
		if final==True:
			listbox=Listbox(self,height=ay, width=ax ,background=bg)
			listbox.pack(side=LEFT)	
			self.__list_listbox.append(listbox)
		else:
			scrolly=Scrollbar(self,orient=VERTICAL)
			
			listbox=Listbox(self,height=ay, width=ax ,background=bg,yscrollcommand=scrolly.set)
			listbox.pack(side=LEFT)
			scrolly.pack(side=LEFT,fill=Y)	
			
			self.__list_listbox.append(listbox)
			self.__list_scrollbar.append(scrolly)
			for x in self.__list_listbox:
				x.configure(yscrollcommand=scrolly.set)
			scrolly.configure(command=self.__yview)

	#metodo privado add scrollbar a los textbox
	def __yview(self, *args):
		for x in self.__list_listbox:
			x.yview(*args)
	
	#add texto en pantalla		
	def addText(self,index,text):
		for x in index:
			self.__list_listbox[x].insert(END,text)

	#add button
	def addButton(self,text="Hola mundo",command=0):
		nbutton=Button(self,text=text)
		nbutton.configure(height=2,width=16)
		nbutton.pack(padx=11,side=LEFT)
		self.__list_button.append(nbutton)
		if command==1:
			nbutton.configure(command=searchOne)
		elif command == 2:
			nbutton.configure(command=showAll)
			
		return nbutton
		
