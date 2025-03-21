def factorialI (n):
    factorial=1
    for i in range (2, n+1):
        print("i:", i)
        factorial*=i
    return factorial

def factorialR(n):
    if n<0:
        raise TypeError("No se puede obtener el factorial de valores negativos")
    if n<=1:
        return 1
    else:
        return n * factorialR(n-1)
        

#Función iterativa que recibe una lista cuyos elementos son listas de enteros
#la función debe devolver la suma de los valores de TODAS las listas

def sumLista1I(l):
    sumTotal=0
    for i in l:
        print("i:",i, "sum", sum(i))
        sumTotal+=sum(i)
    return sumTotal

def sumLista2I(l): #hace lo mismo que sumLista1 pero sin utilizar SUM
    sumTotal=0
    for i in l:
        for j in i:
            sumTotal+=j
    return sumTotal


def sumLista2R(l):
    if len(l) == 0:
        return 0
    else:
        return sum(l[0]) + sumLista2R(l[1:])




lista=[[10,2,4],[100,6,90],[1,1,14],[2,2,2],[456,4],[40]]

print("Suma lista1I:", sumLista1I(lista))


print("factorialI(4):", factorialI(4))
print("factorialR(4):", factorialR(4))

print("Suma lista2I:", sumLista2I(lista))

print("Suma lista2R:", sumLista2R(lista))