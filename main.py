# ----------------- CONSIGNA -----------------

# Crear un programa donde se ingresen datos de varias personas (nombre, edad, nota).  
# Al finalizar el programa por alguna opcion ( finalizar o terminado ) 
# mostrar el listado completo de datos cargados y otro listado ordenado por nota de mayor a menor. 


# ----------------- DESARROLLO -----------------

# Un array vacío para guardar los datos que ingresa el usuario
PERSONAS_REGISTRADAS = []

# Ingresar cantidad de usuarios 
usuarios_a_registrar = int(input("Ingrese una cantidad total de usuarios para el registro!: "))

# Iteramos sobre cada input
for _ in range(usuarios_a_registrar):
    
    # Inputs de usuarios
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("ingresar tu edad: "))
    nota = float(input("nota: ")) 

    datos_personas = [nombre, edad, nota]
    PERSONAS_REGISTRADAS.append(datos_personas)
    
    print (f"{nombre} tiene {edad} de años!, y su nota actual es de: {nota}")

# Mostramos por consola un array con cada registro
print("\nListado completo:")
[print(f"Nombre: {p[0]}, Edad: {p[1]}, Nota: {p[2]}", p) for p in PERSONAS_REGISTRADAS]

# Syntaxis para generar un nuevo array que cumplan con la condición:
#
#   newlist = [expression for item in iterable if condition == True]

print("\nListado ordenado por nota (mayor a menor):")

# "Un uso frecuente es ordenar objetos complejos utilizando algunos de los índices del objeto como clave" 
# https://docs.python.org/es/3/howto/sorting.html 
# x: x[2]

# reverse=
# False ordenará en ascendente, mientras que True ordenará en descendente. El valor predeterminado es False.
notas_ordenadas_mayor_menor = sorted(PERSONAS_REGISTRADAS, key=lambda x: x[2], reverse=True)


[print(f"Nombre: {p[0]}, Nota: {p[2]}") for p in notas_ordenadas_mayor_menor]
