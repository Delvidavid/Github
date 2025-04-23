#Ejercicio 4
#PIDE UN NUMERO AL USUARIO POR TERMINAL
#Y DETERMINA SI ES UN NUMERO PRIMO

num=int(input("Enter an number: "))

if num > 1:
    cont=0
    for i in range(2,num):
      resto= num % i 
      
      if resto==0:   
        cont+=1     
    if cont==0:
        print(f"the number {num} is couins")
    else:
        print(f"the number {num} not is couins")    
else:
    print(f"the number {num} not is couins")            
