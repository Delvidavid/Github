
'''
1- Determinar el estado de aprobación:
a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
b. Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

2- Calcular el promedio:
a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
b. Calcular y mostrar el promedio de las calificaciones en la lista

3- Contar calificaciones mayores:
a. Preguntar al usuario por un valor específico
b. Contar cuántas calificaciones en la lista son mayores que este valor

4- Verificar y contar calificaciones específicas
a. Preguntar al usuario por una calificación específica. 
b. Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa.''' 

#Determinar el estado de aprobación        
def aproval_Status():
    while True:
        try:
            notes = int(input("Enter note of 0 to 100: "))
        
            if notes >= 0 and notes <= 100:    
                if notes >= 60:
                    print("Approved")
                else:
                    print("Reporbate") 
            else:
                print("Enter a number between 0 and 100")
                continue    
        except ValueError:
            print ("Enter a number, Please")
    
        while True :
            question = str(input("want to continue S/N = ").lower())
    
            if question == "s" :
        
                break
    
            elif question == "n"   :
            
                return
    
            else:
                print("Enter S or N !")                                       


# Calcular el promedio  
def average():
    
  while True:  
      
    notes =input("Enter notes separated for commas(,) : ").split(",")
    listNotes = []
    SumNotes = 0
    averageNotas = 0
        
    try:
        
        for x in notes:
            notesNumber = float(x.strip())
            
            if notesNumber >= 0 and notesNumber <= 100 :
                listNotes.append(notesNumber)
            
                SumNotes += float(x)
                divisor = len(listNotes)    
                averageNotas = SumNotes / divisor
            else:
                print(f" Error {notesNumber} Enter number >= 0 and <=100 , please")
            
    except ValueError:
        print("Enter a worth valid")
    print(f"the averge of the notes enter is: {averageNotas}")
    
    while True :
        question = str(input("want to continue S/N = ").lower())
    
        if question == "s" :
        
            break
    
        elif question == "n"   :
            
            return
    
        else:
            print("Enter S or N !")


#Verificar calificaciones mayores
def notes_Greater():
    
    while True:
        
        listQualification = [20,40,60,80,100]
        cont = 0
        try:
            user = int(input("Enter a qualification: "))
            for x in listQualification:
                
                if user < x :
                    cont += 1
        except ValueError:
            print("Enter a worth valid")
    
        print(f"there {cont} qualificaciones greater than {user}")
        
        while True :
            question = str(input("want to continue S/N = ").lower())
    
            if question == "s" :
        
                break
    
            elif question == "n"   :
            
                return
    
            else:
                print("Enter S or N !")                              
             
#Verificar y contar calificaciones             
def notesSpecific ():
    
    while True:
        
        listNotes = [40,40,80,60,70,20,20,30,90]
        cont = 0
        try:
            qualification = int(input("Enter qualification for find out: "))
            
            for x in listNotes:
                
                if qualification == x:
                    cont += 1
                    continue
            
            if cont == 0 :
                print("values not found")
                             
        except ValueError:
            print("Enter a worth valid")
            
        print(f"The quaification {qualification} is repeats {cont} occasions")    
            
        while True :
            question = str(input("want to continue S/N = ").lower())
    
            if question == "s" :
        
                break
    
            elif question == "n"   :
            
                return
    
            else:
                print("Enter S or N !")           


while True:
    
    main = input('''
Enter a option: 
1. Determinar estado de aprovacion 
2. Calcular el promedio
3. Verificar calificaciones mayores
4. Verificar y contar calificaciones
5. salir  
= ''').lower()
    
    match main:
        
        case "1":
            
            aproval_Status()
        
        case "2":
            
            average()
            
        case "3":
            
            notes_Greater()
        
        case "4":
            
            notesSpecific()
            
        case "5" | "out" | "salir":
            break
                                             