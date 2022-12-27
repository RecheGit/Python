#Comentarios en python

'''Comentarios en mas de una linea
asdasdasd
asdasdasd
'''

print("Hola mundo") #print para mostrar por pantalla

#con type conseguimos saber de que tipo es lo que estamos escribiendo

print(type(2))#Nos muestra int
print(type("asd"))#Nos muestra str
print(type("a"))#Muestra String porque un char se considera un string de length 1 en python

#Listas Python(Int,String,Mix,Vacia)
[1,2,3,4,5,6]
["aa","dfaes"]
[10,"eds",10.3,True,7]
[]

#Diccionarios(es como una lista pero guarda distinta informacion del mismo elemento)
{
    "Nombre": "Cristiano",#Nombre es la clave y Cristiano es el Objeto
    "Apellido":"Ronaldo"
}

#################VARIABLES###############

name="Hola"
print(name)
a=1

nom,nnum = "Adri",3 #otra forma para guardar valores de una variable
print(nom)

#################LISTAS###############
r = list(range(1,11))#lista del 1 al 10. Con el list conseguimos crear una lista y con el range conseguimos meter numeros del 1-10 sin tener que ir uno a uno
print(r)
print(r[0])#primer elemento
print(r[-1])#ultimo elemento
print(3 in r)#saber si pertenece a la lista


#anadir objeto al final de la lista 2 formas
r.append(5)
r.insert(len(r),"csidhbvil")
print(r)


r.insert(0,100)#anadir objeto en la posicion que quiera
print(r)



#juntar dos listas en una
cd=[1,3]
print(r+cd)
r.insert(len(r),"csidhbvil")


#################CONDICIONALES###############

if 1*2>5:
    print("Hola")
else:
    print("Adios")

if 1*1==1:#comparacion
    print("siiiiii")


#################LOOPS###############
nka=[1,2,3,4,5]
#Imprime todos menos el 4
for x in nka:
    if x==4:
        continue
    print(x)
#Imprime hasta el 4
for x in nka:
    if x==4:
        break
    print(x)


count=4
x=0
while x <= count:
    print(x)
    x=x+1



#################FUNCIONES###############

def bienvenida():
    print("Bienvenido")

bienvenida()

def bienvenida_pers(x):
    print("Bienvenido "+x)

x="Juanillo"
bienvenida_pers(x)