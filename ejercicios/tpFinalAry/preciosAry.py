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
        else:
            try:
                precio = float(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Error, Debe ingresar un numero")
            
        # agregar producto a la lista de productos
        if precio > 0:
            try:
                cursor.execute("INSERT INTO productos (activo, producto, precio) VALUES (?,?)", (True ,nombre, precio)) # inserta los datos en la tabla productos
                conn.commit() 
                print("Producto agregado exitosamente")
            except sqlite3.OperationalError:
                print("Error al ejecutar la consulta")
        else:
            print("El precio del producto debe ser mayor que 0")
            
    elif opcion == 2:
        print("Modificar de producto")
        # obtener nombre y precio del producto
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cursor.execute("SELECT * FROM productos WHERE producto = ?", (nombre,)) # busca el producto en la tabla productos
            productoEncontrado  = cursor.fetchall()
        except ValueError:
            print("Error, Debe ingresar un numero")
        else:
            if len(productoEncontrado ) == 0:
                print("El producto no existe")
            elif len(productoEncontrado ) > 1:
                print("Se encontraron varios productos con el mismo nombre")
                print("ID    Producto    Precio")
                for prod in productoEncontrado :
                    print(producto[0], "'" +  str(producto[2]) + "'", "$" + str(producto[3])) 
                
                try:
                    idProd = int(input("Ingrese el ID del producto a modificar: "))
                except ValueError:
                    print("Error, Debe ingresar un numero")
                
                try:
                    cursor.execute("SELECT * FROM productos WHERE id = ?", (idProd,)) # busca el producto en la tabla productos
                    productoEncontrado = cursor.fetchone()
                except sqlite3.OperationalError:
                    print("Error al ejecutar la consulta")

            productoEncontrado = productoEncontrado[0]
            print("Producto encontrado: ", " ID: ",productoEncontrado[0], " Producto: ", productoEncontrado[2]," Precio: ", productoEncontrado[3])

            try:
                nuevoPrecio = float(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Error, Debe ingresar un numero")

            if nuevoPrecio > 0:
                try:
                    cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevoPrecio, productoEncontrado[0])) # inserta los datos en la tabla productos
                    conn.commit() 
                    print("Producto modificado exitosamente")
                except sqlite3.OperationalError:
                    print("Error al ejecutar la consulta")
            else:
                print("El precio del producto debe ser mayor que 0")

    elif opcion == 3:
        print("Baja de producto")
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cursor.execute("SELECT * FROM productos WHERE producto = ?", (nombre,)) # busca el producto en la tabla productos
            productoEncontrado  = cursor.fetchall()
            print(productoEncontrado)
        except ValueError:
            print("Error, Debe ingresar un numero")
        else:
            if len(productoEncontrado ) == 0:
                print("El producto no existe")
            elif len(productoEncontrado ) > 1:
                print("Se encontraron varios productos con el mismo nombre")
                print("ID    Producto    Precio")
                for prod in productoEncontrado :
                    print(prod[0], "'" +  str(prod[2]) + "'", "$" + str(prod[3])) 
                
                try:
                    idProd = int(input("Ingrese el ID del producto a eliminar: "))
                except ValueError:
                    print("Error, Debe ingresar un numero")

                try:
                    cursor.execute("SELECT * FROM productos WHERE id = ?", (idProd,)) # busca el producto en la tabla productos
                    productoEncontrado = cursor.fetchone()
                except sqlite3.OperationalError:
                    print("Error al ejecutar la consulta")
            
            productoEncontrado = productoEncontrado[0]

            cursor.execute("UPDATE productos SET activo = ? WHERE id = ?", (False, productoEncontrado[0])) # inserta los datos en la tabla productos
            print("Producto encontrado: ", " ID: ",productoEncontrado[0], " Producto: ", productoEncontrado[2]," Precio: ", productoEncontrado[3])

    elif opcion == 4:
        print("Litado de Productos")
        cursor.execute("SELECT * FROM productos")
        dataProductos = cursor.fetchall()
        print("-------------------------")
        print("ID    Producto    Precio")
        for producto in dataProductos:
            if producto[1]:
                print(producto[0], "'" +  str(producto[2]) + "'", "$" + str(producto[3])) # el str en nombreProd esta de mas, pero lo dejo por que me parece buena practica
        print("-------------------------")

    elif opcion == 5:
        conn.close() # cierra la conexion
        print("¡Hasta el infinito y más allá!")
        break