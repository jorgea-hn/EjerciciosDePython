# Ejercicios de Listas y Tuplas
# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
materia = input("Ingrese la materia: ")
lista=[]
while materia!="salir":
    lista.append(materia)
    materia = input("Ingrese la materia o salir: ")
    if materia=="salir":
        break
print(lista)

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

materia = input("Ingrese la materia: ")
lista=[]
while materia!="salir":
    lista.append(materia)
    materia = input("Ingrese la materia o salir: ")
    if materia=="salir":
        break

for i in lista:
    print(f'Yo estudio {i}')
    
# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

materia = input("Ingrese la materia: ")
materias=[]
while materia!="salir":
    materias.append(materia)
    materia = input("Ingrese la materia o salir: ")
    if materia=="salir":
        break


notas = []
for i in materias:
    nota = input(f'Ingrese la nota de la materia {i}: ')
    notas.append(nota)

for i,j in zip(materias,notas):
    print(f"En {i} la nota fue {j}")

# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

n = input("Ingrese los numeros de la loteria : ")
numeros=[]
while n!="salir":
    n = int(n)
    numeros.append(n)
    n = input("Ingrese los numeros de la loteria o salir: ")
    if n=="salir":
        break


numeros.sort()
print(numeros)

# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

n = input("Ingrese un numero : ")
numeros=[]
while n!="salir":
    n = int(n)
    numeros.append(n)
    n = input("Ingrese un numero o salir: ")
    if n=="salir":
        break


print(numeros[::-1])

# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

materia = input("Ingrese la materia: ")
materias=[]
while materia!="salir":
    materias.append(materia)
    materia = input("Ingrese la materia o salir: ")
    if materia=="salir":
        break


notas = []
for i in materias:
    nota = int(input(f'Ingrese la nota de la materia {i}: '))
    notas.append(nota)


for i,j in zip(materias,notas):
    if j<=3:
        print(f"En {i} la nota fue {j}")

# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(1,len(abecedario)+1):
    if i%3==0:
        print(abecedario[i-1])

# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input("Ingrese una palabra: ")

if ( palabra[::-1]== palabra):
    print(f'La palabra {palabra} es palindroma')
else:
    print(f'La palabra {palabra} no es palindroma')



# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
frase = input("Ingrese una frase: ").lower()

print(f'La vocal a se repite {frase.count("a")} veces')
print(f'La vocal e se repite {frase.count("e")} veces')
print(f'La vocal i se repite {frase.count("i")} veces')
print(f'La vocal o se repite {frase.count("o")} veces')
print(f'La vocal u se repite {frase.count("u")} veces')  

# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista = [50, 75, 46, 22, 80, 65, 8]

mayor = 0
menor = 0

for i in lista:
    if i > mayor:
        mayor = i
    else:
        menor = i

print(mayor)
print(menor)

# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
x =  (1,2,3) 
y =  (-1,0,2)
xy = []

for i,j in zip(x,y):
    sum = i*j
    xy.append(sum)

total = 0
for l in xy:
    total += l

print(total)

# Ejercicio 12
# Escribir un programa que almacene las matrices
 
 

# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.


# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
muestra =[1,2,3,4,5,6,7,8,9,10]  #55/10 = 5.5
sum = 0
media = 0 
for x in muestra:
    sum +=x

media = sum/len(muestra)

varianza=0
for y in muestra:
    varianza = varianza + ((y-media)**2)

varianza = varianza/len(muestra)


desviacion = varianza**(1/2)
print(desviacion)


