#CURSO BASICO DE PHYTON // PRACTICA DE CALCULADORA

from tkinter import *

raiz=Tk()

#FUNCIONES

def b9():
    b9.set(9)

#PANTALLA DE VISTA

pantalla=Frame(raiz, width='280',height='150')
pantalla.config(bg='grey', padx='5',pady='5')
pantalla.pack()

pantallaV=Text(pantalla, font=('Euphemia'), width='24', height='10')
pantallaV.grid(sticky='n', row='0', column='0')

scroll=Scrollbar(pantalla, command=pantallaV.yview)
scroll.grid(sticky='nsew', row='0', column='1')
pantallaV.config(yscrollcommand=scroll.set)

#PANTALLA DE BOTONES

botones=Frame(raiz, width='280', height='240')
botones.config(bg='grey', padx='5',pady='5')
botones.pack()

b9=Button(botones, text='9')
b9.grid(row='1',column='0')
b9.config(width='7', height='4')
b8=Button(botones, text='8')
b8.grid(row='1',column='1')
b8.config(width='7', height='4')
b7=Button(botones, text='7')
b7.grid(row='1',column='2')
b7.config(width='7', height='4')
b6=Button(botones, text='6')
b6.grid(row='2',column='0')
b6.config(width='7', height='4')
b5=Button(botones, text='5')
b5.grid(row='2',column='1')
b5.config(width='7', height='4')
b4=Button(botones, text='4')
b4.grid(row='2',column='2')
b4.config(width='7', height='4')
b3=Button(botones, text='3')
b3.grid(row='3',column='0')
b3.config(width='7', height='4')
b2=Button(botones, text='2')
b2.grid(row='3',column='1')
b2.config(width='7', height='4')
b1=Button(botones, text='1')
b1.grid(row='3',column='2')
b1.config(width='7', height='4')

bigual=Button(botones, text='=')
bigual.grid(row='3',column='3')
bigual.config(width='7', height='4')
bsuma=Button(botones, text='+')
bsuma.grid(row='2',column='3')
bsuma.config(width='7', height='4')
bresta=Button(botones, text='-')
bresta.grid(row='1',column='3')
bresta.config(width='7', height='4')
bmulti=Button(botones, text='x')
bmulti.grid(row='0',column='2')
bmulti.config(width='7', height='4')
bdivi=Button(botones, text='/')
bdivi.grid(row='0',column='1')
bdivi.config(width='7', height='4')


raiz.mainloop()