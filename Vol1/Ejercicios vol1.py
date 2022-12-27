

#EJERCICIO 1
'''
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
python tiene una función max() incorporada, pero no vale usarla.
'''
'''
def maximo(n1,n2):
    if n1 > n2:
        x=n1
    elif n1==n2:
        print("Son iguales")
        x=-1
    else:
        x=n2
    print(x)

maximo(3,1)
maximo(9,6)
maximo(9,9)


#EJERCICIO 2
'''
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
'''

def max_de_tres(n1,n2,n3):
    if n1>n2:
        x=n1
        if x<n3:
            x=n3
    else:
        if n2<n3:
            x=n3
        else:
            x=n2
    print(x)

max_de_tres(1,2,3)
max_de_tres(3,2,1)
max_de_tres(1,3,2)



#EJERCICIO 3

'''
#Definir una función que calcule la longitud de una lista o una cadena dada.Sin usar la funcion len()
'''
l=[1,2,3,4,5]

def longitud(l):
    count=0
    for x in l:
        count=count+1
    print(count)

longitud(l)

si la longitud de que el menor niño sea superior al inclusive


#EJERCICIO 4
'''
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''
def es_vocal(letra):
    vocales=["a","e","i","o","u"]
    if  (letra in vocales):
        resultado=True
    else:
        resultado=False
    return resultado


print(es_vocal("a"))
print(es_vocal("w"))
'''

#Ejercicio 5

'''
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

l=[1,2,3,4,5]
def sumarL(lista):
    resultado=0
    for x in lista:
        resultado=resultado+x
    print(resultado)

sumarL(l)


def multiplicacion(lista):
    res=1
    x=0
    while x < len(lista):
        res=res*lista[x]                                                                                                                                                        +
        x=x+1
    print(res)
multiplicacion(l)
print(len(l))
+

6- Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

cadena=["estoy probando"]
cadena_separada=list(cadena[0])

def inversa(lista):
    ifin=len(lista)-1
    print(lista[ifin])
    rdo=[]
    while ifin >= 0: 
        if lista[ifin]!= ",":
            char1=lista[ifin]
            rdo.insert(len(rdo),char1)
        ifin=ifin-1
    return rdoc

paco= inversa(cadena_separada)


'''