# Ejercicios de Bucles
# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
nombre = input("Ingrese su nombre: ")
for i in range(0,10):
    print(f'{i+1} - {nombre}')

# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingrese su edad: "))
for i in range(1,edad+1):
    print(i)

# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
impares=[]
n = int(input("Ingrese un numero: "))



while n<0:
    n = int(input("Ingrese un numero: "))

if n>0:
    for i in range(1,n+1):
        if i%2!=0:
            impares.append(i)
    print(impares)

# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

regresivo=[]
n = int(input("Ingrese un numero: "))


while n<0:
    n = int(input("Ingrese un numero: "))
    
if n>0:
    for i in range(0,n+1):
        regresivo.append(n-i)
    print(regresivo)

# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad = float(input("Ingrese la cantidad a invertir: "))
intAnual = float(input("Ingrese su interes anual: "))
anos = int(input("Ingrese el numero de Años: "))

for i in range (1,anos+1):
    cantidad = cantidad + (cantidad*(intAnual/100))
    print(f'El capital obtenido es {cantidad} en el año {i}')

# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****


n = int(input("Ingrese un numero: "))


while n<0:
    n = int(input("Ingrese un numero correcto: "))
    
if n>0:
    for i in range(0,n+1):
        print("*"*i)
# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1,11):
    print("")
    print(f'Tabla del {i}')
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')

# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

n = int(input("Ingrese un numero: "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
    
# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password = "jorgito"

passwordU = input("Ingrese su contraseña: ")

while password!=passwordU:
    passwordU = input("Ingrese su contraseña: ")
    if(password==passwordU):
        print("Contraseña correcta")

# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
n = int(input("Ingrese un numero: "))
c = 0 
for i in range(1,10):
    if n%i==0:
        c += c
if n==1:
    print("Numero no Primo")
elif c>2:
    print("Numero no Primo")
else:
    print("Numero primo")


# Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Ingrese una palabra: ")
palabra= palabra[::-1]
for x in palabra:
    print(x)

# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

print(frase.count(letra))

# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
frase = input("Ingrese una frase o palabra: ")

while frase!="salir":
    for i in range(0,len(frase)):
        for j in frase:
            print(frase)
            frase = frase.replace(frase[i],"")
    frase = input("Ingrese una frase o palabra: ")
    if frase=="salir":
        break