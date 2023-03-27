#E2 - Ingresar dos números e imprimir el resultado de las cuatro operaciones básicas (+, -,* ,/)

while True:
    try:
        numA = int(input("Ingrese el primer numero: "))
    except TypeError:
        print("El valor ingresado no es un numero")
    
    try:
        numB = int(input("Ingrese el segundo numero: "))
    except TypeError:
        print("El valor ingresado no es un numero")
    
    print("La suma de los numeros es: ", numA + numB)
    print("La resta de los numeros es: ", numA - numB)
    print("La multiplicacion de los numeros es: ", numA * numB)
    
    try:
        print("La division de los numeros es: ", numA / numB)
    except ZeroDivisionError as e:
        print("Error,", e)
        
    continuar = input("Desea continuar? s/n: ")
    if continuar == "n":
        break