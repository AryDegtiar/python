# A2- Desarrollar un script buscar_archivos.py que reciba como argumentos la ruta a un
# directorio y un nombre de archivo, o parte de él. Deberá buscar los archivos dentro del
# directorio que concuerden con el segundo argumento ingresado y listarlos.
# Si no se pasan los argumentos o la ruta especificada no existe, el programa debe mostrar
# el error en la consola y concluir.

import sys
import os

def listaContieneElemento(lista, elemento):
    res = []
    for item in lista:
        if elemento in item:
            res.append(item)
    return res

try:
    ruta = sys.argv[1]
    nombreArchivo = sys.argv[2]
except IndexError:
    print("Debe ingresar dos argumentos: ruta y nombre de archivo")
else:
    print("--------------------------------------------")
    print("Ruta", ruta)
    print("Nombre de archivo", nombreArchivo)
    if os.path.exists(ruta):
        print("La ruta especificada existe\n")
        listArchivos = os.listdir(ruta)
        archivosEncontrados = listaContieneElemento(listArchivos, nombreArchivo)
        if len(archivosEncontrados) > 0:
            print("Archivos encontrados:")
            for archivo in archivosEncontrados:
                print(archivo)
        else:
            print("No se encontraron archivos con el nombre especificado")
        print("--------------------------------------------")
    else:
        print("La ruta especificada o nombre de archivo inexistentes")
    