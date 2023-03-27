print("/*********************************/")
print("/       TP PROYECTO GUIA 4        /")
print("/       Autor: Ary Degtiar        /")
print("/          Version: 1.0           /")
print("/*********************************/")

programaCorriendo = True
menu = []
itemMenu = []

while(programaCorriendo):
	print()
	print("Acciones del menu")	
	print("1 - Alta de producto")
	print("2 - Modificación de Precio")
	print("3 - Litado de Productos")
	print("4 - Salir")
	print()
	
	# Se solicita al usuario que ingrese la acción que desea realizar
	opcionElegida = int(input("Ingrese el numero de la accion a realizar: "))

	# Si se selecciona la opción 1, se solicita al usuario que ingrese el nombre y precio del producto y se agrega a la lista de menú
	if opcionElegida == 1:
		nombre = input("Ingrese el nombre del producto: ")
		precio = float(input("Ingrese el precio del producto: "))
		if(precio > 0):
			itemMenu.append(nombre)
			itemMenu.append(precio)
			menu.append(itemMenu)
			print()
			print("Producto guardado exitosamente")
		else:
			print()
			print("El precio del producto debe ser mayor que 0")

	# Si se selecciona la opción 2, se solicita al usuario que ingrese la posición del producto a modificar y el nuevo precio
	# Luego se actualiza el precio del producto correspondiente en la lista de menú.
	elif opcionElegida == 2:
		index = int(input("Ingrese la posicion del producto: "))
		if (index >= 0) and (index <= len(menu)):
			itemMenu = menu[index - 1]
			print()
			print("El producto seleccionado es '" + str(itemMenu[0]) + "' con el precio $" + str(itemMenu[1]))
			precio = float(input("Ingrese el nuevo precio del producto: "))
			if(precio > 0):
				itemMenu = [itemMenu[0], precio]
				menu[index - 1] = itemMenu
				print()
				print("Producto modificado exitosamente")
			else:
				print()
				print("El precio del producto debe ser mayor que 0")
		else: 
			print()
			print("Posicion inexistente")

	# Si se selecciona la opción 3, se muestra en pantalla una lista de todos los productos en la lista de menú
	elif opcionElegida == 3:
		print()
		print("Nombre    Precio")
		for item in menu:
			print(item[0], "    ",item[1])

	# Si se selecciona la opción 4, se cambia la variable programaCorriendo a False, lo que detendrá el bucle while
	elif opcionElegida == 4:
		print()
		print("Como diria Terminator: 'Hasta la vista baby'")
		programaCorriendo = False

	# Si se selecciona una opción que no existe, se muestra un mensaje de error.
	else:
		print()
		print("Accion inexistente, seleccione una accion valida")

	# Se resetea la variable itemMenu para que esté vacía

	itemMenu = []

