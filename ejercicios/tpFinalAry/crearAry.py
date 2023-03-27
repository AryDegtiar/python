import sqlite3

conn = sqlite3.connect("dbProductosAry.sqlite") # crea la base de datos
cursor = conn.cursor() # crea el cursor

try:
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, producto VARCHAR(100), precio FLOAT)") # crea la tabla productos
    conn.commit()
except sqlite3.OperationalError:
    print("Error al ejecutar la consulta")
else:
    productos = [
        ("Computadora", 10000),
        ("Disco Duro 1TB", 5000), 
        ("Teclado", 1000),
        ("SSD 1TB", 8000),
        ("Mouse", 500.8),
        ("Monitor 24", 15000)
    ]

    for producto, precio in productos:
        cursor.execute("INSERT INTO productos (producto, precio) VALUES (?,?)", (producto, precio)) # inserta los datos en la tabla productos

    conn.commit() 

    # # Testear la creacion
    # cursor.execute("SELECT * FROM productos")
    # productosEncontrados = cursor.fetchall()
    # print(productosEncontrados)

    conn.close() # cierra la conexion
