from conexion import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#Funcion para guardar datos en la base de datos 
def guardar_en_bd(nombre, direccion, telefono, correo):
    cursor = coneccion.cursor()
    cliente =[(nombre, direccion, telefono, correo)]

    #insertamos datos a la tabla
    cursor.executemany("INSERT INTO Clientes VALUES (NULL,?,?,?,?)", cliente)
    coneccion.commit()
    coneccion.close()
    messagebox.showinfo("Informaciion", "Datos guardados Correctamente")

#Funcion para capturar datos del formulario y guardarlos
def capturar_datos():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    
    guardar_en_bd(nombre, direccion, telefono, correo)
    

#creamos la ventana principal junto con los widgets
root= Tk()
root.title("REGISTRO DE CLIENTES")



frm = ttk.Frame(root, padding=10)
frm.grid()

label_nombre = ttk.Label(frm, text="Nombre")
label_nombre.grid(column=0, row=0)
label_direccion = ttk.Label(frm, text="Dirección")
label_direccion.grid(column=0, row=1)
label_telefono = ttk.Label(frm, text="telefono")
label_telefono.grid(column=0, row=2)
label_correo = ttk.Label(frm, text="Correo")
label_correo.grid(column=0, row=3)

entry_nombre = ttk.Entry(frm)
entry_nombre.grid(column=1, row=0)
entry_direccion = ttk.Entry(frm)
entry_direccion.grid(column=1, row=1)
entry_telefono = ttk.Entry(frm)
entry_telefono.grid(column=1, row=2)
entry_correo = ttk.Entry(frm)
entry_correo.grid(column=1, row=3)

#boton guardar los datos

btn_nuevo= ttk.Button(frm, text="nuevo")
btn_nuevo.grid(column=0, row=4)

btn_guardar = ttk.Button(frm,text="Guardar", command=capturar_datos)
btn_guardar.grid(column=1, row=4)

btn_editar = ttk.Button(frm, text="Editar")
btn_editar.grid(column=2, row=4)

btn_eliminar = ttk.Button(frm, text="Eliminar")
btn_eliminar.grid(column=3,row=4)

root.mainloop()





