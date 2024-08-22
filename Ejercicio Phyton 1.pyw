#CURSO BASICO DE PHYTON INTERFACES GRAFICAS

from tkinter import *

raiz=Tk()

raiz.title('Primera Ventana')
raiz.resizable(1,1)
raiz.geometry('640x480')
raiz.config(bg='darkblue')

frame=Frame()

frame.pack(side='left')
frame.config(bg='red')
frame.config(width='320', height='240')






raiz.mainloop()