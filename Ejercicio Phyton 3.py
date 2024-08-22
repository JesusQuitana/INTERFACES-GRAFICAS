#VALIDAR DATOS DE ENTRADA

from tkinter import *

def ventana1():
    
    #----------------FUNCIONES Y VARIABLES-------------
    
    def validarNumero(valores):
        if valores.isdigit():
            print('ES UN NUMERO')
            return True
        else:
            print('NO ES UN NUMERO')
            return False
            
    def validarLongitud(valores):
        if len(valores)<=5:
            print('ESCRIBIR')
            return True
        else:
            print('MAXIMO PERMITIDO')
            return False
            
    def validarFocus(focus):
        if focus.islower():
            print('FOCUS OFF')
            return True
        else:
            print('FOCUS ON')
            return False
    
    #----------------FUNCIONES Y VARIABLES-------------
    
    #-----------------ELEMENTOS------------------------
    ventana1=Tk()
    ventana1.config()
    ventana1.resizable(0, 0)

    #----------------FUNCIONES Y VARIABLES REGISTRADAS----------------------------
    
    validarNum=ventana1.register(validarNumero)
    
    validarLong=ventana1.register(validarLongitud)
    
    validarFoc=ventana1.register(validarFocus)
    
    #----------------FUNCIONES Y VARIABLES REGISTRADAS----------------------------
    
    frame=Frame(width=300, height=300, padx=10, pady=10)
    frame.pack()
    
    titulo=Label(frame, text='DATOS DE ENTRADA')
    titulo.grid(column=0, row=0, columnspan=2)
    
    titulo1=Label(frame, text='Numeros')
    titulo1.grid(column=0, row=1, pady=7)
    datos1=Entry(frame, validate='key', validatecommand=(validarNum, '%P'))
    datos1.grid(column=1, row=1, pady=7)
    
    titulo2=Label(frame, text='Maximo')
    titulo2.grid(column=0, row=2, pady=7)    
    datos2=Entry(frame, validate='key', validatecommand=(validarLong, '%P'))
    datos2.grid(column=1, row=2, pady=7)
    
    titulo3=Label(frame, text='Focus')
    titulo3.grid(column=0, row=3, pady=7)    
    datos3=Entry(frame, validate='focusin', validatecommand=(validarFoc, '%P'))
    datos3.grid(column=1, row=3, pady=7)
    
    enviar=Button(frame, text='Enviar')
    enviar.grid(column=0, row=4, columnspan=2)

    ventana1.mainloop()
    #-----------------ELEMENTOS------------------------

ventana1()