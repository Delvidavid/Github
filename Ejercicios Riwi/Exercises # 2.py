#Hola Mundo personalizado
#Pide al usuario su nombre y muestra un saludo personalizado en pantalla.

def hello():
    
   while True:
    name = input("Enter you name: ")
    try: 
        if name.isalpha():
          print(f"Hello {name} ! is a pleasure know you.")
          break
        else:
            print("Enter corretly you name")
    except:     
         break  
#hello()           

#Suma de dos números
#Solicita dos números al usuario, realiza la suma y muestra el resultado.

def suma():
    print ("Sum of two numbers")
    while True:
        
        number1 = input("Enter the firts number: ")
        number2 = input("Enter the second number: ")
        
        if number1.isdigit() and number2.isdigit():
            result= float(number1) + float(number2)
            print(f"you result is {result} !")
            break
        else:
            print("Review entered data ")           
#suma()
        
#Conversión de temperatura
#Pide una temperatura en grados Celsius y conviértela a Fahrenheit. Muestra el resultado.

def degress():
    print("Convert degress celsius to fahrenheit")
    while True:
        
        celsius = input("Enter degress celsius what want convert to degress fahrenheit: ")
        
        if celsius.isdigit():
            
            celsius= int(celsius)
            fahrenheit= (celsius * 1.8) + 32
            print(f" {celsius} °C is {int(fahrenheit)} °F")
            break
        else:
            print("Enter a worth valid ")            
#degress()

#Área de un rectángulo
#Pide al usuario la base y la altura de un rectángulo y calcula su área.

def area():
    
    print("Calculate area of a right triangle ")
    while True:
        
        base = input("Enter base in cm: ")
        height = input("Enter height in cm: ")
         
        if base.isdigit() and height.isdigit():
            
            base=int(base)
            height=int(height)
            area_total = (base * height) / 2
            print (f"The area of righr triangle is: {int(area_total)} cm²")
            break
        else:
            
            print("Enter worth valid")       
#area() 

                           