#Ejecicio 5
#PIDE POR TERMINAL QUE INGRESEN UN NUMERO ENTERO,
#SINO ES ENTERO, ENTONCES IMPRIME UN MENSAJE DE ERROR DICIENDO QUE NO SE ACEPTAN DECIMALES
#ADICIONAL, SI EL NUMERO ES MULTIPLO DE 3, IMPRIME LA PALABRA "FIZZ"
#SI EL NUMERO ES MULTIPLO DE 5, IMPRIME LA PALABRA "BUZZ"
#Y SI ES MULTIPLO DE 15, IMPRIME LA PALABRA "FIZZBUZZ"
         
while True:
    num=(input("ingrese numero: "))
        
    if num.isdigit() :
        numero = int(num)
        
        
        if numero % 3 == 0 and numero % 5 == 0:
            print("Fizzbuzz")
    
        elif numero % 5 == 0:
            print("Buzz")    
    
        elif numero % 3 == 0:
         print("Fizz")
    
        else:
            print(f"El numero {num} no es multiplo ni de el 3 ni del 5")
        
        break

    else:
        print("Ingresa un numero valido")
        continue