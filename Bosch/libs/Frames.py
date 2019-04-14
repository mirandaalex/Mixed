from tkinter import *
from PIL import Image, ImageTk


class SectionN(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master=master
		self.configure(height=200, width=940,background="#9A2EFE")
		self.place()


	def ImageIns(self,x=0,y=0,string="default.png"):
		if sys.platform.startswith('win32'):
			string="..\\image\\"+string
		elif sys.platform.startswith('linux'):
			string="../image/"+string

		load=Image.open(string)
		render=ImageTk.PhotoImage(load)
		img=Label(self,image=render)
		img.image=render
		img.place(x=x,y=y)

	def Posicion(self,x=0,y=0):
		self.place(x=x,y=y)