import sqlite3

def buscarProductoXNombre(nombreProd):
    try:  
        # busca el producto en la tabla productos
        cursor.execute("SELECT * FROM productos WHERE producto = ?", (nombreProd,)) 
        return cursor.fetchall()
    except ValueError:
        print("Error, Debe ingresar un numero")

# Creo esta mostrar listado por que la uso en varios lugares
def mostrarListaProductos(listaProductos):
    print("-------------------------")
    print("ID    Producto    Precio")
    for prod in listaProductos:
        if prod[1]:
            print(prod[0], "'" +  str(prod[2]) + "'", "$" + str(prod[3])) # el str en nombreProd esta de mas, pero lo dejo por que me parece buena practica
    print("-------------------------")

def obtenerNumeroEntero(mensaje):
    try:
        numero = int(input(mensaje))
    except ValueError:
        print("Error, Debe ingresar un numero entero")
    else:
        return numero

def obtenerPrecioProducto():
    try:
        inputPrecio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Error, Debe ingresar el precio del producto en numeros (ej: 100.50)")
    else:
        return inputPrecio

def obtenerNombreProducto():
    try:
        inputNombre = input("Ingrese el nombre del producto: ")
    except ValueError:
        print("Error, Debe ingresar el nombre del producto")
    else:
        return inputNombre

def insertarProducto(nombreProd, precioProd):
    try:
        cursor.execute("INSERT INTO productos (activo, producto, precio) VALUES (?,?,?)", (True ,nombreProd, precioProd)) # inserta los datos en la tabla productos
        conn.commit() # guarda los cambios
        print("Producto agregado exitosamente")
    except sqlite3.OperationalError:
        print("Error al ejecutar la consulta")
 
### INICIO DEL PROGRAMA ###

# Conexion a Base de Datos
nombreDB = "dbProductosAry.sqlite"        
conn = sqlite3.connect(nombreDB) # conecta la base de datos
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
        nombre = obtenerNombreProducto()
        if nombre != "" or nombre != None:
            precio = obtenerPrecioProducto()
            # agregar producto a la lista de productos
            if precio > 0:
                insertarProducto(nombre, precio)
            else:
                print("El precio del producto debe ser mayor que 0")
            
    elif opcion == 2:
        print("Modificar de producto")
        nombre = obtenerNombreProducto()
        # busca el producto en la tabla productos
        productoEncontrado = buscarProductoXNombre(nombre)
        
        if productoEncontrado != "" or productoEncontrado != None:
            # si encuentra un solo producto
            if len(productoEncontrado) == 1:   
                productoEncontrado = productoEncontrado[0]
                
            # si encuentra mas de un producto con el mismo nombre
            elif len(productoEncontrado) > 1:
                print("Se encontraron varios productos con el mismo nombre")
                mostrarListaProductos(productoEncontrado)
                
                idProd = obtenerNumeroEntero("Ingrese el ID del producto a modificar: ")
              
                # verifica que el id ingresado sea valido ya que sino se podria ingresar tanto uno invalido por que no exista o partenezca a otro producto diferente
                idValido = False
                for prod in productoEncontrado:
                    if prod[0] == idProd:
                        idValido = True
                        productoEncontrado = prod
                        break
                    
                if idValido:
                    try:
                        cursor.execute("SELECT * FROM productos WHERE id = ?", (idProd,)) # busca el producto en la tabla productos
                        productoEncontrado = cursor.fetchone()
                    except sqlite3.OperationalError:
                        print("Error al ejecutar la consulta")
                else:
                    print("El ID ingresado no esta en la lista de productos encontrados")
            
            print("Producto encontrado: ", " ID: ",productoEncontrado[0], " Producto: ", productoEncontrado[2]," Precio: ", productoEncontrado[3])

            nuevoPrecio = obtenerPrecioProducto()

            if nuevoPrecio > 0:
                try:
                    cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevoPrecio, productoEncontrado[0])) # inserta los datos en la tabla productos
                    conn.commit() 
                    print("Producto modificado exitosamente")
                except sqlite3.OperationalError:
                    print("Error al ejecutar la consulta")
            else:
                print("El precio del producto debe ser mayor que 0")
        else:
            print("No existe un producto con ese nombre") 

    elif opcion == 3:
        print("Baja de producto")
        nombre = obtenerNombreProducto()
        # busca el producto en la tabla productos
        productoEncontrado = buscarProductoXNombre(nombre)
        
        if productoEncontrado != "" or productoEncontrado != None:
            # si encuentra un solo producto
            if len(productoEncontrado) == 1:   
                productoEncontrado = productoEncontrado[0]
                
            # si encuentra mas de un producto con el mismo nombre
            elif len(productoEncontrado) > 1:
                print("Se encontraron varios productos con el mismo nombre")
                mostrarListaProductos(productoEncontrado)
                
                idProd = obtenerNumeroEntero("Ingrese el ID del producto a modificar: ")
              
                # verifica que el id ingresado sea valido ya que sino se podria ingresar tanto uno invalido por que no exista o partenezca a otro producto diferente
                idValido = False
                for prod in productoEncontrado:
                    if prod[0] == idProd:
                        idValido = True
                        productoEncontrado = prod
                        break
                    
                if idValido:
                    try:
                        cursor.execute("SELECT * FROM productos WHERE id = ?", (idProd,)) # busca el producto en la tabla productos
                        productoEncontrado = cursor.fetchone()
                    except sqlite3.OperationalError:
                        print("Error al ejecutar la consulta")
                else:
                    print("El ID ingresado no esta en la lista de productos encontrados")

            try:
                cursor.execute("UPDATE productos SET activo = ? WHERE id = ?", (False, productoEncontrado[0])) # inserta los datos en la tabla productos
                conn.commit() 
            except sqlite3.OperationalError:
                print("Error al ejecutar la consulta")
            else:
                print("Producto eliminado: ", " ID: ",productoEncontrado[0], " Producto: ", productoEncontrado[2]," Precio: ", productoEncontrado[3])

        else:
            print("No existe un producto con ese nombre") 

    elif opcion == 4:
        print("Litado de Productos")
        
        try:
            cursor.execute("SELECT * FROM productos")
            dataProductos = cursor.fetchall()
        except sqlite3.OperationalError:
            print("Error al ejecutar la consulta")
        
        mostrarListaProductos(dataProductos)

    elif opcion == 5:
        conn.close() # cierra la conexion a la base de datos
        print("¡Hasta el infinito y más allá!")
        break