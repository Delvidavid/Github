'''1. Añadir productos al inventario: permitir al usuario agregar productos con atributos como
nombre, precio y cantidad disponibles.
2. Consultar productos en inventario: buscar un producto por su nombre y mostrar sus
detalles (nombre, precio, cantidad).
3. Actualizar precios de productos: modificar el precio de un producto específico en el
inventario.
4. Eliminar productos del inventario: permitir la eliminación de un producto que ya no está
disponible.
5. Calcular el valor total del inventario: multiplicar el precio por la cantidad de cada producto
y mostrar el total acumulado.'''

listProducts = [] #list for add the product enter for the usuary 

#Function of add products witn a limit of five products.
def add ():
    
    while True:
        
      cantProduct = input("How many products do you want to enter (minumun five Product)? :")
      cont = 0


      if cantProduct.isdigit() and int(cantProduct) >= 2:

        while cont < int(cantProduct):
          cont += 1
          print(f"Product #{cont}")
          

          products= input("Enter name of products: ")
          price= input("Enter products price without . and , : ")
          amount= input("Enter products amount: ")
        
          if price.isdigit() and amount.isdigit(): 
            
            productAdd = {products:{"price_product":float(price),"amount":float(amount)}}
            listProducts.append(productAdd)
            print("Product add with success")
        
          else:
            print("check the values of price and amount")
            cont -=1

      else :
        print("Enter a number eldery to 5, please")
 

      while True :
        question = str(input("you want to add another product? Y/N = ").lower())
    
        if question == "y":
          break
        elif question == "n":
          return 
        else:
          print("Enter y or N !")
                    
#Function of consult products by his name.
def consult():
    
    while True:
        
        productConsult = input("Enter product to consult: ")
        x=""
        for x in listProducts:
          if productConsult in x :   
            print (f"product information found:{x} ")
            break  
        if productConsult not in x: 
          print("Product not found")
          
        
        while True :
          question = str(input("Do you want consult another product? Y/N = ").lower())
    
          if question == "y":
            break
          elif question == "n" :
            return False
          else:
            print("Enter Y or N !")            

#Function of update price and amount the product elected.
def update():
   while True: 
      productUpdate = input("Enter product to update: ")
      x=""
      for x in listProducts:
        if productUpdate in x:
                
          while True:
            question = input("you want to update price(1) or amount(2) or borh(3)?: ").lower()
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

            elif question == "borh" or question == "3":
              priceProduct = input(f"Enter new price to product {productUpdate} : ")
              amountProduct = input(f"Enter new amount to product {productUpdate} : ")
              if priceProduct.isdigit() and amountProduct.isdigit():
                x[productUpdate]["price_product"] = float(priceProduct)
                x[productUpdate]["amount"] = float(amountProduct)
                print("Product update correctly")
                break
              else:
                print("worth incorrect")
            else:
              print("wrong option!!")
                    
      if productUpdate not in x:
        print("Product not found")    
        
      while True :
        question = str(input("Do you want update another product? Y/N = ").lower())
    
        if question == "y":
          break
        elif question == "n" :
          return False
        else:
          print("Enter Y or N !")

#Function of delete product only if the amount is 0. 
def delete():
    
  while True:
        
    productDelete = input("Enter product to delete: ")
    x=""
    for x in listProducts:
      if productDelete in x:
        if x[productDelete]["amount"] == 0:
          deleteQuestion = str(input("you sure of delete this product (Y/N) ?: ").lower())
          if deleteQuestion == "y":    
            del x[productDelete]
            print("Product delete witn success")
            break
          elif deleteQuestion == "n":
            break
          else:
            print("option not valid")
        else:
          print("The Product not this empty")
          break
    if productDelete not in x :
      print("Product not found")
         
    while True :
      question = str(input("Do you want update another product? Y/N = ").lower())
    
      if question == "y":
        break
      elif question == "n" :
        return 
      else:
        print("Enter Y or N !")    
                
#Function to display the total of the inventary.
def worthTotal():
    suma_price = 0
    for x in listProducts:
      for products in x: 
        suma = x[products]["price_product"] * x[products]["amount"]
        suma_price += suma 
                         
    print(f"The worth total of invetory is: {suma_price:.2f}")
        
#Main menu     
while True: 
    main = input('''
Enter a option: 
1. Añadir producto. 
2. Consultar productos.
3. Actualizar precio y cantidad.
4. Eliminar productos.
5. Calcular valor total del inventario.
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