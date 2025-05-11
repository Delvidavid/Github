'''
1-Añadir productos:
-Cada producto debe estar definido por su nombre, precio y cantidad disponible
-Esta información será almacenada de modo que el inventario pueda crecer dinámicamente

2-Consultar productos:
-Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
-Si el producto no está en el inventario, se debe notificar adecuadamente

3-Actualizar precios:
-El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario

4-Eliminar productos:
-El programa debe permitir al usuario eliminar productos del inventario de manera segura

5-Calcular el valor total del inventario:
-El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
-Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.'''


# Definir una lista para los productos
listProducts = []

#funsion para agregar productos a las lista
def add ():
    
    while True:
        products= input("Enter name of products: ")
        price= input("Enter products price without . and , : ")
        amount= input("Enter products amount: ")
        
        if price.isdigit() and amount.isdigit(): 
            
            productAdd = {products:{"price_product":float(price),"amount":float(amount)}}
            listProducts.append(productAdd)
            print("Product add with success")
        
        else:
            print("check the values of price and amount")
            
        while True :
            question = str(input("you want to add another product? Y/N = ").lower())
    
            if question == "y":
                break
            elif question == "n":
                return False
            else:
                print("Enter y or N !")
                    
#fusion para consultar los productos con for para recorrer la lista.
def consult():
    
    while True:
        
        productConsult = input("Enter product to consult: ")
        
        for x in listProducts:
            while productConsult in x : 
                
                print (f"product information found:{x} ")
                break
            else:
                print("Product not found")
            
                
        while True :
            question = str(input("Do you want consult another product? Y/N = ").lower())
    
            if question == "y":
                break
            elif question == "n" :
                return False
            else:
                print("Enter Y or N !")            

#Actualizar precio o cantidad ya depende de la opcion escogida
def update():
   while True: 
        productUpdate = input("Enter product to update: ")
    
        for x in listProducts:
            if productUpdate in x:
                
                while True:
                    question = input("you want to update price(1) or amount(2)?: ").lower()
                    if  question == "price" or question == "1": 
                        priceProduct = input(f"Enter new price to product {productUpdate} : ")
                        if priceProduct.isdigit():
                            x[productUpdate]["price_product"] = float(priceProduct)
                            print("Product update correctly")
                            break
                        else:
                            print("worth incorrect")
                            
                    elif question == "amount" or question == "2":   
                        amountProduct = input(f"Enter new amount to product {productUpdate} : ")
                        if amountProduct.isdigit():
                            x[productUpdate]["amount"] = float(amountProduct)
                            print("Product update correctly")
                            break
                        else:
                            print("worth incorrect")
                    else :
                        print("wrong option!!")
                    
            else:
                print("Product not found")    
        
        while True :
            question = str(input("Do you want update another product? Y/N = ").lower())
    
            if question == "y":
                break
            elif question == "n" :
                return False
            else:
                print("Enter Y or N !")

 
#Eliminar productos 
def delete():
    
    while True:
        
        productDelete = input("Enter product to delete: ")
        
        for x in listProducts:
            
            if productDelete in x:
                
                del x[productDelete]
                
            else :
                print("Product not found")
         
        while True :
            question = str(input("Do you want update another product? Y/N = ").lower())
    
            if question == "y":
                break
            elif question == "n" :
                return False
            else:
                print("Enter Y or N !")    
                

#muestra el total de el inventario
def worthTotal():
    suma_price = 0
    for x in listProducts:
        for priceTotal in x: 
            suma = x[priceTotal]["price_product"]
            suma_price += suma 
                         
    print(f"The worth total of invetory is: {suma_price}")
        
    
while True: 
    main = input('''
Enter a option: 
1. Añadir Producto 
2. Consultar Productos
3. Actualizar Precios
4. Eliminar Productos
5. Calcular Promedio Del Inventario
6. Salir  
= ''').lower() 
    
    match main:
        
        case "1":
            
            add()
        
        case "2":
            
            consult()
            
        case "3":
            
            update()
        
        case "4":
            
            delete()
        
        case "5":
            
            worthTotal()    
            
        case "6" | "out" | "salir":
            break
        
        case _:
             
            print("Enter a option valid")
            