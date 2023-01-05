# Ejercicios de Programación Funcional
# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

def descuento(precio):
    return precio + (precio * 0.1)

def iva(precio):
    return precio + (precio* 0.19)

def precioFinal(cesta):
    total = 0
    for x, y in cesta.items():
        total += y + (iva(y) - descuento(y))
    print(f"El precio total de la canaste es {total}")

precioFinal({"pan":3000,"mango":1200,"limon":500,"arroz":3000})

# Ejercicio 2
# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

import math
def calculadora():
    numero = float(input("Ingrse valor a operar: "))

    menu ="""
        Calculadora cientifica
        1 - Seno
        2 - Coseno
        3 - Tangente
        4 - Exponencial
        5 - Logaritmo Neperiano
        Ingrese una de las opciones
        """
    opcion = input(menu)
    
    numeroInt = int(numero)
    for i in range(1,numeroInt+1):
        print(i)


    if opcion=="1":
        return math.sin(numero)
    elif opcion=="2":
        return math.cos(numero)
    elif opcion=="3":
        return math.tan(numero)
    elif opcion=="4":
        return numero**numero
    elif opcion=="5":
        return math.log(numero)

print(calculadora())

# Ejercicio 3
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
numeros = [2,3,4,5,6,7,8]
def cuadrado(n):
    return n**2


def potencia(func,numeros):
    elevado = []
    for i in numeros:
        elevado.append(func(i))
    print(elevado)

potencia(cuadrado,numeros)



# Ejercicio 4
# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.
numeros = [2,0,4,0,6,0,8]
def booleana(n):
    return bool(n)


def potencia(func,numeros):
    booleanType = []
    for i in numeros:
        if func(i)==True:
            booleanType.append(i)
        
    print(booleanType)

potencia(booleana,numeros)

# Ejercicio 5
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

diccionario = {}
def contador_caracteres(frase):
    fraseN = frase.split(" ")
    longitud=0
    for i in fraseN:
        if fraseN.count(i)>1:
            fraseN.remove(i)

    for i in fraseN:
        longitud = len(i)
        diccionario[i]=longitud
    print(diccionario)

contador_caracteres("Hola mi nombre es jorge y me gusta comer y jugar y dibujar")

# Ejercicio 6
# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

conversion = {1:"Deficiente",2:"Insuficiente",3:"Acaptable",4:"Sobresaliente",5:"Excelente" }
calificaciones = []
def notas(notas):
    for nota in notas:
        calificaciones.append(conversion[nota])
    print(calificaciones)
notas([2,3,5,1,4,3,5])

# Ejercicio 7
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
conversion = {1:"Deficiente",2:"Insuficiente",3:"Acaptable",4:"Sobresaliente",5:"Excelente" }
calificaciones = {}
def notas(notas):
    for x, y in notas.items():
        calificaciones[x.upper()]= conversion[y]
    print(calificaciones)

notas({"Matematicas":3,"Sociales":2,"Ingles":5,"Biologia":4, "Informatica":5})

# Ejercicio 8
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.
conversion = {1:"Deficiente",2:"Insuficiente",3:"Acaptable",4:"Sobresaliente",5:"Excelente" }
calificaciones = {}
def notas(notas):
    for x, y in notas.items():
        if y>=3:
            calificaciones[x.upper()]= conversion[y]
    print(calificaciones)

notas({"Matematicas":3,"Sociales":2,"Ingles":5,"Biologia":4, "Informatica":5})

# Ejercicio 9
# Escribir una función que calcule el módulo de un vector.
def modulo(n1,n2):
    return ((n1**2)+(n2**2))**(1/2)

print(modulo(3,4))

# Ejercicio 10
# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
valor=2000000

def busqueda(inmuebles,valor):
    precio = 0
    lista = []
    for i in inmuebles:
        if (i["zona"]=="A"):
            precio = (i["metros"] * 1000 + i["habitaciones"] * 5000 + i["garaje"] * 15000) * (1-i["año"]/100)
            i["precio"]=abs(precio)
        elif (i["zona"]=="B"):
            precio = (i["metros"] * 1000 + i["habitaciones"] * 5000 + i["garaje"] * 15000) * (1-i["año"]/100)*1.5
            i["precio"]=abs(precio)
    
    for j in inmuebles:
        if valor>=j["precio"]:
            lista.append(j)
    
    print(lista)

    
busqueda(inmuebles,valor)

# Ejercicio 11
# Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.

def valoresAtipicos(*args):
    valores=[]
    suma = 0
    desviacion = 0
    longitud = len(args)
    for i in args:
        suma += i

    media = suma/longitud

    for i in args:
        desviacion += (i-media)**2
    
    desviacionTipica = desviacion**(1/2)

    for i in args:
        valores.append((i-media)/desviacionTipica)

    for i in valores:
        if i>=3 or i<=-3:
            print(i)

valoresAtipicos(1,2,3,4,5,6,7,28,260,1998,98098896)