# Ejercicios de Condicionales
# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))
if edad>=18:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contrasena = "pancaliente"
password = input("Ingrese su contraseña: ").lower()

if password==contrasena:
    print("Contraseña correcta!!!")
else:
    print("Contraseña incorrecta")

# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))

if a/b == 0:
    print("Error division por 0")
else:
    print(a/b)

# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
n = int(input("Ingrese un numero: "))

if n%2==0:
    print("Numero par")
else:
    print("Numero inpar")

# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos mensuales: "))

if (edad>16) and (ingresos>1000):
    print("Tiene que tributar")
else:
    print("No tiene que tributar")

# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input("Ingrese su nombre: ").lower()
genero = input("Ingrese su genero M o F: ")

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

x = abecedario[0:13]
y = abecedario[13::]

a=[]
b=[]

if genero == "F":
    if nombre[0] in x:
        a.append(nombre)
    elif nombre[0] in y:
        b.append(nombre)
elif genero == "M":
    if nombre[0] in x:
        b.append(nombre)
    elif nombre[0] in y:
        a.append(nombre)

print(f'Grupo a: {a}')
print(f'Grupo b: {b}')

# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta = int(input("Ingrese su renta anual: "))

if renta<=10000:
    print("%5")
elif renta>10000 and renta<=20000:
    print("%15")
elif renta>20000 and renta<=35000:
    print("%20")
elif renta>35000 and renta<=60000:
    print("%30")
elif renta>60000:
    print("%45")

# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
puntos = float(input("Ingrese sus puntos: "))

if puntos==0.0:
    print("Inaceptable")
    print(f'Dinero ganado {puntos*2400}€')
elif puntos==0.4: 
    print("Aceptable")
    print(f'Dinero ganado {puntos*2400}€')
elif puntos<=0.6:
    print("Meritorio")
    print(f'Dinero ganado {puntos*2400}€')

# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Ingrese su edad: "))
if edad<4:
    print("Entrada gratuita")
elif edad>4 and edad<=18:
    print("Entrada a 5€")
elif edad>18:
    print("Entrada a 10€")

# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

menu = """
        Que tipo de pizza desea?
        1 - Vegetariana
        2 - No Vegetariana
        Ingrese tipo de pizza:
        """

pizzaV = """
        Ingredientes
        1 - Pimiento
        2 - Tofu
        Ingrese nombre del ingrediente
        """

pizzaNV = """
        1 - Peperoni
        2 - Jamon
        3 - Salmon
        Ingrese nombre del ingrediente 
        """

opcion = input(menu)


if opcion == "vegetariana":
    opcionP = input(pizzaV)
elif opcion =="no vegetariana":
    opcionP = input(pizzaNV)

print("="*30)
print("----- Tipo de pizza -----")
print(f"----- {opcion} -----")
print("="*30)
print("-----  Ingrdientes  -----")
print("-----  Mozarella")
print("-----  Tomate")
print(f"-----  {opcionP}")