#E4- Realizar una función día_x_número que retorne el nombre de un día correspondiente al
#número pasado, detectando los errores en los datos.

diasDeLaSemana = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}

def día_x_número (num):
    if (isinstance(num, int) == False):
        raise ValueError("El valor ingresado no es un numero entero")

    try:
        return diasDeLaSemana[num]
    except KeyError:
        raise ValueError("El valor ingresado no es un numero entre 1 y 7")

while True:
    try:
        num = int(input("Ingrese un numero: "))
        print(día_x_número(num))
    except ValueError as e:
        print("Error,", e)

    if input("Desea continuar? s/n: ") == "n":
        break