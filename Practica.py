#print("Escribe tu nombre: ")
#nombre = input()

#print("Escribe tu apellidos: ")
#apel = input()

#print("Escribe tu edad: ")
#edad = input()

#print("Escribe tu estatura: ")
#esta = input()

#print("Soy " + nombre + " " + apel + ", mi edad es " + edad + " años, y mi estatura es " + esta)


#nombre=input("ingrese tu nombre: ")
#edad=input("ingrese tu edad: ")
#h=input("ingrese tu estatura: ")

#print(f"Hola soy {nombre} mi edad es {edad} años y mi estatura es {h} metros " )

#numero_po= 12

#print(type(numero_po).__name__)

#op_1= True
#op_2= False

#resul= op_1 or op_2

#print(resul)

# identificar numero mayor

#num1=input("ingrese un numero: ")
#num2=input("ingrese un numero: " )
#num3=input("ingrese un numero: " )
#num4=input("ingrese un numero: " )

#if num1 > num2 :
#    if num1 > num3:
#        if num1 > num4:
#              print("El numero mayor es: ",num1)
#        else:
#                print("El numero mayor es: ",num4)
#    else:
#             print("El numero mayor es: ",num3)
#elif num2 > num3 :
#     if num2 > num4:
#      print("El numero mayor es: ",num2)            
#     else:
#      print("El numero mayor es: ",num4)           
#elif num3 > num4:
#    print("El numero mayor es:",num3)
#else:
#    print("El numero mayor es: ",num4)
 

 
#for indice in range(10): #Funcion For 
#     print(indice)
     

#for leer in work[::-1]: 
   # print(leer)       
    
"""def my_reverse():
    work = input("Enter a work: ")
    for x in work[::-1]:
       print(x, end="")  
    return work

my_reverse() 

work1 = my_reverse()

if work1 == work1[::1]:
    print("is a palindromo")
else:
    print("not is a palindromo")"""
    
""" # Diccionario


# definir diccionario
Person = {
    "name" : "David",
    "lastname" : "Palacios",
    "age" : 26,
    "id" : 1017268146,
    
}

# Eliminar un key en diccionario 
del Person["id"]

# agregar Un key en diccionario
Person["city"] = "choco"
 
print(Person)
print(Person["age"]) 

#recorrer dicionario con for 
for keys , values in Person.items():
    print(f"{keys} : {values}" )     


#validar valores duplicados 

names = ["antony","Kevin","David","Jefferson","Jefferson","sofia","lina","nicol" ]
countename = {}

for nombre in names:
    if nombre in countename:
        countename[nombre] += 1
    else:
        countename[nombre] = 1
print(countename) """  


"""Parte 1: Básicos
Crea un diccionario llamado auto que contenga:

Marca

Modelo

Año

Cambia el modelo del auto a otro diferente.

Agrega una nueva clave color al diccionario.

Elimina la clave año.

Imprime todas las claves del diccionario usando un bucle for.

Imprime todos los valores del diccionario usando un bucle for.

Parte 2: Intermedio
Crea un diccionario paises donde las claves sean nombres de países y los valores sus capitales.

Escribe un programa que pregunte al usuario un país y devuelva su capital (si existe).

Invierte el diccionario paises, es decir, que las capitales sean las claves y los países los valores.

Crea un diccionario de estudiantes donde las claves sean los nombres y los valores sus notas finales.
Después imprime los nombres de los estudiantes que aprobaron (nota mayor o igual a 6) """

#Parte 1
'''car = {
    
    "brand" : "toyota",
    "Model" : "Txl",
    "year" : 2025, 
}

print(car)

car["Model"] = "supra"

print(car)

car["color"] = "azul"

print(car)

del car["year"]

for keys in car:
    
    print(keys)

for values in car:
    
    print(car[values])'''
    
# parte 2

countrys={
    
    "colombia" : "Bogota",
    "argentina" : "Buenos aires",
    "Brasil" : "Brasilia",
    "Ecuador" : "Quito",
} 



while True:
    x = input("Enter a country: ")
    try:
        if x in countrys:
            print(countrys[x])
            break
        else:
            print("Not exists, enter other country")
    except ValueError:
            print("Not exists, enter other country")
            

invest = {keys:values for values, keys in countrys.items()}
print(invest)

#Parte 3

students ={
    "David" : 6,
    "Antony" : 5,
    "Sebas" : 4,
    "Carlos" : 8,
} 

for student in students:
    
    if students[student] >= 6:
        print(student)


