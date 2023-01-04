# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
def saludo():
    print("¡Hola amigo!")

saludo()

# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludo1(nombre):
    print(f'Hola {nombre}!.')

saludo1("Jorge")
# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    factorial = 1
    for i in range(numero,0,-1):
        factorial = factorial*i
    print(factorial)

factorial(5)
# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def total(cantidad):
    cantidad_con_iva = cantidad + cantidad*0.21
    print(f'El cantidad con iva es de {cantidad_con_iva}')

total(100)



# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math
def areaCirculo(radio):
    area = math.pi * (radio**2)
    return round(area,2)

print(areaCirculo(5))

def volumenCilindro(radio,altura):
    base = areaCirculo(radio)
    volumen = base*altura
    return volumen

print(volumenCilindro(3,6))


# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(*args):
    promedio = 0
    longitud = len(args[0])
    for i in range(longitud):
        promedio = promedio + args[0][i]
        print(promedio/longitud)

media([1,2,3,4,5])
# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadradoNumero(*args):
    cuadrados = []
    longitud = len(args[0])
    for i in range(longitud):
        cuadrado = args[0][i] **2
        cuadrados.append(cuadrado)
    print(cuadrados)

cuadradoNumero([1,2,3,4,5])

# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
def estadisticas(*args):
    diccionario = {}
    longitud = len(args[0])
    suma = 0
    promedio = 0
    sumav=0
    varianza = 0
    for i in range(longitud):
        suma += args[0][i]
    promedio = suma/longitud

    for i in range(longitud):
        sumav += (args[0][i]-promedio)**2
    varianza = sumav/longitud

    desviacion = round(math.sqrt(varianza),2)
    diccionario["Promedio"] = promedio
    diccionario["Varianza"] = varianza
    diccionario["Desviacion"] = desviacion
    print(diccionario)

estadisticas([1,2,3,4,5])

# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def maxComunDiv(n1,n2):
    divN1=[]
    for i in range(1,n1+1):
        if n1%i==0:
            divN1.append(i)
    divN2=[]
    for j in range(1,n2+1):
        if n2%j==0:
            divN2.append(j)


    mayor = 0
    for l in divN1:
        for m in divN2:
            if l==m:
                mayor=l
    print(mayor)
    
maxComunDiv(15,20)

def minComunMult(n1,n2):
    mayor = 0
    if n1<n2:
        mayor = n2
    else:
        mayor = n1
    mulN1=[]
    mulN2=[]
    for i in range(1,mayor+1):
        mulN1.append(n1*i)
        mulN2.append(n2*i)

    mul=[]
    for l in mulN1:
        for m in mulN2:
            if l==m:
                mul.append(m)
    print(mul[0])

minComunMult(3,9)

# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

# def decimal_binario(numero):
#     binario =""
#     cociente = numero//2  
#     modulo = numero%2      
#     while cociente!=0:
#         binario += str(modulo)   
#         print(f'cociente {cociente}') 
#         modulo = cociente%2  
#         cociente = cociente//2     
#         print(f'modulo {modulo}') 
#         if cociente==0:
#             break
#     print(f'binario {binario}')
    

# decimal_binario(10)

def binario_decimal(binario):
    binario = str(binario)
    binarioInv= binario[::-1]
    decimal = 0
    print(binario)
    for i in range(len(binario)):
        if binarioInv[i]=="1":
            decimal += 2**i
    print(decimal)

binario_decimal(1111)


# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia


diccionario = {}
def contador_caracteres(frase):
    fraseN = frase.split(" ")
    veces=0
    for i in fraseN:
        if fraseN.count(i)>1:
            fraseN.remove(i)

    for i in fraseN:
        veces = frase.count(i)
        diccionario[i]=veces
        # print(f'La palabra {i} se repite {veces} veces')
    return diccionario

contador_caracteres("Hola mi nombre es jorge y me gusta comer y jugar y dibujar")

def repetida(diccionario):
    aux = 0
    name =""

    for x, y in diccionario.items():
        if aux<y:
            aux=y
            name=x
    tupla = (name,aux)
    print(tupla)

repetida(contador_caracteres("Hola mi nombre es jorge y me gusta comer y jugar y dibujar"))

