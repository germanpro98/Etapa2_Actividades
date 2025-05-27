#*Ejercisio 1:Gestion de una lista de compras*

lista_compras = [] #creando lista vacia.
lista_compras.append("cemento") #agregando un elemento a la lista.
lista_compras.append("cal") #agregando un elemento a la lista.
lista_compras.append("arena") #agregando un elemento a la lista.  
print(lista_compras) #mostrando la lista.
print(len(lista_compras)) #mostrando la lista y la cantidad de elementos que hay en ella.
lista_compras.pop() #eliminando el ultimo elemento de la lista.
print(lista_compras) #mostrando la lista actualizada. 
print(len(lista_compras)) #mostrando la cantidad de elementos que hay en la lista actualizada.

#*Ejercicio 2:Contar apariciones*

colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"] #creando una lista con colores.
print(colores) #mostrando la lista para luego ver la modificación.
print(f"El color rojo aparece", colores.count("rojo"), "veces.") #contando y mostrando la cantidad de veces que aparece el color rojo en la lista.
reemplazo_verde = colores.index("verde") #buscando el indice del color verde en la lista.
colores[reemplazo_verde] = "amarillo" #reemplazando el color verde por amarillo en la lista.
print(colores) #mostrando la lista actualizada.

#*Ejercicio 3:Diccionario de estudiante*

estudiante = {
    "nombre": "Ana", #agregando el nombre del estudiante.
    "apellido": "Pérez", #agregando el apellido del estudiante.
    "edad": 20, #agregando la edad del estudiante.
    "materias": ["Matemáticas", "Historia"] #agregando las materias que tiene el estudiante.
    } #creando un diccionario.
print(estudiante) #mostrando el diccionario para luego observar las modificaciones.
print("Nombre:", estudiante["nombre"]) #mostrando el nombre del estudiante.
print("Edad:", estudiante["edad"]) #mostrando la edad del estudiante.
estudiante["materias"].append("Física") #agregando una materia al estudiante.
cantidad_materias = len(estudiante["materias"]) #contando la cantidad de materias que tiene el estudiante.
print(f"El estudiante tiene ", cantidad_materias, "materias.") #mostrando la cantidad de materias que tiene el estudiante.
promedio = estudiante.get("promedio", 0)
print("Promedio:", promedio) #mostrando el promedio del estudiante.