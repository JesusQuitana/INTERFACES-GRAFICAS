#CURSO BASICO DE PHYTON INTERFACES GRAFICAS

from tkinter import *

raiz=Tk()

frame=Frame(raiz, width=640, height=480)
frame.pack()

miNombre=StringVar()

texto=Label(frame, text='Nombre:', font=('Calibri','14'))
texto.grid(row=0,column=0, sticky='w', padx='5', pady='5')

cuadroTexto=Entry(frame, textvariable=miNombre)
cuadroTexto.grid(row=0,column=1, sticky='w', padx='5', pady='5')

texto2=Label(frame, text='Apellido:', font=('Calibri','14'))
texto2.grid(row=1, column=0, sticky='w', padx='5', pady='5')

cuadroTexto2=Entry(frame)
cuadroTexto2.grid(row=1, column=1, sticky='w', padx='5', pady='5')

texto3=Label(frame, text='Cedula:', font=('Calibri','14'))
texto3.grid(row=2, column=0, sticky='w', padx='5', pady='5')

cuadroTexto3=Entry(frame)
cuadroTexto3.grid(row=2, column=1, sticky='w', padx='5', pady='5')

texto4=Label(frame, text='Password:', font=('Calibri','14'))
texto4.grid(row=3, column=0, sticky='w', padx='5', pady='5')

cuadroTexto4=Entry(frame)
cuadroTexto4.grid(row=3, column=1, sticky='w', padx='5', pady='5')
cuadroTexto4.config(show='*')

#CUADRO DE TEXTOS LARGOS
texto5=Label(frame, text='-COMENTARIOS-', font=('Calibri','14'))
texto5.grid(row=4, column=0, sticky='n', padx='5', pady='5')

cuadroTexto5=Text(frame, width='30', height='15')
cuadroTexto5.grid(row='4',column='1', sticky='w', padx='5', pady='5')

#SCROLLBAR
scroll=Scrollbar(frame, command=cuadroTexto5.yview)
scroll.grid(row='4', column='2', sticky='nsew')
cuadroTexto5.config(yscrollcommand=scroll.set)

#BOTONES

def codigoBoton():
    miNombre.set('Jesus')

boton=Button(raiz, text='Enviar', command=codigoBoton)
boton.pack()



raiz.mainloop()