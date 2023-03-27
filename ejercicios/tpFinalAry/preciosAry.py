import sqlite3

conn = sqlite3.connect("dbProductosAry.sqlite") # crea la base de datos
cursor = conn.cursor() # crea el cursor

while True:
    print()
    print("Acciones del menu")	
    print("1 - Alta de producto")
    print("2 - Modificar el precio del producto")
    print("3 - Baja de producto")
    print("4 - Litado de Productos")
    print("5 - Salir")
    print()
    
    try:
        opcion = int(input("Ingrese el numero de la accion a realizar: "))
    except ValueError:
        print("Opcion invalida, Debe ingresar un número")
        
    if opcion == 1:
        print("Alta de producto")
                # obtener nombre y precio del producto
        try:
            nombre = input("Ingrese el nombre del producto: ")
        except ValueError:
            print("Error, Debe ingresar un numero")    
        try:
            precio = float(input("Ingrese el nuevo precio: "))
        except ValueError:
            print("Error, Debe ingresar un numero")
            
        # agregar producto a la lista de productos
        if precio > 0:
            try:
                cursor.execute("INSERT INTO productos (producto, precio) VALUES (?,?)", (nombre, precio)) # inserta los datos en la tabla productos
                conn.commit() 
                print("Producto agregado exitosamente")
            except sqlite3.OperationalError:
                print("Error al ejecutar la consulta")
        else:
            print("El precio del producto debe ser mayor que 0")
            
    elif opcion == 2:
        print("Modificar de producto")
        
    elif opcion == 3:
        print("Baja de producto")
        
    elif opcion == 4:
        print("Litado de Productos")
        cursor.execute("SELECT * FROM productos")
        dataProductos = cursor.fetchall()
        print("-------------------------")
        print("ID    Producto    Precio")
        for producto in dataProductos:
            print(producto[0], "'" +  str(producto[1]) + "'", "$" + str(producto[2])) # el str en nombreProd esta de mas, pero lo dejo por que me parece buena practica
        print("-------------------------")
    elif opcion == 5:
        conn.close() # cierra la conexion
        print("¡Hasta el infinito y más allá!")
        break