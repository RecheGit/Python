#Ejercicio 1
# Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
'''
def max_in_list(lista):
    if len(lista)==0:
        print("La lista esta vacia")
    else:
        max=-9999 # pondria 0 pero si hay numeros negativos es mas seguro
        for x in lista:
            if max < x:
                max=x
    return max

l=[-55,-33,-56,-1,90,-11]
print(max_in_list(l))

'''
#Ejercicio 2
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
'''
def funcion_mas_larga(lista):
    if len(lista)==0:
        print("Lista vacia")
    else:
        max=""
        for x in lista:
            if len(x)> len(max):
                max=x
    return max

l=["","hola","","huevo","asdasdasdasd"]
print(funcion_mas_larga(l))

'''

#Ejercicio 3
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
'''
def filtrar_palabras(lista,n):
    if len(lista)==0:
        print("Lista vacia")
    else:
        l=[]
        for x in lista:
            if len(x)>n:
                l.append(x)
    return l

lis=["asdasdsad","aaaaaaaaaaa","uva","gol"]
print(filtrar_palabras(lis,6))

'''

#Ejercicio 4
#Pedir un array y encontrar numero de mayusculas

'''
def pedir_y_mayus():
    control=False
    while control==False:
        n=int(input("Introduzca la cantidad de elementos que desee añadir a la lista: "))
        if n>0:
            control=True
        else:
            print("Seleccion no valida, seleccione un numero valido")
    i=0
    l=[]
    cont=0
    while i<n:
        palabra=str(input("Introduzca una palabra: "))
        l.append(palabra)
        for char in palabra:
            if char==char.upper(): 
                cont=cont+1
        i=i+1
    return cont

print(pedir_y_mayus())

'''

#Ejercicio 5
#Construir un pequeño programa que convierta números binarios en enteros.

def convertidor_entero_a_binario():
    correcto=False
    while correcto==False:
        bin=int(input("Introduzca el numero en binario a convertir: ")) 
        if type(bin)!= int:
            print("Introduzca un numero valido") #No sirve para nada porque la condicion del input hace que salte error 
        else:
            entero=0
            while ''


            




    