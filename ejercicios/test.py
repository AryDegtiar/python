import sqlite3

conn = sqlite3.connect("dbProductosAry.sqlite") # crea la base de datos
cursor = conn.cursor() # crea el cursor
cursor.execute("SELECT * FROM productos")
productosEncontrados = cursor.fetchall()
print(productosEncontrados)
conn.close() # cierra la conexion