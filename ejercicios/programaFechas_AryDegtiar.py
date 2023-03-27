import fecha_AryDegtiar as moduloFecha

# M2. Intercambiar fecha.py entre los alumnos. Utilizar los módulos recibidos en un programa que
# solicite el ingreso de una fecha (dividida en día, mes, año), compruebe que la fecha es válida y
# muestre la fecha en formato texto e indique si el año es bisiesto, por ejemplo:
# 24-05-2021 se deberá mostrar 24 de Mayo de 2021 – no bisiesto

# NOTA: OJO, AL USAR isinstance SI LE DAS UN BOOLEANO SIEMPRE TE VA A TOMAR COMO VALIDO Y NO COMO ENTERO 

def testsAutomaticos():
    print("VERIFICACION DE FECHAS")
    print("fecha 29, 2, 2000 es valida:", moduloFecha.es_valida(29, 2, 2000), "(deberia ser True)")
    print("fecha 29, 2, 2003 es valida:", moduloFecha.es_valida(29, 2, 2003), "(deberia ser False)")
    print("fecha 32, 2, 2003 es valida:", moduloFecha.es_valida(32, 2, 2003), "(deberia ser False)")
    print("fecha 29, 12, 2003 es valida:", moduloFecha.es_valida(29, 12, 2003), "(deberia ser True)")
    print("fecha 29, 13, 2003 es valida:", moduloFecha.es_valida(29, 13, 2003), "(deberia ser False)")
    print("fecha 22, 2, 1930 es valida:", moduloFecha.es_valida(22, 2, 1930), "(deberia ser True)")
    print("fecha 29, 13, 1929 es valida:", moduloFecha.es_valida(29, 13, 1929),"(deberia ser False)","\n")

    print("VERIFICACION DE MESES SEGUN SU NUMERO")
    print("Meses validos: 1 a 12")
    for i in range(1, 13):
        print("mes", i, "es:", moduloFecha.mes_por_numero(i))
    print("Meses invalidos: menor que 1 o mayores que 12")
    print("mes 0 es:", moduloFecha.mes_por_numero(0), "(deberia ser vacio)")
    print("mes 13 es:", moduloFecha.mes_por_numero(13), "(deberia ser vacio)", "\n")

    print("VERIFICACION DE AÑOS BISIESTOS")
    print("Año 1600", moduloFecha.es_bisiesto(1600), "(deberia ser True)")
    print("Año 1700", moduloFecha.es_bisiesto(1700), "(deberia ser False)")
    print("Año 1800", moduloFecha.es_bisiesto(1800), "(deberia ser False)")
    print("Año 1900", moduloFecha.es_bisiesto(1900), "(deberia ser False)")
    print("Año 2000", moduloFecha.es_bisiesto(2000), "(deberia ser True)")
    print("Año 2003", moduloFecha.es_bisiesto(2001), "(deberia ser False)")
    print("Año 2100", moduloFecha.es_bisiesto(2100), "(deberia ser False)")
    print("Año 2200", moduloFecha.es_bisiesto(2200), "(deberia ser False)")
    print("Año 2300", moduloFecha.es_bisiesto(2300), "(deberia ser False)")
    print("Año 2400", moduloFecha.es_bisiesto(2400), "(deberia ser True)")
    print("Año 2500", moduloFecha.es_bisiesto(2500), "(deberia ser False)", "\n")

    print("-----------------------------------------------")
    print("VERIFICACION DE FECHAS CON DATOS MAL INGRESADOS")
    print("       TODOS DEBERIAN DAR UNA EXCEPCION        ")
    print("-----------------------------------------------")
    print(" -- Funcion Fecha -- ")
    try:
        print("fecha 29, 2, 2000.5 :", moduloFecha.es_valida(29, 2, 2000.5))
    except Exception as e:
        print("Error por Float:", e)
    try:
        print("fecha 29, 'hola', 2000 :", moduloFecha.es_valida(29, "hola", 2000))
    except Exception as e:
        print("Error por String:", e)
    try:
        print("fecha True, 2, 2000 :", moduloFecha.es_valida(True, 2, 2000))
    except Exception as e:
        print("Error por Boolean:", e)

    print(" --  Funcion Mes -- ")
    try:
        print("mes 0.5 :", moduloFecha.mes_por_numero(0.5))
    except Exception as e:
        print("Error por Float:", e)
    try:
        print("mes 'hola' :", moduloFecha.mes_por_numero("hola"))
    except Exception as e:
        print("Error por String:", e)
    try:
        print("mes True :", moduloFecha.mes_por_numero(True))
    except Exception as e:
        print("Error por Boolean:", e)
        
    print(" -- Funcion Bisiesto -- ")
    try:
        print("Año 2000.5 :", moduloFecha.es_bisiesto(2000.5))
    except Exception as e:
        print("Error por Float:", e)
    try:
        print("Año 'hola' :", moduloFecha.es_bisiesto("hola"))
    except Exception as e:
        print("Error por String:", e)
    try:
        print("Año True :", moduloFecha.es_bisiesto(True))
    except Exception as e:
        print("Error por Boolean:", e, "\n")
        
    print(" ////////// FIN DE LAS PRUEBAS DEL TERROR ////////// \n")

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
print("/  INICIO DE LAS PRUEBAS DEL TERROR   /")
print("/        PRIMER DIA COMO QA C:        /")
print("/*************************************/\n")

while True:
    print("Acciones del menu")	
    print("1 - Correr tests automaticos")
    print("2 - Probar funciones")
    print("3 - Salir\n")
    
    try:
        opcion = int(input("Ingrese el numero de la accion a realizar: "))
    except ValueError:
        print("El valor ingresado no es un numero entero")
    
    if opcion == 1:
        testsAutomaticos()
    elif opcion == 2:
        dia = obtenerInputConTipoDato(input("Dia: "))
        mes = obtenerInputConTipoDato(input("Mes: "))
        anio = obtenerInputConTipoDato(input("Año: "))
        
        try: 
           print("La fecha ingresada es valida:", moduloFecha.es_valida(dia, mes, anio))
        except Exception as e:
            print("Error:", e)
        try:
            print("El mes ingresado es:", moduloFecha.mes_por_numero(mes))
        except Exception as e:
            print("Error:", e)
        try:
            print("El año ingresado es bisiesto:", moduloFecha.es_bisiesto(anio), "\n")
        except Exception as e:
            print("Error:", e, "\n")
            
    elif opcion == 3:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida \n")
