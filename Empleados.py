from conexion import coneccion
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class appEmleado(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master=master
        self.grid()
        self.crear_witgets()
    
    def crear_witgets(self):
        #Creamos el FRAME PARA DATOS
        self.frmDatos = tk.Frame(self, padx=10, pady= 10, bg="#F5F5DC")
        self.frmDatos.grid(column=0, row=0)
        #Creamos los labels
        self.lbl_nombre = Label(self.frmDatos, text="Nombre")
        self.lbl_nombre.grid(column=0, row=0)
        self.lbl_cargo = Label(self.frmDatos, text="Cargo", padx=10, pady=10)
        self.lbl_cargo.grid(column=0, row=1)
        #creamos las entradas(entrys)
        self.entry_nombre = Entry(self.frmDatos)
        self.entry_nombre.grid(column=1, row=0)
        self.entry_cargo = Entry(self.frmDatos)
        self.entry_cargo.grid(column=1, row=1)

        #Creamos el FRM PARA BOTONOES
        self.frm_botones= tk.Frame(self, padx=10, pady=10)
        self.frm_botones.grid(column=1, row=0)

        self.btn_nuevo = Button(self.frm_botones,text="Nuevo")
        self.btn_nuevo.grid(column=0, row=0)

        self.btn_guardar = Button(self.frm_botones, text="Guardar")
        self.btn_guardar.grid(column=0, row=1)

        self.btn_mostrar = Button(self.frm_botones, text="Mostrar",command=self.listar_empleados)
        self.btn_mostrar.grid(column=0, row=2)

        #CREAMOS EL FRAME DEL treeVIEW
        self.frm_treeview = tk.Frame(self, padx=10,pady=10)
        self.frm_treeview.grid(column=0, row=1, padx=10, pady=10)

        #Crear el TreeView para mostrar los clientes
        self.lista_empleados = ["ID_Empleados", "Nombre", "Cargo"]
        self.tree = ttk.Treeview(self.frm_treeview, columns= self.lista_empleados, show="headings" )

        #configurar las columnas
        for col in self.lista_empleados:
            self.tree.heading(col, text=col)
        
        self.tree.grid(column=0, row=0)

    def listar_empleados(self):
        #Obtener los datos de la tabla cliente
        cursor = coneccion.cursor()
        cursor.execute("SELECT * FROM Empleados")
        empleados = cursor.fetchall()

        #Limpiar el TreeView antes de listar
        for item in self.tree.get_children():
            self.tree.delete(item)

        #Insertar datos al TreeView
        for empleado in empleados:
            self.tree.insert("", "end", values=empleado)

    
root = tk.Tk()
root.title("Formulario Empleado")
root.geometry("1050x500")

MiAppEmp = appEmleado(master=root)

MiAppEmp.mainloop()




    
