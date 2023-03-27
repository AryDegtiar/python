## Modulo de fechas
# Tgriffabenitez


def es_valida(dia, mes, anio):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    fecha_valdia = True

    if type(dia) != int or type(mes) != int or type(anio) != int:
        raise TypeError("Debe ingresar un numero entero")

    if anio < 1930:
        fecha_valdia = False
    
    if mes < 1 or mes > 12:
        fecha_valdia = False
    elif dia < 1 or dia > dias_por_mes[mes - 1]:
        fecha_valdia = False

    if es_bisiesto(anio):
        dias_por_mes[1] = 29
        fecha_valdia = True

    return fecha_valdia

def mes_por_numero(numero):
    meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 8:"Septiembre",9:"alto numero", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
    
    if type(numero) != int:
        raise TypeError("Debe ingresar un numero entero")
    
    if numero > 12 or numero < 1:
        return ""
    
    return meses[numero]


def es_bisiesto(anio):
    es_anio_bisiesto = False

    if type(anio) != int:
        raise TypeError("Debe ingresar un numero entero")

    # si un anio es divisible entre 4 pero no entre 100, entonces el anio es bisiesto
    # los anios divisibles por 400 tambien sos bisiestos
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        es_anio_bisiesto = True

    return es_anio_bisiesto



