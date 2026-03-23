"""Tarea 1 Progra Max Q.H"""

import tkinter as tk
import math as mt   #import super util (no hizo nada)
import pygame #Solo para audio

def Nombre():
    print("Matz")


ventana = tk.Tk()

ventana.title("Perfil")
ventana.geometry("500x500")
ventana.configure(
    background= 'aquamarine',
)

def cerrarVentana():
    print("cerrar esta ventana")
    ventana.destroy()

ventana.resizable(width= False, height= False)

canva1 = tk.Canvas(ventana, bg = 'Gray', width=120, height=129)
canva1.pack()


botonM = tk.Button(ventana, text = 'Cerrar la Ventana', bg = 'Red', command = lambda:cerrarVentana())
botonM.place(x = 250, y= 400)

boton1 = tk.Button(canva1, text = 'Perfil', bg = 'purple', command = lambda:Nombre())
boton1.place(x= 50, y= 100)




ventana.mainloop()