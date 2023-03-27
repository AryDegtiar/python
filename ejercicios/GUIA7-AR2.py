# AR2- Dado un Archivo separado con comas (.csv) con los siguientes campos: numDeProd,
# Producto, Precio
# Ejemplo:
# 1, Computadora, 10000
# 2, Disco Duro 1TB, 5000
# 3, Teclado, 1000
# Generar las siguientes funcionalidades:
# 1- Cargar el archivo en una matriz
# 2- Generar las funciones de Alta, Baja y Modificación de los campos (ABM)
# 3- Generar un Listado de los productos
# 4- Al salir volcar la matriz modificada en el archivo
# 5- Agregar verificaciones a los campos

nombreArchivo = "productos.csv"

productos = []
archivo = open(nombreArchivo, "r")
for linea in archivo:
    productos.append(linea.split(","))
archivo.close()

ultimoID = int(productos[-1][0])

while True:
    print()
    print("Acciones del menu")	
    print("1 - Alta de producto")
    print("2 - Modificar de producto")
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
            productos.append([str(ultimoID + 1), " " + nombre, " " + str(precio) + "\n"])
            ultimoID += 1
            print("Producto agregado exitosamente")
        else:
            print("El precio del producto debe ser mayor que 0")
            
    elif opcion == 2:
        print("Modificar de producto")
        # obtener id del producto
        try:
            id = int(input("Ingrese id del producto: "))
        except ValueError:
            print("Error invalida, Debe ingresar un número")
            
        print("El producto seleccionado es '" + str(productos[id - 1][1]) + "' con el precio $" + str(productos[id - 1][2]))
        
        # obtener nuevo precio del producto
        try:
            newPrecio = float(input("Ingrese el nuevo precio: "))
        except ValueError:
            print("Error, Debe ingresar un numero")
        
        # modificar precio del producto
        if newPrecio > 0:
            productos[id - 1][2] = " " + str(newPrecio) + "\n"
            print("Producto modificado exitosamente")
        else:
            print("El precio del producto debe ser mayor que 0")
            
    elif opcion == 3:
        print("Baja de producto")
        try:
            id = int(input("Ingrese id del producto: "))
        except ValueError:
            print("Error invalida, Debe ingresar un número")
        try:
            # fijarse que pop retorna el elemento elminado, se podria hacer con "del" y solo lo eliminaba
            productos.pop(id - 1)
        except IndexError:
            print("Error, El id ingresado no existe")
        else:
            print("Producto eliminado exitosamente")
            
    elif opcion == 4:
        print("Litado de Productos")
        print("Id, Nombre, Precio")
        for producto in productos:
            print(producto[0], ",",producto[1], ",",producto[2])
            
    elif opcion == 5:
        print("Bye Bye")
        archivo = open(nombreArchivo, "w")
        for producto in productos:
            archivo.write(producto[0] + "," + producto[1] + "," + producto[2])
        archivo.close()
        break