#Ejercicio #2
#SOLICITA EL NOMBRE, EDAD Y NOTAS DE UNIVERSIDAD DE UNA PERSONA
#VAS A PEDIR UN TOTAL DE 5 NOTAS
#VAS A CALCULAR EL PROMEDIO DE NOTAS
#Y SI EL PROMEDIO ES INFERIOR DE 3, ENTONCES IMPRIME POR CONSOLA QUE PERDIO LA MATERIA,
#SI ES MAYOR O IGUAL A 3, ENTONCES IMPRIME GANASTE

name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
#subjects_notes=float(input("Enter your notes: "))

list=[]

for i in range(5):
    notes= float(input("Enter your notes "))
    list.append(notes)
    
average= (list[0] + list[1] + list[2] + list[3] + list[4]) / 5
    
if  average >= 3.0:
    print("You won")
else:
    print("you lost the subject")    