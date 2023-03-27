# ---  INICIO FUNCIONES  ---
def mostrarMenu():
	print("Acciones del menu")	
	print("1 - Alta de producto")
	print("2 - Modificación de Precio")
	print("3 - Litado de Productos")
	print("4 - Salir\n")

def elementoExistente(nombreBuscado, diccionario):
	elementoYaExistente = False
	for nomElemento in diccionario:
		if nombreBuscado == nomElemento:
			elementoYaExistente = True	
			# sale del for para no seguir recorriendo
			break
	return elementoYaExistente

def nombreValido(nombre):
    if nombre != "" and type(nombre) == str:
        return True
    else:
        return False

def precioValido(precio):
	if (precio > 0) and (type(precio) == float):
		return True
	else:
		return False

def guardarElemento(key, value, diccionario):
	diccionario[key] = value

def altaNuevoProducto():
	nombre = input("Ingrese el nombre del producto: ")
	# Verifica si los parametros estan correctos
	if not nombreValido(nombre):	
		print("Nombre del producto invalido \n")
		# sale de la funcion
		return 0
	# Verifica si ya existia el producto  (asi no se modifica ya que no es la seccion)
	# Podria haber hecho que la funcion acceda al diccionario en vez de por parametro por la variable global
	# sin embargo, elegi mandarle por parametro el diccionario ya que la funcion es mas generica y es mas funcional a futuro
	if (not elementoExistente(nombre, productos)):
		# El precio recien se pide ahora ya que si el nombre del prod ya existia no hace falta pedir el precio
		precio = float(input("Ingrese el precio del producto: "))
		if precioValido(precio):
			# mismo de antes, pase como parametro productos por que elegi que sea mas generica la funcion, podria usar el diccionario global
			# ~ productos = guardarElemento(nombre, precio, productos)
			guardarElemento(nombre, precio, productos)
			print("Producto guardado exitosamente \n")
		else:
			print("Precio del producto invalido \n")
	else:
		print("El producto ingresado ya existe, intente de nuevo \n")

#	ESTA FUNCION ESTA COMENTADA POR QUE ES CASI LA MISMA FUNCION DE ARRIBA PERO PONIENDO UN IF ELSE, EN VEZ DEL RETURN 
# ~ def altaNuevoProducto():
	# ~ nombre = input("Ingrese el nombre del producto: ")
	# ~ # Verifica si los parametros estan correctos
	# ~ if nombreValido(nombre):	
		# ~ # Verifica si ya existia el producto  (asi no se modifica ya que no es la seccion)
		# ~ # Podria haber hecho que la funcion acceda al diccionario en vez de por parametro por la variable global
		# ~ # sin embargo, elegi mandarle por parametro el diccionario ya que la funcion es mas generica y es mas funcional a futuro
		# ~ if (not elementoExistente(nombre, productos)):
			# ~ # El precio recien se pide ahora ya que si el nombre del prod ya existia no hace falta pedir el precio
			# ~ precio = float(input("Ingrese el precio del producto: "))
			# ~ if precioValido(precio):
				# ~ # mismo de antes, pase como parametro productos por que elegi que sea mas generica la funcion, podria usar el diccionario global
				# ~ guardarElemento(nombre, precio, productos)
				# ~ print("Producto guardado exitosamente \n")
			# ~ else:
				# ~ print("Precio del producto invalido \n")
		# ~ else:
			# ~ print("El producto ingresado ya existe, intente de nuevo \n")
	# ~ else:
		# ~ print("Nombre del producto invalido \n")

def modificarPrecioProducto(productos):
	nomBusqueda = input("Ingrese el nombre del producto: ")	
	# Verfica si existe el producto, de ser asi se le modifica el precio
	if elementoExistente(nomBusqueda, productos):
		print("El producto seleccionado es '" + nomBusqueda + "' con el precio $" + str(productos[nomBusqueda]))
		nuevoPrecio = float(input("Ingrese el nuevo precio del producto: "))
		# Verifico que el precio nuevo ingresado sea mayor a 0
		if precioValido(nuevoPrecio):		
			guardarElemento(nomBusqueda, nuevoPrecio, productos)
			print("Producto modificado exitosamente \n")
		else:
			print("El precio debe ser mayor que 0, intente de nuevo \n")
	else:
		print("No se encontro un producto con el nombre '" + nomBusqueda + "'\n")

def mostrarDiccionario(diccionario):
	for nomElemento in diccionario:
		print(nomElemento, "    ",diccionario[nomElemento])	

def mostrarListado():
	print("----------------")
	print("Nombre    Precio")
	print("----------------")
	# Recorre y muestra un listado de productos (segun key y value)
	mostrarDiccionario(productos)
	print("---------------- \n")
# ---   FIN FUNCIONES   ---

# ---  VARIABLES GLOBALES ---
productos = {}

# *****************************************
# ***** I N I C I O   P R O G R A M A *****
# *****************************************

print("/*********************************/")
print("/       TP PROYECTO GUIA 6        /")
print("/       Autor: Ary Degtiar        /")
print("/          Version: 3.0           /")
print("/*********************************/\n")

while True:
	
	mostrarMenu()
	
	opcion = int(input("Ingrese el numero de la accion a realizar: "))

	if opcion == 1:
		# da el alta de producto, esta funcion modifica las variables globales ya que es una funcion espesifica limitada al programa
		altaNuevoProducto()
	
	elif opcion == 2:
		# mismo comentario que la funcion "altaNuevoProducto()"
		modificarPrecioProducto(productos)
	
	elif opcion == 3:
		mostrarListado()
		
	elif opcion == 4:
		print("Como diria Terminator: 'Hasta la vista baby' \n")
		# Finaliza el programa (cierra el bucle del menu)
		break
		
	else:
		print("Accion invalida, intente de nuevo \n")
		
