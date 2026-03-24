"""Tarea 1 Progra Max Q.H"""

import tkinter as tk
import math as mt   #import super util (no hizo nada)
import pygame #Solo para audio

def Nombre():
    print("Matz")

def abre_funcion():
    Ventana2 = tk.Toplevel(ventana)
    Ventana2.title("Funcion pares")
    Ventana2.geometry("500x500")
    Ventana2.configure(
        background= 'beige',
    )
    Vuelve = tk.Button(Ventana2, text = 'Volver a la Ventana Principal', bg = 'Red', fg = 'White', command = lambda:Ventana2.destroy())
    Vuelve.place(x = 300, y= 400)


    Ventana2.mainloop()

def abre_animacion():
    Ventana3 = tk.Toplevel(ventana)
    Ventana3.title("Animacion esferas")
    Ventana3.geometry("600x600")
    Ventana3.configure(
        background= 'white',
    )
    canva_e = tk.Canvas(Ventana3, bg = 'black', width=500, height=500)
    canva_e.pack()
    bola = canva_e.create_oval(50, 50, 100, 100, fill='red')
    origen = tk.Button(Ventana3, text = 'Volver a la Ventana Principal', bg = 'Red', fg = 'White', command = lambda:Ventana3.destroy())
    origen.place(x = 300, y= 590)
    Ventana3.mainloop()


# Falta bloquear el tamaño de las ventanas acuérdese de hacerlo mae 


ventana = tk.Tk()

ventana.title("Perfil")
ventana.geometry("500x500")
ventana.configure(
    background= 'gray',
)

def cerrarVentana():
    print("cerrar esta ventana")
    ventana.destroy()

ventana.resizable(width= False, height= False)

canva1 = tk.Canvas(ventana, bg = 'pink', width=250, height=250)
canva1.pack()

tk.Label(canva1, text = 'Max Andrés Quirós Hernández', background= 'Blue', foreground= 'Black', font = ('Arial', 12)).place(x= 25, y= 15)



botonM = tk.Button(ventana, text = 'Cerrar la Ventana', bg = 'Red', command = lambda:cerrarVentana())
botonM.place(x = 300, y= 400)

boton1 = tk.Button(canva1, text = 'Perfil', bg = 'purple', command = lambda:Nombre())
boton1.place(x= 50, y= 100)

boton2 = tk.Button(ventana, text = 'Funcion Pares', bg = 'cyan', command = lambda:abre_funcion())
boton2.place(x= 50, y= 400)

boton3 = tk.Button(ventana, text = 'Animacion Esferas', bg = 'cyan', command = lambda:abre_animacion())
boton3.place(x= 165, y= 400)


ventana.mainloop()

