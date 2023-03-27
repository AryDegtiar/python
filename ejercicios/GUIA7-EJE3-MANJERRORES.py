#E3 – Realizar una función divisible_por_5 que si retorne un es divisible por 5 o no y que lance la
#excepción correspondiente si el numero en el argumento no es un entero

def divisible_por_5(num):
    try:
        num = int(num)
    except isinstance(num, int):
        raise ValueError("El valor ingresado no es un numero entero")
    else:
        if num % 5 == 0:
            return True
        else:
            return False

while True:
    try:
        num = int(input("Ingrese un numero: "))
        if divisible_por_5(num):
            print("El numero es divisible por 5")
        else:
            print("El numero no es divisible por 5")
    except ValueError:
        print("El valor ingresado no es un numero entero")

    if input("Desea continuar? s/n: ") == "n":
        break