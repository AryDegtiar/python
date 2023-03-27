# A4- Generar el archivo backup.py, que reciba un directorio como argumento por consola y
# genere una copia de dicho directorio y su contenido en un directorio para backups
# c:\bkppy\ creado previamente. La copia del directorio debe contener la fecha en su
# nombre con formato _aaaammdd.

import sys
import os
import shutil
from datetime import date

rutaBackUp = "c:\\bkppy"

try:
    rutaDirectorio = sys.argv[1]
except IndexError:
    print("Debe ingresar un direcctorio como argumento")
else:
    if os.path.exists(rutaDirectorio):
        nombreCarpetas = rutaDirectorio.split("\\")
        nombreCarpeta = nombreCarpetas[len(nombreCarpetas) - 1]
        
        # Si no existe el directorio de backup, lo creo
        if not os.path.exists(rutaBackUp):
            os.mkdir(rutaBackUp)
        
        # Obtengo la fecha actual y genero la ruta del backup
        fechaActual = date.today().strftime("%Y%m%d")
        rutaBackUpFecha = rutaBackUp + '\\' + nombreCarpeta + '_' + fechaActual
        
        # Si existe la carpeta del backup de hoy
        if os.path.exists(rutaBackUpFecha):
            # elimino todos los archivos de la carpeta
            for archivo in os.listdir(rutaBackUpFecha):
                os.remove(rutaBackUpFecha + "/" + archivo)
        else:
            # Creo la carpeta con la fecha actual
            os.mkdir(rutaBackUpFecha)

        for archivo in os.listdir(rutaDirectorio):
            try:
                # Copio el archivo al backup
                shutil.copy(rutaDirectorio + '/' + archivo, rutaBackUpFecha)
                print("Archivo copiado", archivo)
            except FileNotFoundError:
                print("No se pudo copiar el archivo", archivo)
                
    else:
        print("Ruta especificada inexistente")