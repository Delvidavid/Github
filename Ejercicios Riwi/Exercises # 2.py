#Hola Mundo personalizado
#Pide al usuario su nombre y muestra un saludo personalizado en pantalla.
#import re
def hello():
    
   while True:
    name = input("Enter you name: ")
    try: 
        if name.isalpha():
          print(f"Hello {name} ! is a pleasure know you.")
          break
        else:
            print("Enter corretly you name")
    except ValueError:
        print("Enter corretly you name")               
#hello() #Pendiente de Caracteres Especiales           

#Suma de dos números
#Solicita dos números al usuario, realiza la suma y muestra el resultado.

def suma():
    print ("Sum of two numbers")
    while True:
        
        try: 
            number1 = input("Enter the firts number: ")
            number2 = input("Enter the second number: ")
        
            if not number1.isalpha() and not number2.isalpha() :
                result= float(number1) + float(number2)
                print(f"you result is {result} !")
                break
            else:
                print("Review entered data ")
        except ValueError:
            print("Review entered data ")                               
#suma() 
        
#Conversión de temperatura
#Pide una temperatura en grados Celsius y conviértela a Fahrenheit. Muestra el resultado.

def degress():
    print("Convert degress celsius to fahrenheit")
    while True:
        
        celsius = input("Enter degress celsius what want convert to degress fahrenheit: ")
        
        if celsius.isdigit():
            
            celsius= float(celsius)
            fahrenheit= (celsius * 1.8) + 32
            print(f" {celsius} °C is {float(fahrenheit)} °F")
            break
        else:
            print("Enter a worth valid ")            
#degress() #pendiente de hacer la operacion con negativos

#Área de un rectángulo
#Pide al usuario la base y la altura de un rectángulo y calcula su área.

def area():
    
    print("Calculate area of a right triangle ")
    while True:
        try:
            base = input("Enter base in cm: ")
            height = input("Enter height in cm: ")
         
            if base.isdigit() and height.isdigit():
            
                base=float(base)
                height=float(height)
                area_total = (base * height) / 2
                print (f"The area of righr triangle is: {float(area_total)} cm²")
                break
            else:
                print("Enter worth valid")
        except ValueError:
            print("Enter worth valid")       
#area() #Pendiente de negativos

#Edad futura
#Pide al usuario su edad y muestra cuántos años tendrá dentro de 5 años 
             
def years():
    print("Age after of 5 years")
    
    while True:
        try:
            age = input("Enter you age: ")
        
            if age.isdigit():
           
                age = int(age)
                age_total = age + 5
                print(f"You age in 5 years is: {age_total}")
                break
            else:
                print("Enter an age valid")
        except ValueError:
            print("Enter an age valid")        
#years()

#Número positivo, negativo o cero
#Solicita un número y muestra si es positivo, negativo o igual a cero.

def numbers():
    
    print("identify wherter the numbers are positive, negative or zero")
    while True:
        
        try:
            number = input("Enter a number: ")
        
            if not number.isalpha():
                number=float(number) 
                if number > 0:
                    print(f"El number {number} is positive !")
                elif number < 0:
                    print(f"El number {number} is negative !")
                else:
                    print(f"El number {number} is zero !")    
                break        
        
            else:
                print("Enter a worth valid")
        except ValueError:
            print("Enter a worth valid")        
#numbers() 

#Par o impar
#Pide un número entero al usuario y muestra si es par o impar.

def even_odd():
    
    print("Identify a number whather even or odd !")
    while True:
        
        try:
            number = input("Enter a number: ")
            
            if  not number.isalpha():
                number = int(number)
                
                if number % 2 == 0 :
                    print(f"The number {number} is even !")
                else:
                    print(f"The number {number} is odd !")
                break
            else:
                print("Enter a worth valid !")        
        except ValueError:
            
            print("Enter a worth valid !")                 
#even_odd()

#Mayor de dos números
#Solicita dos números y muestra cuál es el mayor. Si son iguales, indícalo.

def bigger():
    
    print("Indetify if one number is greater than another !") 
    while True:
        
        try:
            number_1 = input("Enter first number: ")
            number_2 = input("Enter second number: ")
            
            if not number_1.isalpha() and not number_2.isalpha():
                number_1 = float(number_1)
                number_2= float(number_2)
                
                if number_1 > number_2:
                    print(f"The number {number_1} is greater than {number_2} !")
                else:
                    print(f"The number {number_2} is greater than {number_1} !")
                break        
            else:
                print("Enter worth valid")
        except ValueError:
            print("Enter worth valid")
#bigger()

#Calculadora simple
#Crea una pequeña calculadora que permita al usuario ingresar dos números y una operación (+, -, *, /) y luego muestre el resultado.

def calculator():
    
    print("operations math")
    
    while True:
        
        try:
        
            nunmber_1 = input("Enter first number: ")
            number_2 = input("Enter Second Number: ")
            Operations = input("Enter operations math: ")
        
            if not Operations.isdigit() and not Operations.isalpha():
                
                Operations = str(Operations)
                nunmber_1 = float(nunmber_1)
                number_2 = float(number_2)
                
                if Operations == "+":
                    
                    sum = nunmber_1 + number_2
                    print(f"the sum total is {sum}")
                
                elif Operations == "-":
                    
                    res = nunmber_1 - number_2
                    print(f"The remainder is {res}")
                    
                elif Operations == "/":
                    
                    division = nunmber_1 / number_2
                    print(f"The division is {division}")
                
                elif Operations == "*":
                    
                    multiplication = nunmber_1 * number_2
                    print(f"The multiplication is {multiplication} ")
                       
                else: 
                    
                    print("Enter a worth valid")  
            else:
                
                print("Enter a worth valid") 
        
        except ValueError:
                  
                  print("Enter a worth valid")                  
#calculator()

#Aprobado o reprobado
#Pide una nota del 0 al 100. Si es 60 o más, muestra “Aprobado”; si es menor, “Reprobado”.

def approved() :
    
    while True:
        
        try:
            note = input("Enter a note of 0 to 100: ")
            
            if note.isdigit() :
                
                note = int(note)
                
                if note > 60:
                    print("Approved")
                 
                else:
                    print("Reproved")
                break    
            
            else:
                print("Enter a worth valid")
        
        except ValueError:
            
            print("Enter a worth valid")            
#approved()     

#Suma de los primeros 10 números  
#Escribe un programa que use un bucle `for` para sumar los números del 1 al 10 y mostrar el resultado final.

def sum_numbers():
    result=0 
    for i in range(1,11):
            
            print(i)
            result += i 
    print(f"The result is: {result} ")
#sum_numbers()

#Mostrar caracteres en mayúscula
#Crea un programa que recorra una palabra carácter por carácter y muestre cada letra en mayúscula en una nueva línea.

def character():
    list = []
    
    word = input("Enter a word: ")
    
    for i in word:
        
        if  word.isalpha() :
            
            i = i.upper()
            list.append(i)
        else:
            
            print("Error enter a word")
            break   
                
    print(list)
#character()

#Tablas de multiplicar del 1 al 5  
#Haz un programa que muestre las tablas de multiplicar del 1 al 5. Cada tabla debe ir del 1 al 10.

def table():
    table_1 = 0
    table_2 = 0
    table_3 = 0
    table_4 = 0
    table_5 = 0
    for i in range(1,11):
         
        print(f"1 X {i} = {1}")
          
        
table()