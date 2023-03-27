# A1- Desarrollar un script para Imprimir todos los argumentos pasados por consola excepto
# el primero correspondiente al nombre del archivo.

import sys

try:
    sys.argv[1]
except IndexError:
    print("No se pasaron argumentos por consola")
else:
    print("Argumentos pasados por consola: ", sys.argv[1:])