# GUIA 7
#eje e1 manejo de errores

def buscarEmpXLegajo(legajo):
	try:
		try:
			segundoNombre = empleados[legajo]["segundo"]
		except:
			segundoNombre = "*****"
		return {"nombre":empleados[legajo]["nombre"], "segundo":segundoNombre, "apellido":empleados[legajo]["apellido"]}
	except:
		raise NotFoundError("No existe el legajo ingresado")

def buscarEmpsXApellido(apellido):
	listEmp = []
	for legajo in empleados:
		if empleados[legajo]["apellido"] == apellido:
			listEmp.append(buscarEmpXLegajo(legajo))
	if listEmp == []:
		raise NotFoundError("No existe nadie con el apellido ingresado")
	return listEmp

def contEmpSegundoNombre():
	cant = 0
	for legajo in empleados:
		emp = buscarEmpXLegajo(legajo)
		if emp["segundo"] != "*****":
			cant += 1
	return cant

class NotFoundError(Exception):
	pass

empleados={
    "100":{
        "nombre":"Juan",
        "segundo":"Carlos",
		"apellido":"Nuñez"
  	},
    "201":{
        "nombre":"Elvira",
		"apellido":"Goldstein"
  	},
    "202":{
       "nombre":"Ana",
       "segundo":"Laura",
	 	"apellido":"Gonzalez"
   },
    "102":{
       "nombre":"Ignacio",
       "apellido":"Nuñez"
    }
}

while True:
	print("1 - Buscar por legajo")
	print("2 - Buscar por apellido")
	print("3 - Contar cuantos empleados tienen segundo nombre")
	print("4 - Salir\n")

	opcion = input("Ingrese una opcion: ")
 
	if opcion == "1":
		legajo = input("Ingrese el legajo del empleado: ")
		try:
			emp = buscarEmpXLegajo(legajo)
			print(emp["nombre"], emp["segundo"], emp["apellido"], "\n")
		except NotFoundError:
			print("No existe ningun empleado con el legajo '", legajo,"'\n")

	elif opcion == "2":
		apellido = input("Ingrese el apellido del empleado: ")
		try:
			listEmp = buscarEmpsXApellido(apellido)
			print("RESULTADO DE BUSQUEDA CON EL APELLIDO '", apellido,"':")
			for emp in listEmp:
				print(emp["nombre"], emp["segundo"], emp["apellido"])
			print("\n")
		except NotFoundError:
			print("No existe ningun empleado con apellido '", apellido,"'\n")

	elif opcion == "3":
		print("La cantidad de empleados con segundo nombre es: ", contEmpSegundoNombre(), "\n")

	elif opcion == "4":
		break

