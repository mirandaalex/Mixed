from MainRoot import *
from Frames import *
from tkinter import *




root = Tk()
BoschImageF=Window(root)
PlaneA=SectionN(root)
PlaneA.Posicion(x=5,y=20)
PlaneA.ImageIns(650,0,"plot.png")
PlaneB=SectionN(root)
PlaneB.Posicion(x=5,y=240)
PlaneBot=SectionN(root)
PlaneBot.Posicion(x=5,y=460)
PlaneBot.configure(height=130, width=940)
root.mainloop()

print("Hola Mundo")