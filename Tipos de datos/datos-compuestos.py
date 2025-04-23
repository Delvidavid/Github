 #Lista (Matrix) se ṕuede modificar
list =["David Palacios","Estoy muy motivado",True,1.90]

list[3]= "1.80"
print(list[3])

#tuple (Matriz)no se pueden modificar
tuple=("David Palacios","Estoy muy motivado",True,1.90)

#tuple(0)="David"
print(tuple[0])

# conjunto (Set) / No se accede por cada indice / no almacena datos duplicados / son datos desordenados
set={"David Palacios","Estoy muy motivado",True,1.90}
print(set)

# conjunto diccionario (dict) / estructura key : value

dict={
    'Nombre':"David",
    'Apellido':"Palacios",
    'Altura': 1.90,
    'Hombre':True,
}

print(dict['Nombre'])