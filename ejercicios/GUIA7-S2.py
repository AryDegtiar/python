# S2- Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
# apariciones de cada carácter en la cadena.

def contadorCaracterEnString(caracter, cadena):
    contador = 0
    pos = cadena.find(caracter)
    while pos != -1:
        contador += 1
        pos = cadena.find(caracter, pos+1)
    return contador

s = "Imprimir todas las ocurrencias de espacios en este enunciado utilizando find"
diccionario = {}

for caracter in s:
    try:
        diccionario[caracter]
    except:
        diccionario[caracter] = contadorCaracterEnString(caracter, s)
    
print(diccionario)