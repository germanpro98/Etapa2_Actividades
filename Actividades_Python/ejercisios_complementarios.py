#1.creando y mostrando un diccionario de frutas con sus respectivos precios.
frutas = {"manzana" : 10.2, "naranja" : 12.3, "sandia" : 20.0}
print("Frutas y precios:", frutas)

#2.creando y mostrando una lista de ciudades.
ciudades = ["Madrid", "Barcelona", "Valencia"]
print("Ciudades:", ciudades)
#3.agregando una ciudad a la lista.
ciudades.append("Sevilla")
print("Ciudades actuales:", ciudades)

#4.creando y mostrando una lista de paises. Mostrando el pais en la posicion 2.
paises = ["Francia", "Italia", "Alemania"]
print("Paises:", paises)
print("Pais en la posicion 2:", paises[1]) 

#5.creando un diccionario con el nombre de tres personas y sus edades. Mostrando la edad de la tercer persona.
personas = {
    "Juan": 25, 
    "Ana": 30, 
    "Luis": 22
    }
print("Personas y edades:", personas)   
print("La tercer persona del diccionario tiene", personas["Luis"], "años.") #---OPCION 1---se sabe cual fue el ultimo elemento agregado al diccionario.
print("La tercer persona del diccionario tiene", personas.get("Luis"), "años.")#---OPCION 2---no se sabe cual fue el ultimo elemento agregado al diccionario.

#6.creando un set/conjunto con los números del 1 al 10 y mostrando el número mas grande.
num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numero_mas_grande = max(num)
print("el número mas grande es:",numero_mas_grande)

#7.creando un set/conjunto con los números impares del 1 al 10 y mostrando el número de elementos en el conjunto.
numeros_impares = {1, 3, 5, 7, 9}
print("Números impares del 1 al 10:", numeros_impares)
print("Número de elementos en el conjunto de números impares:", len(numeros_impares))

#7-Creando un diccionario con los nombres de tres ciudades y sus respectivas poblaciones. Agregando una cuarta ciudad con su respectiva población.
ciudades_poblaciones = {
    "Madrid": 3200000,
    "Barcelona": 1600000,
    "Valencia": 800000
}
ciudades_poblaciones["Sevilla"] = 700000
print("Ciudades y poblaciones:", ciudades_poblaciones)

#8.Creando una lista con los números del 1 al 10 y mostrarlos en orden inverso.
numeros = [1,2,3,4,5,6,7,8,9,10]
#--------OPCION 1--------
num_inverso = list(range(1, 11))
num_inverso.reverse()
print("Números del 1 al 10 en orden inverso:", num_inverso)
#--------OPCION 2--------
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
invertido = numeros[::-1]
print("Números del 1 al 10 en orden inverso:", invertido)

#9.creando y mostrando una lista con los nombres de tres países en orden alfabético.
paises = ["Francia", "Rusia", "Alemania"]
paises.sort()
print("Paises en orden alfabético:", paises)

#10.creando una lista con los nombres de tres frutas y eliminando la segunda fruta de la lista. 
frutas = ["manzana", "naranja", "sandia"]
print("Frutas originales:", frutas)
frutas.pop(1)  
print("Lista final después de eliminar la segunda fruta:", frutas)

#11.creando una lista con los nombres de tres animales y agregando un cuarto animal al principio de la lista. 
animales = ["perro", "gato", "conejo"]
print("Animales originales:", animales)
animales.insert(0, "elefante")
print("Lista final después de agregar un cuarto animal al principio:", animales)

#12.creando una lista con los nombres de tres países y reemplazando el segundo país de la lista por otro país.
paises = ["Australia", "Suiza", "Argentina"]
print("Paises originales:", paises)
paises[1] = "Canadá"
print("Lista final después de reemplazar el segundo país:", paises)

#13.creando una lista con los nombres de tres colores y agregando dos colores más al final de la lista.
colores = ["negro", "amarillo", "azul"]
print("Colores originales:", colores)
colores.extend(["blanco", "morado"])
print("Lista final después de agregar dos colores más al final:", colores)

#14.creando una tupla con los números del 1 al 5 y mostrando la suma de todos los elementos de la tupla. 
numeros = (1, 2, 3, 4, 5)
suma_numeros = sum(numeros)
print("Suma de los números del 1 al 5:", suma_numeros)




