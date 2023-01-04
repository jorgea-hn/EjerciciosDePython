# Ejercicios de Tipos de Datos Simples

# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
x = "¡Hola Mundo!"
print(x)

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
n = input("Ingrese su nombre: ")
print(f'¡Hola {n}!')

# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
print(((3+2)/(2*5))**2)


# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input('Ingrese el numero de horas trabajadas: '))
precio = int(input('Ingrese el coste de la hora: '))
operacion = horas*precio
print(operacion)

# Ejercicio 6
# Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:

n = int(input("Ingrese un numero: "))
suma = (n*(n+1))/2
print(suma)
 


# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura: "))

IMC = peso/(altura)**2
print(f'Tu indice de masa corporal es {round(IMC,2)}')

# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = a//b
r = a%b
print(f'La {a} entre {b} da un cociente {c} y un resto {r}')


# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad = float(input("Ingrese la cantidad a invertir: "))
intAnual = float(input("Ingrese su interes anual: "))
anos = int(input("Ingrese el numero de Años: "))

for i in range (1,anos+1):
    cantidad = cantidad + (cantidad*(intAnual/100))

print(f'El capital obtenido es {cantidad}')




# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payaso = 112
muneca = 75

cantP = int(input("Ingrese la cantidad de payasos: "))
cantM = int(input("Ingrese la cantidad de muñecas: "))

PesoP = cantP * payaso
PesoM = cantM * muneca

PesoTotal = PesoP+PesoM
print(f'El peso total del paquete es{PesoTotal}')

# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

int = 0.04
ahorro = float(input("Ingrese la cantidad de dinero: "))
anos=3

for i in range(1,anos+1):
    ahorro = ahorro + (ahorro*int)

print(f'El capital obtenido es {round(ahorro,2)}')

# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barrasV = int(input("Ingrese la cantidad de pan vendido: "))
precioPan = 3.49
desc = 60
precioDesc = precioPan * (desc/100)

total = barrasV * precioDesc
print("-"*30)
print(f"----Precio habitual:{precioPan}  ----")
print(f"----Descuento: {desc}%        ----")
print(f'----Precio total: {round(total,2)}   ----')
print("-"*30)



