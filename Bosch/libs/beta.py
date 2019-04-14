from tkinter import *
from PIL import Image, ImageTk
import numpy
import cv2
root = Tk()
root.geometry("1000x600")

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



BoschImageF=Window(root)
PlaneA=SectionN(root)
PlaneA.place(x=5,y=20)
PlaneA.ImageIns(650,0,"plot.png")
PlaneB=SectionN(root)
PlaneB.place(x=5,y=240)
PlaneBot=SectionN(root)
PlaneBot.place(x=5,y=460)
PlaneBot.configure(height=130, width=940)
root.mainloop()

