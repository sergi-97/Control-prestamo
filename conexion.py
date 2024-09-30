import sqlite3

coneccion = sqlite3.connect("control_prestamos.db")
coneccion.execute("PRAGMA foreign_keys = ON")

