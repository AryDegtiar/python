# S1- Imprimir todas las ocurrencias de espacios en este enunciado utilizando find.

s = "Imprimir todas las ocurrencias de espacios en este enunciado utilizando find"

posUltimoEspacio = -1
while s.find(" ") != -1:
    posUltimoEspacio += s.find(" ") +1
    print("Espacio en la posicion", posUltimoEspacio)
    s = s[s.find(" ")+1:]