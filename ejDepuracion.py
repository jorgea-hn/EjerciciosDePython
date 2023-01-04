# Ejercicios de Depuración

# Ejercicio 1
# Corregir los errores sintácticos del siguiente programa:

# contraseña = input('Introduce la contraseña: ")
# if contraseña in ['sesamo'):
#   print('Pasa')
# else
#   print('No pasa')

contraseña = input("Introduce la contraseña: ")
if contraseña in ('sesamo'):
  print('Pasa')
else:
  print('No pasa')

# Ejercicio 2
# Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:

# base = input('Introduce la base imponible de la factura: ')
# print(aplica_iva(base, iva))

# def aplica_iva(base, iva = 21):
#     base = base * iva   
#     return base

base = input('Introduce la base imponible de la factura: ')


def aplica_iva(base, iva = 21):
    valor = int(base)
    base = valor + valor * iva/100   
    return base  

print(aplica_iva(base))

# Ejercicio 3
# Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos vectores:

# u = (1, 2, 3)
# v = (4, 5, 6)

# def producto_escalar(u, v):
#     for i in u:
#         u[i+1] *= v[i+1]
#     return sum(u)

# print(producto_escalar(u, v))

u = (1, 2, 3)
v = (4, 5, 6)

def producto_escalar(u, v):
    multiplicacion = 0
    suma = 0
    for i,j in zip(u,v):
        multiplicacion = i * j
        suma += multiplicacion
    return suma 

print(producto_escalar(u, v))


u = [1, 2, 3]
v = [4, 5, 6]

def producto_escalar2(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)

print(producto_escalar(u, v))


# Ejercicio 4
# Detectar y corregir los errores del siguiente programa que devuelve y elimina el teléfono de un listín telefónico a través del nombre del usuario:

# listin = {'Juan':123456789, 'Pedro':987654321}

# def elimina(listin, usuario):
#     del listin[usuario]
#     return listin[usuario]

# print(elimina(listin, 'Pablo'))

listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):

    if usuario not in listin.keys():
        return "Usuario no existente"
    elif usuario in listin.keys():
        del listin[usuario]
        return listin


print(elimina(listin, 'Pedro'))

listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):
    return listin.pop(usuario, '')

print(elimina(listin, 'Pablo'))



# Ejercicio 5
# Detectar y corregir los errores del siguiente programa que multiplica dos matrices:

# a = ((1, 2, 3),
#      (3, 2, 1))
# b = ((1, 2),
#      (3, 4),
#      (5, 6))

# def producto(a, b):
#     producto = []
#     for i in range(len(b)):
#         fila = []
#         for j in range(len(a[0])):
#             suma = 0
#             for k in range(len(a[0]+1)):
#                 suma += a[i][k] * b[k+1][j]
#             fila[j] = suma
#         producto[i] = tuple(fila)
#     return tuple(producto)

# print(producto(a, b))

a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = [] 
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(a[0])):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

print(producto(a, b))