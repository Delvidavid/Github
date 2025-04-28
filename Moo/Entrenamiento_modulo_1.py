#Sistama de validacion de productos
"""Eres un desarrollador junior en una empresa de software, y te han asignado la tarea de crear un
programa que calcule el costo total de una compra en una tienda. El programa debe interactuar con
el usuario a través de la consola, solicitando cuatro datos esenciales: el nombre del producto, el
precio unitario, la cantidad de productos adquiridos, y el porcentaje de descuento que se aplicará,
si es que existe alguno. Es fundamental que el programa maneje adecuadamente las entradas,
validando que tanto el precio como la cantidad sean números positivos, y que el descuento esté
dentro del rango aceptable de 0 a 100%.
Con estos datos, el programa debe calcular el costo total de la compra. Primero, debe determinar
el costo sin aplicar ningún descuento y, luego, si corresponde, aplicar el descuento especificado
para calcular el monto final. Además, este costo total debe ser mostrado junto con el nombre del
producto, de manera clara y formateada, asegurando que el resultado sea fácil de interpretar, por
ejemplo, presentando el valor con dos decimales.
Es importante que consideres la estructura y legibilidad de tu código, asegurándote de que esté
bien organizado y libre de errores. Por último, prueba el programa con distintos escenarios,
incluyendo casos extremos, para garantizar que funcione correctamente en todas las situaciones
posibles."""

list_subtotal=[]
list_discount=[]

while True:
         
        try:
            amount=input("How many products do you want to enter? :")
            if not amount.isdigit():
                True
                print("Enter a worth valid")
                
            else:
                
                print("...To Welcome...")
                break
        except:
            break
            
def Enter_Product():

    while True:
        product = input("Enter name product: ")
        try:
            
            if product.isalpha():
                True
                break
            else:
                print("Product not valid")
        except:
            break

cant=int(amount)

while True:
    
    try:
        for x in range(cant):
    
            #Definir variable con funcion input()
            Enter_Product()
            amount= input("Amount: ")
            unitary= input("worth unitary: ")
            percentage_product= input("Enter discount of the product: ")
    
            if unitary.isdigit()  > 0 and amount.isdigit() > 0 :
                #if 0 >= percentage_product.isdigit() <=0:
        
                unit_val=  float(unitary)
                percenetage = int(percentage_product)
                cant_val_= int(amount)
            
                sum_unitary = unit_val * cant_val_ 
                sum_subtotal = sum_unitary - ( sum_unitary * (percenetage / 100))
                discount = unit_val * (percenetage / 100)
                 
                list_discount.append(discount)
                list_subtotal.append(sum_subtotal)
        break    
                
    except:
        print("check the entered values")
        break
        


        
sum_total = sum(list_subtotal)
sum_discount = sum(list_discount)
print(f"discount total: {sum_discount}")
print(f"Total: {sum_total} ")



