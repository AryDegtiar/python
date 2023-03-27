import fecha_AryDegtiar as moduloFecha

# M2. Intercambiar fecha.py entre los alumnos. Utilizar los módulos recibidos en un programa que
# solicite el ingreso de una fecha (dividida en día, mes, año), compruebe que la fecha es válida y
# muestre la fecha en formato texto e indique si el año es bisiesto, por ejemplo:
# 24-05-2021 se deberá mostrar 24 de Mayo de 2021 – no bisiesto

# NOTA: OJO, AL USAR isinstance SI LE DAS UN BOOLEANO SIEMPRE TE VA A TOMAR COMO VALIDO Y NO COMO ENTERO 

def obtenerInputConTipoDato(inputString):
    try:
        resultado = int(inputString)
        return resultado
    except ValueError:
        pass

    try:
        resultado = float(inputString)
        return resultado
    except ValueError:
        pass

    if inputString.lower() == 'true':
        resultado = True
        return resultado
    elif inputString.lower() == 'false':
        resultado = False
        return resultado

    resultado = str(inputString)
    return resultado


print("/*************************************/")
print("/            INICIO PROGRAMA          /")
print("/*************************************/\n")

dia = obtenerInputConTipoDato(input("Dia: "))
mes = obtenerInputConTipoDato(input("Mes: "))
anio = obtenerInputConTipoDato(input("Año: "))

try:
    if moduloFecha.es_valida(dia, mes, anio):
        print("La fecha es: " + str(dia) + " de " + moduloFecha.mes_por_numero(mes) + " de " + str(anio) + " - " + ("bisiesto" if moduloFecha.es_bisiesto(anio) else "no bisiesto"))
    else:
        print("La fecha ingresada no es valida")
except:
    print("Los tipos de datos de la fecha ingresada no son validos")
    