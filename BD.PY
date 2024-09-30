from conexion import *


miCursor = coneccion.cursor()


miCursor.execute('''CREATE TABLE Clientes(
    ID_cliente INTEGER PRIMARY KEY AUTOINCREMENT, 
    Nombre TEXT, 
    Dirección TEXT, 
    Telefono TEXT, 
    Correo TEXT)
    ''')

clientes = [
    
            ("Sergio Kayap", "Jr. las delicias N°104", "985623589", "cristhiankayapgmail.com"),
            ("Samuel Camacho", "Jr. la Merced N°104", "985623580", "camacho@gmail.com"),
            ("Bastian Fernandez", "Jr. la Merced N°104", "985623580", "basti@gmail.com"),
            ("Nora Tiwi", "Jr. Chuchug N°104", "985623580", "nora@gmail.com")
            ]
miCursor.executemany("INSERT INTO Clientes VALUES (NULL,?,?,?,?)",clientes)   


miCursor.execute('''CREATE TABLE Empleados(
    ID_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Cargo TEXT)
    
    ''')

empleados = [
    ('Yamilet Lozano', 'vendedora'),
    ('Walter Cieza', 'Responsable Ventas')
    ]

miCursor.executemany("INSERT INTO Empleados VALUES (NULL, ?,?)", empleados)



miCursor.execute('''CREATE TABLE Prestamos(
                     ID_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
                     Monto INTEGER,
                     Tasa_interes INTEGER,
                     Plazo INTEGER,
                     Fech_inicio TEXT,
                     Fech_fin TEXT,
                     ID_cliente INTEGER, 
                     ID_empleado INTEGER,
                     FOREIGN KEY (ID_cliente) REFERENCES Clientes(ID_cliente) ON DELETE CASCADE,
                     FOREIGN KEY (ID_empleado) REFERENCES Empleados(ID_empleado) ON DELETE CASCADE
                     )
                 ''')


prestamo = [(2000, 10, 3, '19/9/2024', '19/12/2024', 1, 2),
            (4000, 10, 4, '19/9/2024', '19/1/2025', 2, 2),
            (1000, 10, 2, '19/9/2024', '19/11/2024', 1, 2)
            ]

miCursor.executemany("INSERT INTO Prestamos VALUES (NULL, ?,  ?, ?, ?, ?, ?, ?)", prestamo)



miCursor.execute('''
                 CREATE TABLE Pagos(
                     ID_pago INTEGER PRIMARY KEY AUTOINCREMENT,
                     Monto_pago INTEGER,
                     Fech_pago TEXT,
                     ID_prestamo INTEGER,
                     FOREIGN KEY (ID_prestamo) REFERENCES Prestamos (ID_prestamo) ON DELETE CASCADE             
                                      
                     )
                 
                 ''')


pago = [
    (240, '19/10/2024',1 ),
    (550, '19/10/2024',2 )
]


coneccion.executemany("INSERT INTO Pagos VALUES (NULL, ?, ?, ?)", pago)

coneccion.commit()

coneccion.close()
