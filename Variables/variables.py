#definicion de variable
nombre = "Crack "

#definicion de variable con CamelCase
NombreDeTuHermano = "sebas"

#definicion de variable con snake_Case
nombre_de_tu_hermano = "sebas"

#concatenar con +
bienvedido= "hola " + nombre + "Como estas?"

#concatenar con f-strings
bienvedido = f"hola {nombre} Como estas?"

#eliminar variable
del bienvedido
print(bienvedido)

#operadores de pertenencia(in / not in )

print("hola" not in bienvedido) #false
print("hola"  in bienvedido) #true