# Ejercicios de Cadenas
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre = input("Ingrese su nombre: ")
n = int(input("Ingrese un numero: "))
for i in range(1,n+1):
    print(nombre)

# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre = input("Ingrese su nombre completo: ")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
nombre = input("Ingrese su nombre completo: ")
nombreM = nombre.upper()
cantidad = len(nombre.replace(" ", ""))

print(f'El nombre {nombre.upper()} tiene {cantidad} letras')


# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

telefono = input("Ingrese el numero de telefono: ")
n = telefono.split("-")
print(f'El numero es {n[1]}')


# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = input("Ingrese una frase: ")
print(frase[::-1])

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")

if vocal in frase:
    print(frase.replace(vocal,vocal.upper()))
else:
    print("La vocal no se encuentra")

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Ingrese un correo: ")
x = correo.split("@")
print(f'{x[0]}'+"@ceu.es")

# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Ingrese el precio del producto: ")
x = precio.split(".")
print(f'Euros:{x[0]}, centimos: {x[1]}')

# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fechaN = input("Ingrese la fecha de su nacimiento dd/mm/aaaa: ")
f = fechaN.split("/")
print(f"Dia: {f[0]}, Mes: {f[1]}, Año: {f[2]}")

# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
compra = input("Ingrese los productos de su cesta de compra separados por ',': ")
compra = compra.split(",")

for i in range(0,len(compra)):
    print(f'{i+1}. {compra[i]}')

# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto= input("Ingrese el nombre del producto: ")
precio= (input("Ingrese el precio del producto: "))
un = (input("Ingrese la cantidad de unidades del producto: "))
total = int(precio) *int(un)

pm = abs(len(precio)-6)
print('0'*pm + precio +','+ '0'*2)

um = abs(len(un)-3)
print('0'*pm + un)

tm = abs(len(un)-8)
print('0'*pm + str(total) +','+ '0'*2)

