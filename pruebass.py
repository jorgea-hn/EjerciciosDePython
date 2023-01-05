# a = ((1,2,3),(4,5,6))
# b = ((-1,0),(0,1),(1,1))  

# x = []

# mul = 0
# for i in b:
#     for j in i:
#         for m in a:
#             for n in m:

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


