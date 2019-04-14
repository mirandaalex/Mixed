from tkinter import *
from PIL import Image, ImageTk



class Window(Frame):
	"""docstring for Frame"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master=master
		self.init_window(master)

	def init_window(self,master):
		self.master.title("MAIN Window")
		
		if sys.platform.startswith('win32'):
			self.master.iconbitmap("..\\image\\favicon.ico")
		elif sys.platform.startswith('linux'):
			self.master.iconbitmap("../image/favicon.ico")
		
		self.master.geometry("1000x600")
		self.master.configure(bg="#F9EFEF")
		self.master.resizable(1,1)
		self.place(x=950,y=0)
		self.configure(height=600, width=50 ,background="#0000FF")

		if sys.platform.startswith('win32'):
			load=Image.open("..\\image\\boschImage.png")
		elif sys.platform.startswith('linux'):
			load=Image.open("../image/boschImage.png")
		
		render=ImageTk.PhotoImage(load)
		img=Label(self,image=render)
		img.image=render
		img.pack()

