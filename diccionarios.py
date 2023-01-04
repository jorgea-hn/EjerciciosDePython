# Ejercicios de Diccionarios
# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

menu="""
    Menu de divisas
    Euro
    Dollar
    Yen
    Ingrese una divisa
    """

divisa = input(menu)

sum=0
for i in divisas:
    if divisa==i:
        print(f'La divisa es {divisas[i]}')
    else:
        sum += 1
        if(sum==len(divisas)):
            print("La divisa no existe")

# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

contacto = {}

nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
direccion=input("Ingrese su direccion: ")
telefono=input("Ingrese su telefono: ")

contacto["Nombre"] = nombre
contacto["Edad"] = edad
contacto["Direccion"] = direccion
contacto["Telefono"] = telefono
print(contacto)

# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera":0.85,"Naranja":0.70}
                

menu = """
        ---- Frutas ----
        Platano
        Manzana
        Pera
        Naranja
        Ingrese una fruta
        """
fruta = input(menu)

sum=0
for i in frutas:
    if fruta==i:
        kilos = int(input("Ingrese un numero de kilos: "))
        total = frutas[i] * kilos
        print(f'El precio total del kilo de {fruta} es {total}')
    else:
        sum += 1
        if(sum==len(frutas)):
            print("La fruta no esta en el diccionario")

# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
meses ={
    "01":"Enero",
    "02":"Febrero",
    "03":"Marzo",
    "04":"Abril",
    "05":"Mayo",
    "06":"Junio",
    "07":"Julio",
    "08":"Agosto",
    "09":"Septiembre",
    "10":"Octubre",
    "11":"Noviembre",
    "12":"Diciembre",
}

fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
fecha = fecha.split("/")
print(f'La fecha es {fecha[0]} del mes de {meses[fecha[1]]} del año {fecha[2]}')

# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
suma = 0
for x, y in creditos.items():
    suma += y
    print(f'La asignatura {x} tiene {y} creditos')

print(f"El numero de creditos total es {suma}")

# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
diccionario = {}
dic = {}
nombre = input("Ingrese su nombre: ")
c = 0
while nombre!="salir":
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero: ")
    direccion = input("Ingrese su direccion: ")
    correo = input("Ingrese su correo: ")
    diccionario["Nombre"]=nombre
    diccionario["Edad"]=edad
    diccionario["Genero"]= genero
    diccionario["Direccion"]=direccion
    diccionario["Correo"]=correo
    dic[f'User{c}']=diccionario
    print(dic)
    nombre = input("Ingrese su nombre o salir: ")
    c +=1
    if nombre=="salir":
        break


# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste

compras = {}

o = input("Ingrese su items: ")

while o!="salir":
    costo = int(input("Ingrese el valor: "))
    compras[o]=costo
    o = input("Ingrese su items o salir: ")
    if o=="salir":
        break

suma = 0
for x, y in compras.items():
    suma += y
    print(f'{x} - {y} ')

print(f"El precio total es {suma}")

# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

traduccion = {}

palabra = input("Ingrese sus palabra en este formato <español:ingles> y las separa por ',' : ")
separadas_comas = palabra.split(",")

for i in separadas_comas:
    i = i.split(":")
    traduccion[i[0]]=i[1]
print(traduccion)

frase = input("Ingrese su frase para traducir: ")
separadas = frase.split(" ")
traducida = []
for i in separadas:
    traducida.append(traduccion[i])

palabraNueva=""
for j in traducida:
    palabraNueva+=  j + " "
print(palabraNueva)


# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
facturas = {}

menu = """
    ------  MENU  ------
    1 - Añadir Factura
    2 - Pagar Factura
    3 - Terminar
    Ingrese una opcion:
    """
opcion = input(menu)

while opcion!="3":
    
    if opcion=="1":
        numeroFactura = input("Ingrese el numero de su factura: ")
        costeFactura = input("Ingrese el coste de su factura: ")
        facturas[numeroFactura] = costeFactura
        deuda = 0
        for i in facturas.values():
            deuda += int(i)
        print(f'La cantidad pendiente es {deuda}')
        opcion = input(menu)
    if opcion=="2":
        numeroFactura = input("Ingrese el numero de su factura: ")
        facturas.pop(numeroFactura)
        deuda = 0
        for i in facturas.values():
            deuda += int(i)
        print(f'La cantidad pendiente es {deuda}')
        opcion = input(menu)
    if opcion=="3":
        print("Usted ha decidido finalizar el programa")
        print("Muchas gracias!")
        break

# Ejercicio 10
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.

# clientes = {'1': {'nombre': 'jorge', 'direccion': 'calle10', 'telefono': '3202020', 'correo': 'jorge@gmail.com', 'preferente': 'si'},'2': {'nombre': 'juan', 'direccion': 'calle11', 'telefono': '3202020', 'correo': 'juan@gmail.com', 'preferente': 'no'}}

clientes={}

menu = """
    ------------ MENU ------------
    1 - Añadir Cliente
    2 - Eliminar Cliente
    3 - Mostrar Cliente
    4 - Listar Todos los Clientes
    5 - Listar Clientes Preferentes
    6 - Terminar
    Ingrese una opcion:
    """
opcion = input(menu)

while opcion!="6":
    if opcion=="1":
        print("---------------  Añadir Cliente  -------------------")
        nif = input("Ingrese su NIF: ")
        cliente = {}

        nombre = input("Ingrese su nombre: ")
        direccion = input("Ingrese su direccion: ")
        telefono = input("Ingrese su telefono: ")
        correo = input("Ingrese su correo: ")
        preferente = input("Ingrese si es preferente si o no: ")

        cliente["nombre"]=nombre
        cliente["direccion"]=direccion
        cliente["telefono"]=telefono
        cliente["correo"]=correo
        cliente["preferente"]=preferente

        clientes[nif]=cliente
        print(clientes)
        opcion = input(menu)

    if opcion=="2":
        print("---------------  Eliminar Cliente  -------------------")
        nif = input("Ingrese su NIF: ")
        clientes.pop(nif)
        print(clientes)
        opcion = input(menu)
    if opcion=="3":
        print("---------------  Mostrar Clientes  -------------------")
        nif = input("Ingrese su NIF: ")
        clienteBuscar = clientes[nif]
        print(clienteBuscar)
        opcion = input(menu)
    if opcion =="4":
        print("----------  Mostrar todos los Clientes  --------------")
        print(clientes)
        opcion = input(menu)
    if opcion =="5":
        print("------ Mostrar todos los Clientes Preferentes --------")
        for i in clientes:
            # cliente =clientes[i]
            if clientes[i]["preferente"]=="si":
                print(clientes[i])
        opcion = input(menu)
    if opcion=="6":
        print

# Ejercicio 11
# El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

# "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"


# Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

# {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}

directorio ={}

contactos = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

contactoNuevo = contactos.split("\n")

for i in range(1,len(contactoNuevo)):
    titulo_separado = contactoNuevo[0].split(";")
    contacto_separado = contactoNuevo[i].split(";")

    contact = {}
    for i in range(1,len(titulo_separado)):
        
        contact[titulo_separado[i]]= contacto_separado[i]
        directorio[contacto_separado[0]]=contact
print(directorio)