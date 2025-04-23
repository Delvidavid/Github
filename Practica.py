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

num1=input("ingrese un numero: ")
num2=input("ingrese un numero: " )
num3=input("ingrese un numero: " )
num4=input("ingrese un numero: " )

if num1 > num2 :
    if num1 > num3:
        if num1 > num4:
              print("El numero mayor es: ",num1)
        else:
                print("El numero mayor es: ",num4)
    else:
             print("El numero mayor es: ",num3)
elif num2 > num3 :
     if num2 > num4:
      print("El numero mayor es: ",num2)            
     else:
      print("El numero mayor es: ",num4)           
elif num3 > num4:
    print("El numero mayor es:",num3)
else:
    print("El numero mayor es: ",num4)
   