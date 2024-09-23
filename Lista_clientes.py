from conexion import *
from tkinter import ttk
import tkinter as tk
from tkinter import *

class miApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.crear_widgets()

    def crear_widgets(self):
        # Primer Frame para datos (Treeview)
        self.frm_datos = ttk.Frame(self, padding=10)
        self.frm_datos.grid(column=0, row=0, padx=10, pady=10, sticky=N)

        # Crear el Treeview para mostrar los clientes
        self.lista_clientes = ["ID_client", "nombre", "direccion", "telf", "correo"]
        self.tree = ttk.Treeview(self.frm_datos, columns=self.lista_clientes, show="headings")

        # Configurar las columnas
        for col in self.lista_clientes:
            self.tree.heading(col, text=col)
            self.tree.grid(column=0, row=0)

        # Segundo Frame para botones
        self.frm_botones = ttk.Frame(self, padding=10)
        self.frm_botones.grid(column=1, row=0)

        # Botón para buscar clientes
        self.btn_buscar = Button(self.frm_botones, text="Buscar", command=self.listar_clientes)
        self.btn_buscar.grid(column=1, row=1)

        # Botón para editar
        self.btn_editar = Button(self.frm_botones, text="Editar", command=self.editar_cliente)
        self.btn_editar.grid(column=1, row=2)

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

        coneccion.close()

    def editar_cliente(self):
        # Implementación para editar un cliente (esto se puede desarrollar más)
        seleccionado = self.tree.focus()
        if seleccionado:
            valores = self.tree.item(seleccionado, 'values')
            print(f"Editar cliente con ID: {valores[0]}")  # Aquí puedes desarrollar la lógica de edición
        else:
            print("No se ha seleccionado ningún cliente.")

# Crear la raíz de la aplicación
root = Tk()
root.title("Lista de Clientes")
ventana = miApp(master=root)
ventana.mainloop()
