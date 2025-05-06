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

#dictProducts ={}
listProducts = []

def add ():
    
    while True:
        
        try:
            products = input("Enter name of products: ")
            price = float(input("Enter products price: "))
            amount = float(input("Enter products amount: "))
            
            
            if price >= 0 and amount > 0: 
                
                productsAdd = {"name_product":products,"price_product":price,"amount":amount}
                listProducts.append(productsAdd)
                print("Product add with success")
                
            else:
                print("The price and tha amout they must be > 0")    
     
        except ValueError:
            
            print("check the entered values")
            
        while True :
            question = str(input("you want to enter another product? Y/N = ").lower())
    
            if question == "y":
                break
            elif question == "n":
                return False
            else:
                print("Enter y or N !")    
            
add()


def consult():
    
    while True:
        
        
        try:
            productConsult = str(input("Enter product to consult: "))
        
            for x in listProducts:
            
                if x['name_product'] == productConsult: 
                    print (f"product information found:{x} ")
                else:
                    print("Product not found")
                
        except ValueError:
            print("Enter the product name")
            
        while True :
            question = str(input("Do you want consult another product? Y/N = ").lower())
    
            if question == "y":
                break
            elif question == "n" :
                return False
            else:
                print("Enter Y or N !")            
consult()
