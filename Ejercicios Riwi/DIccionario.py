agenda = {}
list = []
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
                
                contact = input ("Enter a contact: ")
                number = input(F"Entre a phone of {contact} :"   )
                new = {"name" : contact , "iphone" : number}
                #agenda.update(new)
                print(f"Contact create with success {agenda} ")
                list.append(new)
                print(list)
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
                
                agenda.update({contact:newValues})
                
                print(agenda)
                print("Update with success")
                
                
            else:
                print("Not Exist contact")
        
        case "delete" | "4":
            
            delete = input("Enter contact to delete: ")
            
            for usuario in list:
                print(list)
                #if usuario == :
                #   print("Usuario encontrado", usuario)
                
                
               # del list[delete]
                #print("Contact delete with success")
                #print(agenda)
            #else:
             #   print("there is not contact to delete ") 
                
        case "out" | "5":
            
            break   