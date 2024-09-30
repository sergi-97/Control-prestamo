from conexion import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Aplicacion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.crear_witgets()

    def crear_witgets(self):
        # Etiquetas
        frm_datos = ttk.Frame(self, padding = 10)
        frm_datos.grid(column=0, row=0, padx=10, pady=10, sticky="N")

        self.label_nombre = ttk.Label(frm_datos, text="Nombre")
        self.label_nombre.grid(column=0, row=0)

        self.label_direccion = ttk.Label(frm_datos, text="Dirección")
        self.label_direccion.grid(column=0, row=1)

        self.label_telefono = ttk.Label(frm_datos, text="Teléfono")
        self.label_telefono.grid(column=0, row=2)

        self.label_correo = ttk.Label(frm_datos, text="Correo")
        self.label_correo.grid(column=0, row=3)

        # Entradas
        self.entry_nombre = ttk.Entry(frm_datos)
        self.entry_nombre.grid(column=1, row=0, pady=5)

        self.entry_direccion = ttk.Entry(frm_datos)
        self.entry_direccion.grid(column=1, row=1, pady=5)

        self.entry_telefono = ttk.Entry(frm_datos)
        self.entry_telefono.grid(column=1, row=2, pady=5)

        self.entry_correo = ttk.Entry(frm_datos)
        self.entry_correo.grid(column=1, row=3, pady=5)

        # Botones en un frame separado
        self.frm_botones = ttk.Frame(self, padding=10)  # Cambio aquí
        self.frm_botones.grid(column=1, row=0, padx=10, pady=10, sticky="N")

        btn_nuevo = ttk.Button(self.frm_botones, text="Nuevo", command=self.limpiar_entry)
        btn_nuevo.grid(column=0, row=0, pady=5)

        btn_guardar = ttk.Button(self.frm_botones, text="Guardar", command=self.capturar_datos)
        btn_guardar.grid(column=0, row=1, pady=5)

        btn_salir = ttk.Button(self.frm_botones, text="Salir", command=self.cerrar_conexion)
        btn_salir.grid(column=0, row=2, pady=5)

        # Primer Frame para datos (Treeview)
        self.frm_treeview = ttk.Frame(self, padding=10)
        self.frm_treeview.grid(column=0, row=1, padx=10, pady=10,columnspan=2, sticky=N)

        # Crear el Treeview para mostrar los clientes
        self.lista_clientes = ["ID_client", "nombre", "direccion", "telf", "correo"]
        self.tree = ttk.Treeview(self.frm_treeview, columns=self.lista_clientes, show="headings")

        # Configurar las columnas
        for col in self.lista_clientes:
            self.tree.heading(col, text=col)
            
        self.tree.grid(column=0, row=0)

    # Función para guardar datos en la base de datos 
    def guardar_en_bd(self, nombre, direccion, telefono, correo):
        self.cursor = coneccion.cursor()
        self.cliente = [(nombre, direccion, telefono, correo)]

        # Insertamos datos a la tabla
        self.cursor.executemany("INSERT INTO Clientes VALUES (NULL,?,?,?,?)", self.cliente)
        coneccion.commit()
        
        messagebox.showinfo("Información", "Datos guardados Correctamente")

    def listar_clientes(self):
        # Obtener los datos de la tabla Clientes
        cursor = coneccion.cursor()
        cursor.execute("SELECT * FROM Clientes")
        clientes = cursor.fetchall()

        # Limpiar el Treeview antes de listar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos en el Treeview
        for cliente in clientes:
            self.tree.insert("", "end", values=cliente)
        
    # Función para capturar datos del formulario y guardarlos
    def capturar_datos(self):
        self.nombre = self.entry_nombre.get()
        self.direccion = self.entry_direccion.get()
        self.telefono = self.entry_telefono.get()
        self.correo = self.entry_correo.get()

        self.guardar_en_bd(self.nombre, self.direccion, self.telefono, self.correo)
        self.listar_clientes()

    # Limpiar los campos de entrada (entry)
    def limpiar_entry(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_nombre.focus_set()   # Coloca el cursor en el entry de nombre

    def cerrar_conexion(self):
        if coneccion:
            coneccion.close() #Cierra la conexion cuando cierra la aplicacion
        
        self.master.quit() #Cierra la ventana


# Crear la ventana principal
root = tk.Tk()
root.title("Formulario Clientes")
root.geometry("1050x500")

miApp = Aplicacion(master=root)
miApp.listar_clientes()
miApp.mainloop()






