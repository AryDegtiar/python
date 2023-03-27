# A3- Del drive descargar el programa procesos.exe. El mismo muestra en consola una tabla
# con el PID, nombre y usuario de cada proceso corriendo en el sistema.
# Crear un script buscar_proceso.py que reciba como argumento a través de la consola el
# nombre de un proceso, ejecute el programa procesos.exe e imprima su PID y usuario.
# Si hay varios procesos con el mismo nombre, debe imprimir la información de todos ellos.
# Si el nombre del proceso no se ha pasado, debe mostrar un error en la consola y concluir.
# En los procesos en que no aparezca el usuario reemplazarlo por una cadena vacía.

# NOTA v1:
# Diccionario de diccionarios. es la primera opcion que se me ocurrio

# ej:
# 	procesos{
# 		"19323":{
# 			"Process": "chrome.exe", 
# 			"User": "miPCuser"
# 		},
# 		"11223":{
# 			"Process": "chrome.exe", 
# 			"User": "miPCuser"
# 		},
# 		"1246":{
# 			"Process": "otroPrograma.exe", 
# 			"User": "miPCuser"
# 		},
# 		"4321":{
# 			"Process": "chrome.exe", 
# 			"User": "miPCuser"
# 		}
# 	}


import sys
import subprocess

def separarItemsRenglon(renglon):
    # separo los items del renglon
    itemsRenglon = renglon.split("|")
    for e in range(len(itemsRenglon)):
        itemsRenglon[e] = itemsRenglon[e].replace("|", "").strip()
        
    # elimino los primeros y ultimos datos insesarios
    itemsRenglon = itemsRenglon[1:-1]
    itemsRenglon[1] = itemsRenglon[1].lower()
    if itemsRenglon[2] == "-":
        itemsRenglon[2] = ""
    return itemsRenglon

try:
    nombreProceso = sys.argv[1]
    procesosActuales = subprocess.run("procesos.exe", capture_output=True, encoding="cp850").stdout
except IndexError:
    print("Debe ingresar el nombre del proceso a buscar como argument")
except FileNotFoundError:
    print("No se encontro el archivo procesos.exe")
else:
    print("--------------------------------------------")
    # convierto a minusculas
    nombreProceso = nombreProceso.lower()
    print("Nombre del proceso", nombreProceso)
    
    # separo en renglones
    renglones = procesosActuales.split("\n")
    renglones = renglones[3:-2]
    
    # creo un diccionario con los datos de cada proceso
    procesos = {}
    for renglon in renglones:
        # separo los items del renglon
        itemsRenglon = separarItemsRenglon(renglon)
        
        # agrego el proceso al diccionario haciendo diccionario de diccionarios
        procesos[itemsRenglon[0]] = {"Process": itemsRenglon[1], "User": itemsRenglon[2]} 

    print("Procesos encontrados:")
    # busco el proceso
    for pid in procesos:
        # si el proceso coincide con el nombre ingresado, lo imprimo
        if procesos[pid]["Process"] == nombreProceso:
            print("PID:", pid, "Usuario:", procesos[pid]["User"])
    
    print("--------------------------------------------")
        

    