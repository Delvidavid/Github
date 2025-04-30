"""Mini-proyecto: "Agenda de Contactos"
Descripción:
Crea una pequeña agenda que permita:

Agregar un nuevo contacto (nombre y número de teléfono).

Buscar un contacto por su nombre.

Mostrar todos los contactos.

Eliminar un contacto.

Requisitos:
Usar un diccionario donde el nombre sea la clave y el número sea el valor.

Crear un pequeño menú en consola para elegir las acciones."""

agenda = {}

while True:
    
    crud = input('''
Enter a option: 
1. create 
2. read
3. update
4. delete 
5. out  
= ''').lower()
    
    match crud:
        
        case "create" | "1":
                
                keys = input ("Enter a contact: ")
                values = input(F"Entre a phone of {keys} :"   )
                new = {keys : values}
                agenda.update(new)
                print(f"Contact create with success {agenda} ")
               
                #newContact = input("create other contact S/N: ").lower()
             
        case "read" | "2" :
            
            read = input("Enter contact to search: ")
            
            if read in agenda:
                print(f"contact {agenda}" )
            
            else:
                print("Not Exist contact")
        
        case "update" | "3":
            
            update = input("Enter contact to update: ")
            
            if update in agenda:
                
                newValues = input("Enter new number of contact: ")
                
                agenda.update({keys:newValues})
                
                print(agenda)
                print("Update with success")
                
                
            else:
                print("Not Exist contact")
        
        case "delete" | "4":
            
            delete = input("Enter contact to delete: ")
            
            if delete in agenda:
                del agenda[delete]
                print("Contact delete with success")
                print(agenda)
            else:
                print("there is not contact to delete ") 
                
        case "out" | "5":
            
            break   
        

                