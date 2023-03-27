a = "hola mundo"
print(a , type(a))

a = 10
print(a , type(a))

print("division normal ", 11/2)
print("division entera ", 11//2)
print("multiplicacion ", 11.3*2)
print("al cuadrado", 11**2)

print("juan tiene " + str(a))

print("obtengo la parte enetera de un float ", int(32.65))

print(bool(0)) #False
print(bool(1)) #True
print(bool(100000)) # cualquier numero diferente a 0 da True
print(bool("")) #False
print(bool("cualquier cosa")) #True

print(True and False) #Falso (operaciones boleanas)

num = 100
if num == 100:
	print("El numero es 100")
elif num == 101:
	print("El numero es 101")
else:
	print("El numero NO es 100 NI 101")
	
	
	
# - - - C O L E C I O N E S - - -
#Lista ordanada modificable
#Diccionarios no ordenados modificables
#Tuplas ordenadas no modificables
#Set no ordernado no modificable	

#LISTA
lista = [1, 2, 3, 4]
lista = [1, 2 , 5, True, "hola"]
print(lista)
print(lista[4])

lista.append(50) #agrega un nuevo dato al final
print(lista)

lista.insert(2, "nuevo") #agrega un elemento segun un indice: .insert(i, elemento)
print(lista)

lista[0] = 100 # reemplaza el elemento del i = 0 por otro elemento
print(lista) 
	
del lista[0] # elimina el elemento del i = 0
print(lista) 	
	
lista.remove("hola") #elimina la primera ocurrencia del elemento en la lista
print(lista)

elementoEliminado = lista.pop(2) #elimina un elemento de una posicion y tambien lo retorna
print("Se elimino el elemento ", elementoEliminado)
print(lista)

longitudLista = len(lista)
print("la longitud es de ", longitudLista)


#FOR
# ~ newList = [10,20,30,40]
# ~ for elemento in newList:
	# ~ print(elemento)

# ~ range(desde, hasta, incremento)
# ~ range(0, 5, 1) # esto genera [0,1,2,3,4] desde el 0 hasta el uno menos del numero limite
# ~ range(5,1) # toma el desde, desde 0 es decir tambien genera [0,1,2,3,4]
# ~ range(5)  # toma el desde, desde 0 y incremento de 1, es decir tambien genera [0,1,2,3,4]

# ~ print("hola")
# ~ for pos in range(0,4,1):
	# ~ print("hola")

# ~ newList = []
# ~ for valor in range(10, 50, 10):
	# ~ newList.append(valor)


#MATRICES
# ~ matriz = [[1,2], ["A","B"], [4,3.93231]] # matriz 3x2
# ~ matriz = [[1,2], [3,4], [4,3]] # matriz 3x2

# ~ print("ele en matriz", matriz[1][1])

# ~ for fila in range(0,3,1):
	# ~ for columna in range(0,2,1):
		# ~ print(matriz[fila][columna])
		
# ~ for fila in matriz:
	# ~ for columna in fila:
		# ~ print(columna)
		
# cargar una matriz
# ~ matriz = []
# ~ valor = 0

# ~ for fila in range(0, 2, 1):
    # ~ matriz.append([])
    # ~ print(matriz)
    # ~ for columna in range(0, 3, 1):
        # ~ valor += 10
        # ~ matriz[fila].append(valor)
        # ~ print(matriz)

#TUPLAS
tupla = (10,20,30,40)
tuplaDeUnSoloValor = (3,) # obligatorio la coma
sumaDeTupla = tupla + tuplaDeUnSoloValor
# ~ print("tupla: " + str(tupla))
# ~ print(sumaDeTupla)
# ~ for ele in sumaDeTupla:
	# ~ print(ele)

#DICCIONARIOS
# ~ diccionario = {clave1:valor1, clase2: valor2, clase3: valor3}

diccionario = {
	"nombre:":"romina",
	"edad:":30
}
# ~ print(diccionario["edad"])

for clave in diccionario:
	print(clave)
	print(str(diccionario[clave]))

#SET (Conjunto) #tienen que ser unicos
conjunto = {4,6,7,9}

# convertir de lista a set
lista = [1,2,3,1,2,5] 
unicos = set(lista) # salida: {1,2,3,5}
# ~ print(unicos)

# convertir de set a lista
lista = list(unicos) # salida: [1,2,3,5]
# ~ print(lista)

#operandos con lista y set
# ~ print(min(lista))
# ~ print(max(lista))
# ~ print(sum(lista))
# ~ print(sorted(lista))
# ~ print(sorted(lista, reverse = True))

#FECHAS



#MANEJO DE ERRORES
try:
    print(int([1,2,3]))
except ValueError:
	print("Valor invalido")
except TypeError:
	print("Tipo invalido")
except:
	print("Error desconocido")

def sumar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Los parametros deben ser enteros o flotantes")
    return num1 + num2

#try:
#    s = sumar(1, "2")
#except TypeError as e:
#	print(e)

#IMPORTAR
 # tiene que estar en la misma carpeta	
import proyectoGuia4_AryDegtiar # me treigo todo
from proyectoGuia4_AryDegtiar import * # me traigo todo
from proyectoGuia4_AryDegtiar import sumar # me traigo solo la funcion sumar

# MANEJO DE CADENA DE CARACTERES
s = "cadena de caracteres"
print(s[0])	# primer elemento
print(s[-1]) # ultimo elemento
# Slicing
print(s[0:3]) # desde el 0 hasta el 3
print(s[0:3:2]) # desde el 0 hasta el 3 con un incremento de 2
print(s[0:]) # desde el 0 hasta el final
for letra in s:
	print(letra)
if s.startswith("c"):
	print("empieza con c")
if s.endswith("s"):
    print("termina con s")
if s.strip() == "cadena de caracteres": # strip retorna el string quitando los espacios de los extremos
	print("es igual")
s.replace("cadena", "cadena nueva") # reemplaza cadena por cadena nueva, en todos los casos que aparezca "cadena"
s.split(" ") # separa la cadena por el caracter que se le pasa como parametro y lo transforma en una lista
s.split("*****") # transforma el string en una lista de un solo elemento
s.upper() # convierte todo a mayuscula
s.lower() # convierte todo a minuscula
s.find("de") # retorna la posicion de la primera ocurrencia de la cadena que se le pasa como parametro
s.find("de", 0) # retorna la posicion de la primera ocurrencia de la cadena que se le pasa como parametro, a partir del indice 0
s.find("de", 0, 5) # retorna la posicion de la primera ocurrencia de la cadena que se le pasa como parametro, entre los indices 0 y 5
s.capitalize() # convierte la primera letra en mayuscula
s.title() # convierte la primera letra de cada palabra en mayuscula

# SYSTEM ARGVS
import sys
try:
    sys.argv[1]
except IndexError:
    print("No se pasaron argumentos por consola")
else:
    print("Argumentos pasados por consola: ", sys.argv[1:])

# MANEJO DE ARCHIVOS
import os # os es un modulo que permite manejar archivos y carpetas
os.listdir() # lista los archivos de la carpeta actual
os.listdir("c:\\Users") # lista los archivos de la carpeta c:\\Users
os.getcwd()	# retorna el directorio actual
os.path.exists("c:\\Users") # retorna True si existe el directorio
os.mkdir("nueva_carpeta") # crea una carpeta
os.rmdir("nueva_carpeta") # elimina una carpeta
os.path.isfile("archivo.txt") # retorna True si existe el archivo
os.rename("archivo.txt", "nuevo_nombre.txt") # renombra el archivo
os.remove("archivo.txt") # elimina el archivo

import shutil # shutil es un modulo que permite copiar, mover y eliminar archivos y carpetas
shutil.copy("archivo.txt", "copia.txt") # copia el archivo
shutil.move("archivo.txt", "copia.txt") # mueve el archivo
shutil.rmtree("nueva_carpeta") # elimina una carpeta y todo su contenido
shutil.copytree("nueva_carpeta", "copia_carpeta") # copia una carpeta y todo su contenido

import subprocess # subprocess es un modulo que permite ejecutar comandos de consola
subprocess.run({"mkdir", "nueva_carpeta"}, shell=True) # ejecuta el comando mkdir nueva_carpeta
hostname = subprocess.run({"hostname"}, capture_output=True, encoding="cp850") # ejecuta el comando hostname y captura la salida. El comando hostname retorna el nombre de la maquina
resultado = subprocess.run("C\\windows\\Users\\Ary\\Desktop\\Python\\proyectoGuia4_AryDegtiar.py", shell=True) # ejecuta el archivo proyectoGuia4_AryDegtiar.py

archivo = open("archivo.txt", "w") # abre el archivo en modo escritura, si no existe lo crea
archivo.write("Hola mundo\n") # escribe en el archivo
archivo.close() # cierra el archivo

lista = ["Bye\n", "Bye\n", "Bye\n"]
archivo = open("archivo.txt", "a") # abre el archivo en modo append
archivo.write("Hola mundo\n") # escribe en el archivo
archivo.write("Hola mundo\n") # escribe en el archivo
archivo.writelines(lista) # escribe en el archivo
archivo.close() # cierra el archivo

archivo = open("archivo.txt", "r") # abre el archivo en modo lectura
archivo.read() # lee todo el archivo
archivo.close() # cierra el archivo

archivo = open("archivo.txt", "r") # abre el archivo en modo lectura
archivo.readline() # lee una linea del archivo
archivo.readlines() # lee todas las lineas del archivo y las retorna en una lista
archivo.close() # cierra el archivo

archivo = open("archivo.txt", "r") # abre el archivo en modo lectura
linea = archivo.readline()
while linea != "":
	print(linea)
	linea = archivo.readline()
archivo.close() # cierra el archivo

archivo = open("archivo.txt", "r") # abre el archivo en modo lectura
contador = 1
for linea in archivo.readlines():
	print(f"{contador}: {linea}")
	contador += 1
archivo.close() # cierra el archivo

archivo = open("archivo.txt", "r") # abre el archivo en modo lectura
for contador, linea in enumerate(archivo.readlines(), 1): # enumerate retorna un objeto iterable con el indice y el elemento, en este caso el indice empieza en 1
	print(f"{contador}: {linea}")
archivo.close() # cierra el archivo

# CONEXION BDD
import sqlite3
conn = sqlite3.connect("database.sqlite") # crea la base de datos
cursor = conn.cursor() # crea el cursor
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))") # crea la tabla usuarios
conn.commit() # guarda los cambios
conn.close() # cierra la conexion

personas = (
    ("Ary", 30),
    ("Juan", 25), 
    ("Pedro", 35)
)

for nombre, edad in personas:
	cursor.execute(f"INSERT INTO usuarios VALUES ('{nombre}', {edad})")
	cursor.execute(f"INSERT INTO usuarios VALUES (?,?)", ('{nombre}', {edad})) # inserta los datos en la tabla usuarios
conn.commit() # guarda los cambios

cursor.execute("SELECT * FROM usuarios") # selecciona todos los registros de la tabla usuarios
personas = cursor.fetchall() # retorna una lista con los registros
print(personas)
conn.close() # cierra la conexion

cursor.execute("SELECT count(*) FROM usuarios") # selecciona la cantidad de registros de la tabla usuarios
cant = cursor.fetchone() # retorna una tupla con el registro
print(cant) # imprime la cantidad de registros, salida: (3,)
print(cant[0]) # imprime la cantidad de registros, salida: 3
conn.close() # cierra la conexion

try:
	cursor.execute("SELECT * FROM usuarios WHERE nombre = 'Ary'") # selecciona el registro de la tabla usuarios donde el nombre es Ary
	persona = cursor.fetchone() # retorna una tupla con el registro
	print(persona) # imprime el registro, salida: (1, 'Ary', 30, None)
	print(persona[0]) # imprime el registro, salida: 1
	conn.close() # cierra la conexion
except sqlite3.OperationalError:
	print("Error al ejecutar la consulta")

cursor.executescript("SELECT * FROM usuarios WHERE nombre = 'Ary'; SELECT * FROM usuarios WHERE nombre = 'Juan'") # ejecuta dos consultas

##############################
import pymysql # modulo para conectarse a una base de datos mysql
import clave # archivo con la clave de la base de datos

conn.pymysql.connect(
	host = "localhost",
	user = "root",
	password = clave.CLAVE_MYSQL,
	database = "prueba"
)

cursor = conn.cursor() # crea el cursor
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))") # crea la tabla usuarios
conn.commit() # guarda los cambios
conn.close() # cierra la conexion

##############################
import openpyxl # modulo para trabajar con archivos de excel
alumnos = [
	("Ary", 30),
	("Juan", 25), 
    ("Pedro", 35)
]

wb = openpyxl.Workbook() # crea un libro de excel
hoja = wb.active # activa la hoja
hoja.title = "Alumnos" # cambia el nombre de la hoja

hoja.append("nombre", "edad") # agrega una fila con los titulos de las columnas
for alumno in alumnos:
    hoja.append(alumno) # agrega una fila con los datos de los alumnos

hoja.close() # cierra la hoja

# ORIENTADO A OBJETOS
class MiClase:
    def __init__(self, un_numero):
        __oculto = "Soy un atributo privado"
      	self.a = un_numero		
    def publico(self):
        return "Metodo publico"
    def imprimir_a(self):
    	print(self.a)
	def __privado(self):
    	return "Metodo privado"
	def get_oculto(self):
		return self.__oculto

class Hijo(MiClase):
    def __init__(self, un_numero):
		super().__init__(un_numero)
	def publico(self):
		return "Metodo publico hijo"

objecto1 = MiClase(10)
objecto2 = MiClase()

print(objecto1.a) # imprime 10
objecto1.imprimir_a() # imprime 10

print(objecto1.publico()) # imprime Metodo publico
print(objecto1.__privado()) # imprime Metodo privado


# ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
# ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
# ~ GUIA 1 y 2
# ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
# ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
	
# ----------- EJERCICIO 1 -------------
# ~ print()
# ~ print("EJERCICIO 1")
# ~ num1 = 2
# ~ print("El numero 1 es " + str(num1))
# ~ num2 = 3
# ~ print("El numero 2 es " + str(num2))
# ~ num3 = 4
# ~ print("El numero 3 es " + str(num3))

# ~ resultado = num1 + num2 + num3
# ~ print("Resultado " + str(resultado))

# ----------- EJERCICIO 3 -------------
# ~ print()
# ~ print("EJERCICIO 3")
# ~ nombre = "Ary"
# ~ print("Variable nombre: " + nombre)
# ~ edad = 23
# ~ print("Variable edad: " + str(edad))

# ~ print("Soy " + nombre + " y tengo " + str(edad) + " años")

# ----------- EJERCICIO 8 -------------
# ~ print()

# ~ estaEnchufado = bool(input("Ingrese el estado del enchufe, True si esta enchufado, False si NO esta enchufado "))

# ~ interruptorA = bool(input("Ingrese el estado del interruptor A "))
# ~ interruptorB = bool(input("Ingrese el estado del interruptor B "))
# ~ interruptorC = bool(input("Ingrese el estado del interruptor C "))

# ~ if estaEnchufado:
	# ~ if interruptorA or (interruptorB and interruptorC):
		# ~ print("Lampara prendida")
	# ~ else:
		# ~ print("Lampara apagada") 
# ~ else:
	# ~ print("Lampara desenchufada")


# ----------- EJERCICIO 7 -------------
# ~ print()

# ~ num1 = int(input("Ingrese el primer numero "))
# ~ num2 = int(input("Ingrese el segundo numero "))

# ~ operacion = input("Ingrese la operacion matematica ")

# ~ if operacion == "+":
	# ~ resultado = num1 + num2
# ~ elif operacion == "-":
	# ~ resultado = num1 - num2 
# ~ elif operacion == "*":
	# ~ resultado = num1 * num2
# ~ elif operacion == "/":
	# ~ if(num2 == 0):
		# ~ resultado = "Indeterminacion"
	# ~ else: 
		# ~ resultado = num1 / num2
# ~ else:
	# ~ resultado = "Operacion matematica invalida"

# ~ print("Resultado: " , resultado)


# GUIA 3

#eje 1 
# ~ Ingresar por consola número de mes e imprimir el nombre de mes correspondiente
# ~ (Ejemplo: 2 -> Febrero). Si es un número no válido mostrar un mensaje de error.
# ~ Resolverlo utilizando una lista.

# ~ lista = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# ~ print(lista[ int( input("Ingrese el numero del mes: ") ) - 1 ])
# no muestro el mensaje de error si el num es invalido por paja

#eje 3
# ~ L3- A partir de una lista de números calcular la suma de sus elementos. (sin utilizar sum())

# ~ listNum = [1,2,3]
# ~ sumaTotal = 0

# ~ for ele in listNum:
	# ~ sumaTotal += ele

# ~ print("La suma total es: ", sumaTotal)

#eje 6
# ~ L6-¿Cuál es el menor número de una lista de números cualquiera?(sin utilizar min())

# ~ listNum = [1,2,3]
# ~ menorNum = listNum[0]

# ~ for ele in listNum:
	# ~ if(ele < menorNum):
		# ~ menorNum = ele
		
#se puede hacer tmabien con range para evitar el primer paso ya que el primer elemento se compararia al p2

# ~ print("El numero menor es: ", menorNum)

#eje 2
# ~ L2- Solicitar a un usuario una muestra de cinco valores numéricos flotantes, guardarlos en
# ~ una lista y luego calcular el promedio de los mismos a partir de los datos guardados.

# ~ lista = []
# ~ for i in range(5):
	# ~ lista.append(float( input("Ingrese el " + str(i+1) + "  numero flotante: ") ))
	
# ~ sumaTotal = 0	
# ~ for ele in lista:
	# ~ sumaTotal += ele

# ~ print( "El promedio es: ", sumaTotal/len(lista) )


#GUIA 4
#eje 1
# ~ Declarar una matriz de 3x3, donde los valores de cada lista serán ceros y sólo un uno en
# ~ cualquier posición.
# ~ Solicitar al usuario una posición de la matriz determinada por fila y columna. Mostrar un
# ~ mensaje de acierto o fallo y solicitar un nuevo ingreso hasta que se acierte la posición
# ~ donde está el uno.

# ~ matriz = [ 
	# ~ [0,0,0,], 
	# ~ [0,1,0,], 
	# ~ [0,0,0,] 
# ~ ]
	
# ~ acerto = False

# ~ while(not acerto):
	
	# ~ fila = int( input("Ingrese una fila: ") )
	# ~ columna = int( input("Ingrese una columna: ") )
	# ~ if ( (fila < len(matriz)) and (columna < len(matriz[fila])) ):
		# ~ if(matriz[fila-1][columna-1]):
			# ~ acerto = True
			# ~ print("ACERTASTE")
		# ~ else:
			# ~ print("Intente de nuevo")
	# ~ else:
		# ~ print("La matriz es de 3x3, ingrese valores del rango 1 al 3")
		
		
# ~ while(not acerto):
	
	# ~ fila = int( input("Ingrese una fila: ") )
	# ~ columna = int( input("Ingrese una columna: ") )
	# ~ if ( (fila < len(matriz)) and (columna < len(matriz[fila])) ):
		# ~ if(matriz[fila-1][columna-1]):
			# ~ acerto = True
			# ~ print("ACERTASTE")
			# ~ break;
	# ~ print("Intente de nuevo")


#eje 2
# ~ Crear un programa que permita cargar una matriz de dimensiones elegidas por el usuario.
# ~ El código deberá solicitar los números enteros correspondientes a cada celda.
# ~ Supongamos que el usuario elige una matriz de 2 x3
# ~ La entrada y salida del programa para este ejemplo sería similar a la siguiente:
# ~ Ingrese el número de filas: 2
# ~ Ingrese el número de columnas: 3
# ~ Ingrese el número para matriz[0][0]: 10
# ~ Ingrese el número para matriz[0][1]: 11
# ~ Ingrese el número para matriz[0][2]: 12
# ~ Ingrese el número para matriz[1][0]: 20
# ~ Ingrese el número para matriz[1][1]: 21
# ~ Ingrese el número para matriz[1][2]: 22
# ~ La matriz ingresada es:
# ~ [[10, 11, 12], [20, 21, 22]]

# ~ matriz = []

# ~ filas = int( input("Ingrese numero de filas: ") )
# ~ columnas = int( input("Ingrese numero de columnas: ") )

# ~ for fila in range(filas):
    # ~ matriz.append([])
    # ~ for columna in range(columnas):
        # ~ matriz[fila].append( int(input("Ingrese el numero para matriz [" + str(fila) +"] [" + str(columna) +"] :" )) )

# ~ print("La matriz ingresada es:")        
# ~ print(matriz)


#GUIA 5

#eje 1
# ~ D1- Crea un diccionario con los nombres y stock en kilos de distintos metales. Realizar un
# ~ programa que pida el nombre del metal y los kilos que se desean vender del mismo y nos muestre
# ~ si hay o no disponibilidad. Tras cada consulta el programa debe preguntar si queremos hacer otra
# ~ consulta.

# ~ stockMetales = []

# ~ metal = {
	# ~ "nombre":"",
	# ~ "stock": 0,
	# ~ "kilos": 0
# ~ }

# ~ for i in range(5):
	# ~ metal["nombre"] = "nombre" + str(i)
	# ~ metal["stock"] = i*10
	# ~ metal["kilos"] = i*1000
	# ~ stockMetales.append(metal)

# ~ print(stockMetales)

# ~ metalConsultado = {}

# ~ nombreMetal = input("ingrese el nombre del metal: ")
# ~ for met in stockMetales:
	# ~ if met["nombre"] == nombreMetal:
		# ~ metalConsultado = met

# ~ if metalConsultado == {}
	# ~ print("no tenemos el metal " + met["nombre"])
# ~ else:
	# ~ kilosConsultado = int(input("ingrese los kilos que desea comprar: "))
	# ~ if metalConsultado["kilos"] <= kilosConsultado
		# ~ metalConsultado[kilos] = metalConsultado[kilos] - kilosConsultado
		# ~ print("TE VENDO")
	# ~ else:
		# ~ print("no tenemos la cantidad de kilos que necesitas para el metal " + met["nombre"])

#eje 2
# ~ D2 -Escribe un programa que pida un número por consola y que cree un diccionario cuyas claves
# ~ sean desde el número 1 hasta el número indicado incluido, y los valores sean los cuadrados de las
# ~ claves.
# ~ numero = input("Ingrese un numero: ")
# ~ diccionario = {}
# ~ for i in range(1, int(numero)+1, 1):
	# ~ diccionario[i] = i**2
	
# ~ print(diccionario)


#eje3
# ~ D3-Escribe un programa que cree un diccionario simulando un ticket de una compra. El programa
# ~ debe preguntar el artículo y su precio, y añadir el par al diccionario, hasta que el usuario decida
# ~ terminar. Después se debe mostrar por pantalla la lista de la compra y el costo total
# ~ programaCorriendo = True

# ~ ticket = {}

# ~ while programaCorriendo:
	# ~ nombreArt = input("Ingrese el nombre del art: ")
	# ~ precio = int(input("Ingrese el precio del art: "))
	# ~ ticket[nombreArt] = precio
	# ~ seguirAdelante = input("Desea seguir ingresando art? y/n: ")
	# ~ if seguirAdelante == "n":
		# ~ programaCorriendo = False
		
# ~ for nomArt in ticket:
	# ~ print("--------------")
	# ~ print("nombre  precio")
	# ~ print("--------------")
	# ~ print(nomArt + "  " + str(ticket[nomArt]))


#eje4
# ~ D4-Codifica un programa en Python que nos permita guardar los DNIs de los alumnos de una clase
# ~ y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la
# ~ información en un diccionario cuyas claves serán los DNIs de los alumnos y los valores serán listas
# ~ con las notas de cada alumno.

# ~ clase = {}

# ~ while True:
	# ~ while True:
		# ~ dni = int(input("ingrese dni alumno: "))
		# ~ if dni > 0:
			# ~ break
		# ~ else: 
			# ~ print("dni invalido, ingrese nuevamente")
		 
	# ~ listNotas  = []
	
	# ~ while True:
		# ~ if "y" == input("desea agregar una nota? y/n: "):
			# ~ nota = int(input("ingrese la nota del alumno: "))
			# ~ if nota >= 0:
				# ~ listNotas.append(nota)
			# ~ else:
				# ~ print("nota invalida, ingrese nuevamente")
		# ~ else:
			# ~ break

	# ~ clase[dni] = listNotas
	
	# ~ if "n" == input("desea agregar otro alumno? y/n: "):
		# ~ break

# ~ print("--------------")
# ~ print("dni      notas")
# ~ print("--------------")
# ~ for dniAlu in clase:
	# ~ print(str(dniAlu) + "  " + str(clase[dniAlu]))

#eje 1
# ~ T1- Solicitar a un usuario diez números enteros al azar. Una vez finalizado el ingreso, mostrarlos
# ~ ordenados y sin números repetidos
# ~ numeros = []
# ~ while len(numeros) < 10:
    # ~ num = input("Ingrese un número entero: ")
    # ~ numeros.append(int(num))

# ~ numerosUnicos = list(set(numeros))

# ~ print("Los números ingresados, ordenados y sin repetir son: ", sorted(numerosUnicos))




