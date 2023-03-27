#M1. Generar un módulo fecha que contenga las siguientes funciones. Guardar el archivo como fecha.py

meses = {
    1: {"nombre":"Enero", "dias": 31},
    2: {"nombre":"Febrero", "dias": 28},
    3: {"nombre":"Marzo", "dias": 31},
    4: {"nombre":"Abril", "dias": 30},
    5: {"nombre":"Mayo", "dias": 31},
    6: {"nombre":"Junio", "dias": 30},
    7: {"nombre":"Julio", "dias": 31},
    8: {"nombre":"Agosto", "dias": 31},
    9: {"nombre":"Septiembre", "dias": 30},
    10: {"nombre":"Octubre", "dias": 31},
    11: {"nombre":"Noviembre", "dias": 30},
    12: {"nombre":"Diciembre", "dias": 31}
}

anioMinimo = 1930

# es_valida(dia,mes,año):es válida si los días corresponden con el mes .Ej 31/4 no es válido
def es_valida(dia, mes, anio):
    if (type(dia) != int or type(mes) != int or type(anio) != int):
        raise TypeError("Datos de fecha mal ingresados")
    
    if es_bisiesto(anio) and dia == 29 and mes == 2:
        return True

    if anio >= anioMinimo and (mes >= 1 and mes <= 12):
        diasDelMes = meses[mes]["dias"]
        if dia >= 1 and dia <= diasDelMes:
            return True
        else:
            return False
    else:
        return False
    
# devuelve un string con el nombre del mes    
def mes_por_numero(numero):
    if (type(numero) != int):
        raise TypeError("Datos de fecha mal ingresados")
    
    try:
        mes = meses[numero]["nombre"]
        return mes
    except:
        return ""
    
# es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400
def es_bisiesto(anio):
    if (type(anio) != int):
        raise TypeError("Datos de fecha mal ingresados")
    
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    