# ~ ENUNCIADO
# ~ La lista de productos que habíamos creado en el proyecto anterior ahora debe ser un diccionario,
# ~ en donde las claves serán nombres de los productos y los valores sus respectivos.

print("/*********************************/")
print("/       TP PROYECTO GUIA 5        /")
print("/       Autor: Ary Degtiar        /")
print("/          Version: 2.0           /")
print("/*********************************/\n")

productos = {}

# Se declara "intentosMaximos" que es la cantidad maxima para poner opciones del menu invalidas
intentosMaximos = 3

while True:
	print("Acciones del menu")	
	print("1 - Alta de producto")
	print("2 - Modificación de Precio")
	print("3 - Litado de Productos")
	print("4 - Salir\n")
	
	opcion = int(input("Ingrese el numero de la accion a realizar: "))

	if opcion == 1:
		nombre = input("Ingrese el nombre del producto: ")
		
		# Verifica si ya existia el producto  (asi no se modifica ya que no es la seccion)
		productoYaExistente = False
		for nomProducto in productos:
			if nombre == nomProducto:
				productoYaExistente = True	
		
		# Verifica si los parametros estan correctos y sea un nuevo producto
		if (not productoYaExistente):
			# El precio recien se pide ahora ya que si el nombre del prod ya existia no hace falta pedir el precio
			precio = float(input("Ingrese el precio del producto: "))
			if(precio > 0) and (nombre != ""):
				productos[nombre] = precio
				print("Producto guardado exitosamente \n")
			else:
				print("Nombre o precio del producto invalidos \n")
		else:
			print("El producto ingresado ya existe, intente de nuevo \n")
	
	elif opcion == 2:
		nomBusqueda = input("Ingrese el nombre del producto: ")
		
		# Verfica si existe el producto, de ser asi se le modifica el precio
		prodInexistente = True
		for nomProd in productos:
			if nomProd == nomBusqueda:
				prodInexistente = False
				
				print("El producto seleccionado es '" + nomProd + "' con el precio $" + str(productos[nomProd]))
				
				nuevoPrecio = float(input("Ingrese el nuevo precio del producto: "))
				# Verifico que el precio nuevo ingresado sea mayor a 0
				if nuevoPrecio > 0:		
					productos[nomProd] = nuevoPrecio
					print("Producto modificado exitosamente \n")
					# Sale del for para no seguir buscando el producto
					break
				else:
					print("El precio debe ser mayor que 0, intente de nuevo \n")
		
		if prodInexistente:
			print("No se encontro un producto con el nombre '" + nomBusqueda + "'\n")
	
	elif opcion == 3:
		print("----------------")
		print("Nombre    Precio")
		print("----------------")
		
		# Recorre y muestra un listado de productos (segun key y value)
		for nomProducto in productos:
			print(nomProducto, "    ",productos[nomProducto])
		
		print("---------------- \n")
	
	elif opcion == 4:
		print("Como diria Terminator: 'Hasta la vista baby' \n")
		# Finaliza el programa (cierra el bucle del menu)
		break
		
	else:
		# Accion invalida, si se llega al limite de intentos, cierra el programa
		intentosMaximos -= 1
		if intentosMaximos > 0:
			print("Seleccione una opcion valida, le quedan " + str(intentosMaximos) + " intentos \n")
		else:
			print("Accion invalida, se llego al limite de intentos \n")
			break
		
