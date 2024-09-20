from conexion import *
from tkinter import ttk
import tkinter as tk
from tkinter import *


def listar_clientes():
    #obtener los datos de la tabla cliente
    cursor = coneccion.cursor()
    cursor.execute("SELECT * FROM Clientes")
    cliente = cursor.fetchall()

    #Limpiar el Treeview antes de listar
    for i in tree.get_children():
        tree.delete(i)
    
    #Insertar datos el Treeview
    for clien in cliente:
        tree.insert("", "end", values=clien)
    
    coneccion.close()

#creamos la raiz
root = Tk()
root.title("LISTA DE EMPLEADOS")

frm = ttk.Frame(root, padding=10)
#frm.grid()
frm.pack()

#CREAR EL Treeview para mostrar los empleados
lista_clientes = ["ID_client", "nombre", "direccion", "telf", "correo"]
tree = ttk.Treeview(root, columns=lista_clientes, show="headings")

#Configurar las columnas
for col in lista_clientes:
    tree.heading(col, text=col)

#tree.grid(column=0, row=0)
tree.pack()

#boton para listar empleados
btn_buscar = Button(root, text="buscar")
btn_buscar.pack()
#btn_buscar.grid(column=0, row=1)

#Boton editar
btn_editar = Button(root, text="Editar")
btn_editar.pack()
#btn_editar.grid(column=1, row=2)


listar_clientes()





root.mainloop()