from conexion import *
import tkinter as tk

class appMain(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.crear_witgets()
        self.grid()


#Creamos la ventana
root = tk.Tk()
root.title("Formulario Principal")
root.geometry("1920x1080")
root.mainloop()




        
